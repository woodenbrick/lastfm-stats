import webbrowser
import md5
import urllib
import urllib2

#currently implemented in the set_method function:
#user.getrecenttracks
#this may be reimplemented as a class if it becomes too unwieldy

class Lastfm_Stats:
    def __init__(self):
        self.get_values = {'api_key' : '2d21a4ab6f049a413eb27dbf9af10579'}
        self.base_url = "http://ws.audioscrobbler.com/2.0/?"
        self.xml_dir = "./xml/"
        
    def set_user(self, user):
        self.get_values['user'] = user
        
    def set_method(self, method, limit=10):
        self.get_values['method'] = method
        #self.get_values['limit'] = limit
        self.filename = self.xml_dir + method + '.xml'

    def encode_url_values(self):
        values = urllib.urlencode(self.get_values)
        return values
    
    def request_data(self, values):
        req = urllib.urlretrieve(url = self.base_url + values, filename = self.filename)
    
  
if __name__ == '__main__':
    lastfm = Lastfm_Stats()
    lastfm.set_user('woodenbrick')
    lastfm.set_method('user.getrecenttracks')
    url_values = lastfm.encode_url_values()
    request = lastfm.request_data(url_values)
