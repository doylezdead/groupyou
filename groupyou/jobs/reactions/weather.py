from groupyou.jobs.reaction import Reaction
import urllib.request
import http.client as htcli

class Weather(Reaction):

    def __init__(self):
        self.message = ''

    def react(self, user_name, text, attachments):
        if text.startswith('weather'):
            command = text.split(' ')
            if len(command) == 3:
                if command[1] == 'forecast':
                    pass
            elif len(command) == 2:
                if command[1]:
                    try:
                        float(command[1])
                        if len(command[1]) is 5:
                            self.message = self.getCurrentZip(zipcode=command[1])
                            return True
                    except ValueError:
                        self.message = 'Bad zipcode'
                        return True

            else:
                self.message = 'Bad format for weather call'
                return True

            return True
        return False

    def getCurrentZip(self, zipcode="00000"):
        conn = htcli.HTTPConnection('http://api.wunderground.com')
        conn.request('GET', '/api/420931bcbb94c902/conditions/q/' + zipcode + '.json')
        response = conn.getresponse().read()

        # request = urllib.request.urlopen('http://api.wunderground.com/api/420931bcbb94c902/conditions/q/' + zipcode + '.json')
        # result = request.read()
        # request.close()
        print(response)
        return 'not good'



    def run(self, chat):
        chat.add_text(self.message)
        chat.flush()
        return
