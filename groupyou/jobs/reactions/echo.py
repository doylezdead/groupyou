from groupyou.jobs.reaction import Reaction


class Echo(Reaction):

    def __init__(self):
        self.message = 'bad'

    def react(self, user_name, text, attachments):
        if text.startswith('echo '):
            self.message = text[4:]
            return True
        return False

    def run(self, chat):
        chat.add_text(self.message)
        chat.flush()
        return
