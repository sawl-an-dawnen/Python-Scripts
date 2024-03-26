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

class MessagesException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')

class TooManyMessages(MessagesException):
    statusCode = 500
    message = 'Your log is full!'

class MessageExceedsLength(MessagesException):
    statusCode = 601
    message = 'Incoming message exceeds maximum character length'

class Message:
    def __init__(self, m, t):
        self.message = m
        self.timeStamp = t
    def print(self):
        print(self.timeStamp + ": " + self.message)

class SaveMessages(Messenger):
    log = []
    max_messages = 10
    max_char = 10

    def receive(self, message):

        if len(self.log) >= self.max_messages:
            raise TooManyMessages()
        if len(message) >= self.max_char:
            raise MessageExceedsLength()
        self.log.append(Message(message,getCurrentTime()))

    def printMessages(self):
        for message in self.log:
            message.print()
        self.log = []
    pass

listener = SaveMessages()

sender = Messenger([listener])

sender.send('01')

sender.send('02')

sender.send('03')

sender.send('04')

sender.send('05')

sender.send('I am trying to exceed the maximum character length for these messages')

sender.send('07')

sender.send('08')

sender.send('09')

sender.send('10')

sender.send('11')

sender.send('12')


listener.printMessages()