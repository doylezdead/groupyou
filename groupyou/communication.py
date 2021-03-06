from http import client as htcli
import json
import time
import logging

log = logging.getLogger()


class Chat(object):
    def __init__(self, bid):
        self.bot_id = bid
        self.tempdict = {
            "bot_id": self.bot_id,
            "attachments": []
        }
        try:
            self.conn = htcli.HTTPSConnection("api.groupme.com")
            # self.conn.set_debuglevel(1)
        except Exception as e:
            print("Could not connect to groupme api")

    def flush(self):
        raw_send = json.dumps(self.tempdict)
        time.sleep(.5)
        self.conn.request('POST', '/v3/bots/post', body=raw_send, headers={'Content-Type': 'application/json'})
        try:
            self.conn.getresponse().read()
        except htcli.BadStatusLine as e:
            pass
        self.tempdict = {
            "bot_id": self.bot_id,
            "attachments": []
        }

    def add_text(self, text):
        self.tempdict['text'] = text

    def add_image(self, url):
        self.tempdict['attachments'].append({
            'type': 'image',
            'url': url
        })

    def add_location(self, lat, lng, name=""):
        self.tempdict['attachments'].append({
            'type': 'location',
            'lat': lat,
            'long': lng,
            'name': name
        })
