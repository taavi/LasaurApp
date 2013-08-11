
import os, sys, subprocess, shutil
import argparse


argparser = argparse.ArgumentParser(description='Compile Cython code.', prog='make_cython')
argparser.add_argument('-u', '--undo', dest='undo', action='store_true',
                       default=False, help='undo cython module')
argparser.add_argument('--pyx_only', dest='pyx_only', action='store_true',
                       default=False, help='only .pyx files instead of all .py files')
argparser.add_argument('-b', '--beaglebone', dest='beaglebone', action='store_true',
                       default=False, help='compile with beaglebone optimizations')
args = argparser.parse_args()

ret = 0

OBJECTS  = [
    "backend/filereaders/dxf_reader",
    "backend/filereaders/kdtree",
    "backend/filereaders/path_optimizers",
    "backend/filereaders/svg_attribute_reader",
    "backend/filereaders/svg_path_reader",
    "backend/filereaders/svg_reader",
    "backend/filereaders/svg_tag_reader",
    "backend/filereaders/utilities",
    "backend/filereaders/webcolors"
]

if args.undo:
    for obj in OBJECTS:
        # del .so
        f = '%s_c.so' % (obj)
        if os.path.isfile(f):
            os.remove(f)

        # # restore any possible python module
        # f_src = '%s_.py' % (obj)
        # f_dst = '%s.py' % (obj)
        # if os.path.isfile(f_src):
        #     shutil.move(f_src, f_dst)


else:
    for obj in OBJECTS:
        if not args.pyx_only:
            # .py to .c
            command = 'cython %s.py -o %s_c.c' % (obj, obj)
            ret += subprocess.call(command, shell=True)
        else:
            # .pyx to .c
            command = 'cython %s_c.pyx' % obj
            ret += subprocess.call(command, shell=True)

        # .c to .o
        if args.beaglebone:
            command = 'gcc -c -fPIC -O3 -mcpu=cortex-a8 -mfpu=neon -ftree-vectorize -ffast-math -fsingle-precision-constant -I/usr/include/python2.7/ %s_c.c -o %s_c.o' % (obj, obj)
            # see http://linuxreviews.org/man/gcc/
            # see http://pandorawiki.org/Floating_Point_Optimization
        else:
            command = 'gcc -c -fPIC -O3 -I/usr/include/python2.7/ %s_c.c -o %s_c.o' % (obj, obj)
        ret += subprocess.call(command, shell=True)

        # .o to .so
        command = 'gcc -shared %s_c.o -o %s_c.so' % (obj, obj)
        ret += subprocess.call(command, shell=True)

        # del .c
        f = '%s_c.c' % (obj)
        if os.path.isfile(f):
            os.remove(f)

        # del .o
        f = '%s_c.o' % (obj)
        if os.path.isfile(f):
            os.remove(f)

        # # move any possible python module
        # f_src = '%s.py' % (obj)
        # f_dst = '%s_.py' % (obj)
        # if os.path.isfile(f_src):
        #     shutil.move(f_src, f_dst)

        # # del .pyc
        # f = '%s.pyc' % (obj)
        # if os.path.isfile(f):
        #     os.remove(f)

print "done!"
