from groupyou.jobs.reaction import Reaction
from http import client as htcli


class Weather(Reaction):

    def __init__(self):
        self.message = ''

    def react(self, user_name, text, attachments):
        if text.startswith('weather'):
            command = text.split(' ')
            if len(command) == 3:
                if command[1] == 'forecast':

            elif len(command) == 2:

            elif len(command) == 1:
                pass
            else:
                self.message = 'Bad format for weather call'
                return True

            conn = htcli.HTTPConnection

            return True
        return False

    def run(self, chat):
        chat.add_text(self.message)
        chat.flush()
        return
