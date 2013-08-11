
import os, sys, subprocess, shutil
import argparse


argparser = argparse.ArgumentParser(description='Compile Cython code.', prog='makeython')
argparser.add_argument('-u', '--undo', dest='undo', action='store_true',
                       default=False, help='undo cython module')
<<<<<<< HEAD
<<<<<<< HEAD
argparser.add_argument('-d', '--deactivate', dest='deactivate', action='store_true',
                       default=False, help='deactivate cython modules (rename)')
argparser.add_argument('-r', '--reactivate', dest='reactivate', action='store_true',
                       default=False, help='reactivate cython modules (undo rename)')
argparser.add_argument('--pyx_only', dest='pyx_only', action='store_true',
                       default=False, help='only .pyx files instead of all .py files')
=======
argparser.add_argument('-c', '--compile_all', dest='compile_all', action='store_true',
                       default=False, help='compile all .py files')
>>>>>>> parent of 1d676a1... working on conditional c-module import
=======
argparser.add_argument('-c', '--compile_all', dest='compile_all', action='store_true',
                       default=False, help='compile all .py files')
>>>>>>> parent of 1d676a1... working on conditional c-module import
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
        f = '%s.so' % (obj)
        if os.path.isfile(f):
            os.remove(f)

<<<<<<< HEAD
<<<<<<< HEAD
        # del _.so
        f = '%s_.so' % (obj)
        if os.path.isfile(f):
            os.remove(f)
=======
        # restore any possible python module
        f_src = '%s_.py' % (obj)
        f_dst = '%s.py' % (obj)
        if os.path.isfile(f_src):
            shutil.move(f_src, f_dst)
>>>>>>> parent of 1d676a1... working on conditional c-module import

elif args.deactivate:
    for obj in OBJECTS:
        # move any possible python module
        f_src = '%s.so' % (obj)
        f_dst = '%s_.so' % (obj)
=======
        # restore any possible python module
        f_src = '%s_.py' % (obj)
        f_dst = '%s.py' % (obj)
>>>>>>> parent of 1d676a1... working on conditional c-module import
        if os.path.isfile(f_src):
            shutil.move(f_src, f_dst)

elif args.reactivate:
    for obj in OBJECTS:
        # move any possible python module
        f_src = '%s_.so' % (obj)
        f_dst = '%s.so' % (obj)
        if os.path.isfile(f_src):
            shutil.move(f_src, f_dst)

else:
    for obj in OBJECTS:
        if args.compile_all:
            # .py to .c
<<<<<<< HEAD
<<<<<<< HEAD
            command = 'cython %s.py -o %s.c' % (obj, obj)
=======
            command = 'cython %s.py' % obj
>>>>>>> parent of 1d676a1... working on conditional c-module import
=======
            command = 'cython %s.py' % obj
>>>>>>> parent of 1d676a1... working on conditional c-module import
            ret += subprocess.call(command, shell=True)
        else:
            # .pyx to .c
            command = 'cython %s.pyx' % obj
            ret += subprocess.call(command, shell=True)

        # .c to .o
        if args.beaglebone:
<<<<<<< HEAD
<<<<<<< HEAD
=======
            # command = 'gcc -c -fPIC -O3 -march=armv5 -I/usr/include/python2.7/ %s.c -o %s.o' % (obj, obj)
>>>>>>> parent of 1d676a1... working on conditional c-module import
=======
            # command = 'gcc -c -fPIC -O3 -march=armv5 -I/usr/include/python2.7/ %s.c -o %s.o' % (obj, obj)
>>>>>>> parent of 1d676a1... working on conditional c-module import
            command = 'gcc -c -fPIC -O3 -mcpu=cortex-a8 -mfpu=neon -ftree-vectorize -ffast-math -fsingle-precision-constant -I/usr/include/python2.7/ %s.c -o %s.o' % (obj, obj)
            # see http://linuxreviews.org/man/gcc/
            # see http://pandorawiki.org/Floating_Point_Optimization
        else:
<<<<<<< HEAD
<<<<<<< HEAD
            # 'gcc -shared -pthread -fPIC -fwrapv -O3 -Wall -fno-strict-aliasing -I/usr/include/python2.5 -o %s.so %s.c'
=======
>>>>>>> parent of 1d676a1... working on conditional c-module import
=======
>>>>>>> parent of 1d676a1... working on conditional c-module import
            command = 'gcc -c -fPIC -O3 -I/usr/include/python2.7/ %s.c -o %s.o' % (obj, obj)
        ret += subprocess.call(command, shell=True)

        # .o to .so
        command = 'gcc -shared %s.o -o %s.so' % (obj, obj)
        ret += subprocess.call(command, shell=True)

        # del .c
        f = '%s.c' % (obj)
        if os.path.isfile(f):
            os.remove(f)

        # del .o
        f = '%s.o' % (obj)
        if os.path.isfile(f):
            os.remove(f)

<<<<<<< HEAD
<<<<<<< HEAD


=======
        # move any possible python module
        f_src = '%s.py' % (obj)
        f_dst = '%s_.py' % (obj)
        if os.path.isfile(f_src):
            shutil.move(f_src, f_dst)

=======
        # move any possible python module
        f_src = '%s.py' % (obj)
        f_dst = '%s_.py' % (obj)
        if os.path.isfile(f_src):
            shutil.move(f_src, f_dst)

>>>>>>> parent of 1d676a1... working on conditional c-module import
        # del .pyc
        f = '%s.pyc' % (obj)
        if os.path.isfile(f):
            os.remove(f)
<<<<<<< HEAD
>>>>>>> parent of 1d676a1... working on conditional c-module import
=======
>>>>>>> parent of 1d676a1... working on conditional c-module import

print "done!"
