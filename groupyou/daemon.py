import bottle
import json
import logging
import argparse
from groupyou.jobscheduler import JobScheduler
from groupyou.communication import Chat

root_logger = logging.getLogger(name="root")
root_logger.setLevel(logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument('bid')
args = parser.parse_args()
bot_id = args.bid

chat = Chat(bot_id)
job_scheduler = JobScheduler(chat)
quit()


@bottle.route('/groupyou', method='POST')
def ping_event():
    raw_ping = bottle.request.body.readline()
    ping = json.loads(raw_ping.decode('utf-8'))
    job_scheduler.chat_hit(ping)

root_logger.info('Ctrl-C to gracefully shut down the bot')
bottle.run(host='0.0.0.0', port=60606)
