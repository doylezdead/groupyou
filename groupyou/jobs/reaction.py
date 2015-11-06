from groupyou.job import Job


class Reaction(Job):
    def __init__(self):
        super(Job, self).__init__()

    def react(self, user_name, text, attachments):
        return False
