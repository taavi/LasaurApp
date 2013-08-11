"""
File Reader Module
"""


__author__ = 'Stefan Hechenberger <stefan@nortd.com>'

import shared


def read_svg(svg_string, target_size, tolerance, forced_dpi=None, optimize=True):
    if shared.args.optimize:
        from .svg_reader_c import SVGReader
        from .path_optimizers_c import optimize_all
    else:
        from .svg_reader import SVGReader
        from .path_optimizers import optimize_all
        
    svgReader = SVGReader(tolerance, target_size)
    parse_results = svgReader.parse(svg_string, forced_dpi)
    if optimize:
        optimize_all(parse_results['boundarys'], tolerance)
    # {'boundarys':b, 'dpi':d, 'lasertags':l}
    return parse_results


def read_dxf(dxf_string, tolerance, optimize=True):
    if shared.args.optimize:
        from .dxf_reader_c import DXFReader
        from .path_optimizers_c import optimize_all
    else:
        from .dxf_reader import DXFReader
        from .path_optimizers import optimize_all

    dxfReader = DXFReader(tolerance)
    parse_results = dxfReader.parse(dxf_string)
    if optimize:
        optimize_all(parse_results['boundarys'], tolerance)
    # # flip y-axis
    # for color,paths in parse_results['boundarys'].items():
    # 	for path in paths:
    # 		for vertex in path:
    # 			vertex[1] = 610-vertex[1]
    return parse_results