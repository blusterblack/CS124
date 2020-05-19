import re


class Eliza:
    def __init__(self):
        self.isStop = False

    def ask(self, str):
        str = str.lower()
        print(self.think(str))

    def think(self, str):
        if re.search('hello|hi|good (morning|afternoon|evening)', str):
            answer = 'Hello. What can I do for you?'
        elif re.search('bye', str):
            answer = "Goodbye. Have a good day."
            self.isStop = True
        elif re.search("i (hate|love) (.*)", str):
            g = re.search("i (hate|love) (.*)", str).group
            answer = f'What make you think {g(1)}ing {g(2)} is a good idea?'
        else:
            answer = 'I will consider it.'
        return answer

    def start(self):
        while not self.isStop:
            self.ask(input())


chatbot = Eliza()
chatbot.start()
