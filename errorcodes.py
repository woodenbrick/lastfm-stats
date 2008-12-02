#!/usr/bin/env python

class Lastfm_Api_Error():
    def __init__(self, errnum):
        self.all_error_messages = {
                 2 : "Invalid service -This service does not exist",
                 3 : "Invalid Method - No method with that name in this package",
                 4 : "Authentication Failed - You do not have permissions to access the service",
                 5 : "Invalid format - This service doesn't exist in that format",
                 6 : "Invalid parameters - Your request is missing a required parameter",
                 7 : "Invalid resource specified",
                 8 : "There was an error granting the request token. Please try again later",
                 9 : "Invalid session key - Please re-authenticate",
                 10 : "Invalid API key - You must be granted a valid key by last.fm",
                 11 : "Service Offline - This service is temporarily offline. Try again later.",
                 12 : "Subscribers Only - This service is only available to paid last.fm subscribers"
            }
        self.errnum = errnum
        self.error_message = self.all_error_messages[self.errnum]
        print self.error_message
    
    
if __name__ == '__main__':
    num = 4
    if num is not 1:
        Lastfm_Api_Error(num)