


# def f(d):
# 	d = [10]

# a = [5]
# f(a)
# print a


# from svg_reader import SVGReader

# reader = SVGReader(0.08, [1220,610])
# boundarys = reader.parse(open("/home/noema/git/LasaurApp/other/test_svgs/lasersaur-v0.4.02-cutfiles-formulor.svg").read())
# boundarys = reader.parse(open("/home/noema/git/LasaurApp/other/test_svgs/elephant_red.svg").read())
# boundarys = reader.parse(open("/home/noema/git/LasaurApp/other/test_svgs/Steven and Chris Picture Frame - with ERROR.svg").read())
# print boundarys


from filereaders import read_dxf

dxfstring = open("/home/noema/git/LasaurApp/other/test_dxfs/leg.dxf").read()
boundarys = read_dxf(dxfstring, 0.08)
print boundarys