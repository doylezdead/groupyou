from groupyou.jobs.reaction import Reaction


class PingPong(Reaction):

    def __init__(self):
        self.message = 'bad'

    def react(self, user_name, text, attachments):
        if text == 'ping':
            self.message = 'asdf'
            return True
        return False

    def run(self, chat):
        chat.add_text(self.message)
        chat.flush()
        return
