from groupyou.jobs.reaction import Reaction
from groupyou.jobs.date import Date
import groupyou.jobs.reactions
import groupyou.jobs.dates

import threading

import time

class JobScheduler(object):
    def __init__(self, chat):
        self.chat = chat
        self.prefix = '/bot'

        self.reactionlist = Reaction.__subclasses__()
        self.datelist = Date.__subclasses__()

    def chat_hit(self, ping_dict):
        if not ping_dict.get('text', '').startswith(self.prefix):
            return
        else:
            ping_dict['text'] = ping_dict['text'][(len(self.prefix)+1):]
        for job in self.reactionlist:
            if job.react(job, ping_dict.get('name', ''), ping_dict.get('text', ''), ping_dict.get('attachments', [])):
                retvals = job.run(job, self.chat)
                if retvals is not None:
                    self.__dict__.update(retvals)

    def minute_check(self):
        pass
