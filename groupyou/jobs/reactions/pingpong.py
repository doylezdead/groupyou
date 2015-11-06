from groupyou.jobs.reaction import Reaction


class PingPong(Reaction):

    def react(self, user_name, text, attachments):
        if text == 'ping':
            return True
        return False

    def run(self, chat):
        chat.add_text("pong")
        chat.flush()
        return
