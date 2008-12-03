#!/usr/bin/env python
import xml.etree.ElementTree as ET
import os
path = os.path.dirname(os.path.realpath(__file__))
xml = path + '/xml/user.getrecenttracks.xml'
doc = ET.parse(xml)
iter = doc.getiterator()
wanted_subs = {'date' : 'uts'}
wanted = ['artist', 'name', 'date']

collected = []
current = {}
for child in iter:
    if child.tag in wanted:
        if child.tag in wanted_subs:
            current[child.tag] = child.attrib['uts']
        else:
            current[child.tag] = child.text
    if len(wanted) == len(current):
        collected.append(current)
        current = {}
print collected
#tree = doc.getiterator(wanted)
#for element in tree:
#    print element.text
