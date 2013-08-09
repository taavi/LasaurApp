


# def f(d):
#   d = [10]

# a = [5]
# f(a)
# print a


# from svg_reader import SVGReader

# reader = SVGReader(0.08, [1220,610])
# boundarys = reader.parse(open("/home/noema/git/LasaurApp/other/test_svgs/lasersaur-v0.4.02-cutfiles-formulor.svg").read())
# boundarys = reader.parse(open("/home/noema/git/LasaurApp/other/test_svgs/elephant_red.svg").read())
# boundarys = reader.parse(open("/home/noema/git/LasaurApp/other/test_svgs/Steven and Chris Picture Frame - with ERROR.svg").read())
# print boundarys

import os
import profile
import timeit
import pstats
import argparse

from filereaders import read_svg

### Setup Argument Parser
argparser = argparse.ArgumentParser(description='Run LasaurApp.', prog='lasaurapp')
argparser.add_argument('svg_file', metavar='svg_file', nargs='?', default=False,
                       help='svg file to parse')
argparser.add_argument('-p', '--profile', dest='profile', action='store_true',
                    default=False, help='run with profiling')  
argparser.add_argument('-t', '--timeit', dest='timeit', action='store_true',
                    default=False, help='run with timing')                                       
args = argparser.parse_args()


def main():
    print "running"
    # svgstring = open("/home/noema/git/LasaurApp/other/test_svgs/full-bed.svg").read()
    svgstring = open("/home/noema/git/LasaurApp/other/test_svgs/rocket_full.svg").read()
    # svgstring = open("/home/noema/git/LasaurApp/other/test_svgs/Steven and Chris Picture Frame - with ERROR.svg").read()
    boundarys = read_svg(svgstring, [1220,610], 0.08)

def yo():
    print 'yo'


if args.profile:
    profile.run("main()", 'profile.tmp')
    p = pstats.Stats('profile.tmp')
    p.sort_stats('cumulative').print_stats(30)
    os.remove('profile.tmp')
elif args.timeit:
    t = timeit.Timer("main()", "from __main__ import main")
    print t.timeit(1)
    # print t.timeit(3)
else:
    main()