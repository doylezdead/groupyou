from groupyou.jobs.reaction import Reaction


class Chprefix(Reaction):
    help = '"echo asdf" will echo back "asdf"'

    def __init__(self):
        self.message = 'bad'

    def react(self, user_name, text, attachments):
        if text.startswith('chprefix '):
            self.message = text[9:]
            return True
        return False

    def run(self, chat, scheduler=None):
        scheduler.prefix = self.message
        chat.add_text("prefix changed to " + self.message)
        chat.flush()
        return
