import webbrowser
import md5
import urllib
import urllib2

#currently implemented in the set_method function:
#user.getrecenttracks
#this may be reimplemented as a class if it becomes too unwieldy

class Lastfm_Stats:
    def __init__(self):
        self.secret = '6146d36f59da8720cd5f3dd2c8422da0'
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
        req = urllib2.Request(url=self.base_url, data=values)
        try:
            url_handle = urllib2.urlopen(req)
            for line in url_handle.readlines():
                print line
        except urllib2.URLError:
            response = 'Connection Refused, please try again'
    
    def returnError(errorid):
        errors = {
             8 : "There was an error granting the request token. Please try again later",
             2 : "Invalid service -This service does not exist",
             3 : "Invalid Method - No method with that name in this package",
             4 : "Authentication Failed - You do not have permissions to access the service",
             5 : "Invalid format - This service doesn't exist in that format",
             6 : "Invalid parameters - Your request is missing a required parameter",
             7 : "Invalid resource specified",
             9 : "Invalid session key - Please re-authenticate",
             10 : "Invalid API key - You must be granted a valid key by last.fm",
             11 : "Service Offline - This service is temporarily offline. Try again later.",
             12 : "Subscribers Only - This service is only available to paid last.fm subscribers"
        }
        return errors[errorid]
    
if __name__ == '__main__':
    lastfm = Lastfm_Stats()
    lastfm.set_user('woodenbrick')
    lastfm.set_method('user.getrecenttracks')
    url_values = lastfm.encode_url_values()
    request = lastfm.request_data(url_values)
