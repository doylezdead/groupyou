from groupyou.jobs.reaction import Reaction
import groupyou.jobs.reactions


class Help(Reaction):

    def __init__(self):
        self.help = 'Display this help message.'
        self.message = 'bad'

    def react(self, user_name, text, attachments):
        if text == 'help':
            self.message += 'Available Commands:\n'
            reactionlist = Reaction.__subclasses__()
            for job in reactionlist:
                self.message += job.__name__
                self.message += ': '
                self.message += job.help
                self.message += '\n'
            return True
        return False

    def run(self, chat):
        chat.add_text(self.message)
        chat.flush()
        return
