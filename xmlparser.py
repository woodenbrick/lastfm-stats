#!/usr/bin/env python
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class Lastfm_Xml_Handler(ContentHandler):
    
    def __init__(self):
        self.inTitle = 0
        self.mapping = {}
 
  def startElement(self, name, attributes):
    if name == "book":
      self.buffer = ""
      self.isbn = attributes["isbn"]
    elif name == "title":
      self.inTitle = 1
 
  def characters(self, data):
    if self.inTitle:
      self.buffer += data
 
  def endElement(self, name):
    if name == "title":
      self.inTitle = 0
      self.mapping[self.isbn] = self.buffer

Extracting the information we're looking for is now trivial. If the code above is in bookhandler.py and our sample document is in books.xml, we could do this in an interactive session:

>>> import xml.sax
>>> import bookhandler
>>> import pprint
>>> 
>>> parser = xml.sax.make_parser(  )
>>> handler = bookhandler.BookHandler(  )
>>> parser.setContentHandler(handler)
>>> parser.parse("books.xml")
>>> pprint.pprint(handler.mapping)
{u'1-56592-051-1': u'Making TeX Work',
 u'1-56592-724-9': u'The Cathedral & the Bazaar'}
