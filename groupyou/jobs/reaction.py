from groupyou.job import Job


class Reaction(Job):
    help = 'No help available'
    message = ''

    def react(self, user_name, text, attachments):
        raise Exception("you need to override react function")
