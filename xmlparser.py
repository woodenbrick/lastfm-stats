#!/usr/bin/env python
import xml.etree.ElementTree as ET
import os

class XML_Parser(object):
    def __init__(self, xml_doc, wanted_data, wanted_attrib = None):
        """Parses an xml document.  wanted_data is all the tags that you wish to parse,
        including the tags of attributes.  Send a dictionary of wanted_attributes as well
        if they are required.
        eg. XML_Parser(doc.xml, wanted_data = ['artist', 'name', 'date'],
        wanted_attrib = { 'date' : 'uts' }
        """
        
        self.tree = ET.parse(xml_doc)
        self.iter = self.tree.getiterator()
        self.wanted_attrib = wanted_attrib
        self.wanted = wanted_data
        self.collected = []
        
    def add_attrib(self, tag, attrib):
        """Adds a new attribute tag to search for"""
        self.add_tag(tag)
        self.wanted_attrib[tag] = attrib
        
    def add_tag(self, tag):
        """Adds a new tag to search for"""
        self.wanted.append(tag)
        
    def run_iterator(self):
        """Runs through the document and returns all tags and attributes as a list"""
        current = {}
        for child in self.iter:
            if child.tag in self.wanted:
                if child.tag in self.wanted_attrib:
                    current[child.tag] = child.attrib[self.wanted_attrib[child.tag]]
                else:
                    current[child.tag] = child.text
            if len(self.wanted) == len(current):
                self.collected.append(current)
                current = {}
        return self.collected

if __name__ == '__main__':
    wanted_attrib = {'date' : 'uts'}
    wanted = ['artist', 'name', 'date']
    path = os.path.dirname(os.path.realpath(__file__))
    xml_doc = path + '/xml/user.getrecenttracks.xml'
    parser = XML_Parser(xml_doc, wanted, wanted_attrib)
    parser.run_iterator()
    print parser.collected