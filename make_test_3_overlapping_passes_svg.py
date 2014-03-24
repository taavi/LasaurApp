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
  {g}
  <text y="630">{lasertags}</text>
</svg>
"""

G = """<g>{paths}</g>"""

PATH = """<path d="m {x},{y} {dx},{dy}" style="stroke:{colour};stroke-width:1" />"""


def normalize(img):
    maximum = float(max(max(l) for l in img))
    return [[x / maximum for x in row] for row in img]


class Quantizer(object):
    def __init__(self, levels):
        self.levels = levels

    def quantize(self, img):
        return [[int(x*self.levels) for x in row] for row in img]

    def colour(self, v):
        return ['#000000', '#3f0000', '7f0000'][v]

    def bitslice(self, img):
        slices = []
        for n in range(math.ceil(math.log(self.levels, 2))):
            mask = 1 << n
            slices.append(
                [
                    [x & mask for x in row]
                    for row in img
                ]
            )
        return reversed(slices)

    def lasertags(self):
        return [
            "=pass{n}:1200mm/min:{twotothen}%:{colour}=".format(
                n=(n + 1), twotothen=2**n, colour=self.colour(n))
            for n in reversed(range(math.ceil(math.log(self.levels, 2))))
        ]


def compress(img):
    return [
        [(x, len(list(l))) for x, l in itertools.groupby(row)]
        for row in img]


img = [[abs(x * y) for x in range(-20, 20)] for y in range(-20, 20)]
img = normalize(img)
quantizer = Quantizer(8)
img = quantizer.quantize(img)
img = quantizer.bitslice(img)

paths = []

for c, layer in enumerate(img):
for y, row in enumerate(compress(img)):
    x = 0
    for px, length in row:
        if px != quantizer.levels - 1:
            paths.append(PATH.format(x=x, y=y, dx=length, dy=0, colour=quantizer.colour(px)))
        x += length

print TEMPLATE.format(paths='\n'.join(paths), lasertags=quantizer.lasertags())
