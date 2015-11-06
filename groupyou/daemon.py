import bottle
import json
import signal
import sys
import logging

root_logger = logging.getLogger(name="root")
root_logger.setLevel(logging.DEBUG)



@bottle.route('/groupyou', method='POST')
def handle_ping():
    raw_ping = bottle.request.body.readline()
    ping = json.loads(raw_ping.decode('utf-8'))



root_logger.info('Ctrl-C to gracefully shut down the bot')
bottle.run(host='0.0.0.0', port=60606)
