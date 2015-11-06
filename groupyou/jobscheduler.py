from groupyou.jobs.reaction import Reaction
from groupyou.jobs.date import Date
import groupyou.jobs.reactions
import groupyou.jobs.dates



class JobScheduler(object):
    def __init__(self, chat):
        self.chat = chat

        self.reactionlist = Reaction.__subclasses__()
        self.datelist = Date.__subclasses__()

    def chat_hit(self, ping_dict):
        for job in self.reactionlist:
            if job.react(None, ping_dict.get('name', ''), ping_dict.get('text', ''), ping_dict.get('attachments', [])):
                job.run(None, self.chat)

    def minute_check(self):
        pass
