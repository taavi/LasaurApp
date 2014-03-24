import itertools


TEMPLATE = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   version="1.1"
   width="1220"
   height="610"
   id="svg2">
  <g id="layer1">
    {paths}
  </g>
  <text y="630">{lasertags}</text>
</svg>
"""

PATH = """<path d="m {x},{y} {dx},{dy}" style="stroke:{colour};stroke-width:1" />"""


def normalize(img):
    maximum = float(max(max(l) for l in img))
    return [[x / maximum for x in row] for row in img]


class Quantizer(object):
    def __init__(self, levels):
        self.levels = levels

    def quantize(self, img):
        levels = float(self.levels)
        return [[int(x*levels)/levels for x in row] for row in img]

    def colour(self, v):
        v = min(255, int(256 * v))
        return "#%02x%02x%02x" % (0, 0, v)

    def lasertags(self):
        colours = [[x/float(self.levels) for x in range(self.levels)]]
        colours = reversed(self.quantize(colours)[0])
        tags = ' '.join(
            "=pass{i}:1200mm/min:{i}%:{colour}=".format(i=i, colour=self.colour(colour))
            for i, colour in enumerate(colours, start=1)
        )
        return tags


def compress(img):
    return [
        [(x, len(list(l))) for x, l in itertools.groupby(row)]
        for row in img]


img = [[abs(x * y) for x in range(-20, 20)] for y in range(-20, 20)]
img = normalize(img)
quantizer = Quantizer(8)
img = quantizer.quantize(img)

paths = []

for y, row in enumerate(compress(img)):
    x = 0
    for px, length in row:
        paths.append(PATH.format(x=x, y=y, dx=length, dy=0, colour=quantizer.colour(px)))
        x += length

print TEMPLATE.format(paths='\n'.join(paths), lasertags=quantizer.lasertags())
