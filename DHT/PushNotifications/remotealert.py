#From https://github.com/soynerdito/RaspberryPiTalk/blob/master/in_out_sample/remotealert.py
import json
import urllib2

class RemoteAlert:
    def send(self, device_id, message ):
        data = { 'message' : message }
        url = 'http://remote-alert.herokuapp.com/post/' + device_id
        req = urllib2.Request( url )
        req.add_header('Content-Type', 'application/json')
        urllib2.urlopen(req, json.dumps(data))
        return 'OK'
