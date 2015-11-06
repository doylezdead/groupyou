from groupyou.job import Job
from groupyou.jobs.reaction import Reaction
from groupyou.jobs.date import Date

import os

class JobScheduler(object):
    def __init__(self, chat):
        self.chat = chat
        self.reactionlist = []
        self.datelist = []

        dir = os.path.dirname(os.path.realpath(__file__))
        datedir = dir + "/jobs/dates"
        reactiondir = dir + "/jobs/reactions"
        reactionlist = os.listdir(reactiondir)
        datelist = os.listdir(datedir)
        reactionlist.remove('__init__.py')
        datelist.remove('__init__.py')

        for x in range(0, len(reactionlist)):
            item = reactionlist[x][0:-3]


            new_job = job_class()
            self.reactionlist.append(new_job)





        new_job = job_class()
        self.datelist.append(new_job)

    def chat_hit(self, ping_dict):
        for job in self.reactionlist:
            if job.react(ping_dict['name'], ping_dict['text'], ping_dict['attachments']):
                job.run(self.chat)

    def minute_check(self):
        pass
