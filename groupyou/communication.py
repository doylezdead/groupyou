from http import client as htcli
import json
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
            self.conn = htcli.HTTPConnection("https://api.groupme.com")
        except Exception as e:
            log.error("Could not connect to groupme api")

    def flush(self):
        raw_send = json.dumps(self.tempdict).encode('utf-8')
        self.conn.request('POST', '/v3/bots/post', body=raw_send, headers={'Content-Type': 'application/json'})
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
