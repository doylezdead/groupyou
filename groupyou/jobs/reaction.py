from groupyou.job import Job


class Reaction(Job):

    def react(self, user_name, text, attachments):
        raise Exception("you need to override react function")
