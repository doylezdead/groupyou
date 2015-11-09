from groupyou.jobs.reaction import Reaction


class PingPong(Reaction):
    help = 'Responds with "ping" upon a "pong"'

    def __init__(self):
        self.message = 'bad'

    def react(self, user_name, text, attachments):
        if text == 'ping':
            self.message = 'pong'
            return True
        return False

    def run(self, chat):
        chat.add_text(self.message)
        chat.flush()
        return
