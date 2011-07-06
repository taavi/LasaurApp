
import time
import os.path
import wsgiref.simple_server
from bottle import *
import serial_manager, serial


ARDUINO_PORT = '/dev/tty.usbmodem621'
BAUDRATE = 9600

current_dir = os.path.dirname(os.path.abspath(__file__))


def run_with_callback(host='127.0.0.1', port=8080, timeout=0.01):
    """ Start a wsgiref server instance with control over the main loop.
        This is a function that I derived from the bottle.py run()
    """
    handler = default_app()
    server = wsgiref.simple_server.make_server(host, port, handler)
    server.timeout = timeout
    print "Bottle server starting up ..."
    print "Listening on http://%s:%d/" % (host, port)
    print "Use Ctrl-C to quit."
    print
    while 1:
        try:
            serial_manager.send_queue_as_ready()
            server.handle_request()
        except KeyboardInterrupt:
            break
    print "\nShutting down..."
    serial_manager.close()



@route('/hello')
def hello_handler():
    return "Hello World!!"

@route('/connect')
def connect_handler():
    global arduino_port, baudrate
    try:
        serial_manager.connect(ARDUINO_PORT, BAUDRATE)
        ret = "Serial connected to %s:%d." % (ARDUINO_PORT, BAUDRATE)  + '<br>'
        time.sleep(0.5) # allow some time to receive a prompt/welcome
        return serial_manager.get_responses('<br>')
    except serial.SerialException:
        print "Failed to connect to serial."    
        return ""    

@route('/longtest')
def longtest_handler():
    fp = open("longtest.ngc")
    for line in fp:
        serial_manager.queue_for_sending(line)
    return "Longtest queued."
    


@route('/css/:path#.+#')
def static_css_handler(path):
    return static_file(path, root=os.path.join(current_dir, 'css'))
    
@route('/js/:path#.+#')
def static_css_handler(path):
    return static_file(path, root=os.path.join(current_dir, 'js'))
    
@route('/img/:path#.+#')
def static_css_handler(path):
    return static_file(path, root=os.path.join(current_dir, 'img'))

@route('/')
@route('/index.html')
@route('/app.html')
def default_handler():
    return static_file('app.html', root=current_dir)
    

@route('/serial/:connect')
def serial_handler(connect):
    if connect == '1' and not serial_manager.is_connected():
        try:
            global arduino_port, baudrate
            serial_manager.connect(ARDUINO_PORT, BAUDRATE)
            ret = "Serial connected to %s:%d." % (ARDUINO_PORT, BAUDRATE)  + '<br>'
            time.sleep(0.5) # allow some time to receive a prompt/welcome
            return serial_manager.get_responses('<br>')
        except serial.SerialException:
            print "Failed to connect to serial."    
            return ""          
    elif connect == '0' and serial_manager.is_connected():
        if serial_manager.close(): return "1"
        else: return ""  
    elif connect == "2":
        if serial_manager.is_connected(): return "1"
        else: return ""
    else:
        print 'got neither: ' + connect            
        return ""
        

@route('/gcode/:gcode_line')
def gcode_handler(gcode_line):
    if serial_manager.is_connected():    
        print gcode_line
        serial_manager.queue_for_sending(gcode_line + '\n')
        return "Queued for sending."
    else:
        return ""

@route('/gcode', method='POST')
def gcode_handler_submit():
    gcode_program = request.forms.get('gcode_program')
    if gcode_program and serial_manager.is_connected():
        print gcode_program
        lines = gcode_program.split('\n')
        for line in lines:
            serial_manager.queue_for_sending(line + '\n')
        return "Queued for sending."
    else:
        return ""

@route('/queue_pct_done')
def queue_pct_done_handler():
    return serial_manager.get_queue_percentage_done()


debug(True)
run_with_callback(host='localhost', port=8080)