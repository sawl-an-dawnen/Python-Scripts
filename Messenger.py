from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")


class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners
    
    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)

    def receive(self, message):
        # Must be implemented by extending classes
        pass

class Message:
    def __init__(self, m, t):
        self.message = m
        self.timeStamp = t
    def print(self):
        print(self.timeStamp + ": " + self.message)

class SaveMessages(Messenger):
    log = []

    def receive(self, message):
        self.log.append(Message(message,getCurrentTime()))

    def printMessages(self):
        for message in self.log:
            message.print()
    pass

listener = SaveMessages()

sender = Messenger([listener])

sender.send('Hello, there! This is the first message')

sender.send('Oh hi! This is the second message!')

sender.send('Hola! This is the third and final message!')

listener.printMessages()