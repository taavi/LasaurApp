import string 

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def getTag(node):
	"""Get tag name without possible namespace prefix."""
	tag = node.tag
	return tag[tag.rfind('}')+1:]


f = open("/home/noema/git/LasaurApp/other/test_svgs/lasersaur-dino.svg")
root = ET.fromstring(f.read())
# print root.tag
print getTag(root)
print root.attrib
print '----'
print root.keys()

