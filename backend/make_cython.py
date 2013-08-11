#!/usr/bin/python

import os, sys, subprocess, shutil
import argparse


argparser = argparse.ArgumentParser(description='Compile Cython code.', prog='make_cython')
argparser.add_argument('module', metavar='module', nargs='?', default=False,
                    help='module to compile')
argparser.add_argument('-u', '--undo', dest='undo', action='store_true',
                       default=False, help='undo cython module')
argparser.add_argument('--pyx_only', dest='pyx_only', action='store_true',
                       default=False, help='only .pyx files instead of all .py files')
argparser.add_argument('-b', '--beaglebone', dest='beaglebone', action='store_true',
                       default=False, help='compile with beaglebone optimizations')
args = argparser.parse_args()

ret = 0

if args.module:
    OBJECTS  = [args.module]
else:
    OBJECTS  = [
        "filereaders/dxf_reader",
        "filereaders/kdtree",
        "filereaders/path_optimizers",
        "filereaders/svg_attribute_reader",
        "filereaders/svg_path_reader",
        "filereaders/svg_reader",
        "filereaders/svg_tag_reader",
        "filereaders/utilities",
        "filereaders/webcolors"
    ]

if args.undo:
    for obj in OBJECTS:
        # del .so
        f = '%s.so' % (obj)
        if os.path.isfile(f):
            os.remove(f)

        # del _c.so
        f = '%s_c.so' % (obj)
        if os.path.isfile(f):
            os.remove(f)

        # del .pyc, for good measure
        f = '%s.pyc' % (obj)
        if os.path.isfile(f):
            os.remove(f)

else:
    for obj in OBJECTS:
        if not args.pyx_only:
            # rename first
            f_src = '%s.py' % (obj)
            f_dst = '%s_c.py' % (obj)
            if os.path.isfile(f_src):
                shutil.move(f_src, f_dst)
            # .py to .c
            command = 'cython %s_c.py' % obj
            ret += subprocess.call(command, shell=True)
            # rename back
            f_src = '%s_c.py' % (obj)
            f_dst = '%s.py' % (obj)
            if os.path.isfile(f_src):
                shutil.move(f_src, f_dst)
        else:
            # rename first
            f_src = '%s.pyx' % (obj)
            f_dst = '%s_c.pyx' % (obj)
            if os.path.isfile(f_src):
                shutil.move(f_src, f_dst)
            # .pyx to .c
            command = 'cython %s.pyx' % obj
            ret += subprocess.call(command, shell=True)
            # rename back
            f_src = '%s_c.pyx' % (obj)
            f_dst = '%s.pyx' % (obj)
            if os.path.isfile(f_src):
                shutil.move(f_src, f_dst)

        # .c to .o
        if args.beaglebone:
            # command = 'gcc -c -fPIC -O3 -mcpu=cortex-a8 -mfpu=neon -ftree-vectorize -ffast-math -fsingle-precision-constant -I/usr/include/python2.7/ %s_c.c -o %s_c.o' % (obj, obj)
            command = 'gcc -c -fPIC -O3 -march=arm -I/usr/include/python2.7/ %s_c.c -o %s_c.o' % (obj, obj)
            # see http://linuxreviews.org/man/gcc/
            # see http://pandorawiki.org/Floating_Point_Optimization
        else:
            # 'gcc -shared -pthread -fPIC -fwrapv -O3 -Wall -fno-strict-aliasing -I/usr/include/python2.5 -o %s.so %s.c'
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




print "done!"
