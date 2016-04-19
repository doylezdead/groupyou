from groupyou.jobs.reaction import Reaction


class Echo(Reaction):
    help = '"echo asdf" will echo back "asdf"'

    def __init__(self):
        self.message = 'bad'

    def react(self, user_name, text, attachments):
        if text.startswith('echo '):
            self.message = text[5:]
            return True
        return False

    def run(self, chat):
        chat.add_text(self.message)
        chat.flush()
        return
