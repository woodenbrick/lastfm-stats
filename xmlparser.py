#!/usr/bin/env python
import xml.etree.ElementTree as ET

xml = './xml/user.getrecenttracks.xml'
doc = ET.ElementTree(xml)
iter = doc.getiterator()
print iter

#tree = doc.getiterator(wanted)
#for element in tree:
#    print element.text
