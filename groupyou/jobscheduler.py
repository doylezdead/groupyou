from groupyou.jobs.reaction import Reaction
from groupyou.jobs.date import Date
import groupyou.jobs.reactions
import groupyou.jobs.dates



class JobScheduler(object):
    def __init__(self, chat):
        self.chat = chat
        self.reactionlist = []
        self.datelist = []

        reactlist = Reaction.__subclasses__()
        datelist = Date.__subclasses__()

        for reaction in reactlist:
            new_job = reaction
            reactlist.append(new_job)

        for date in datelist:
            new_job = date
            datelist.append(new_job)



    def chat_hit(self, ping_dict):
        for job in self.reactionlist:
            if job.react(ping_dict['name'], ping_dict['text'], ping_dict['attachments']):
                job.run(self.chat)

    def minute_check(self):
        pass
