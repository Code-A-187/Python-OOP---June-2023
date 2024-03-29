from abc import ABC, abstractmethod


class IProtocol(ABC):

    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

    def format_sender(self):
        pass

    def format_receiver(self):
        pass


class IContent(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class IM(IProtocol):
    def format_sender(self):
        return ''.join(["I'm ", self.sender])

    def format_receiver(self):
        return ''.join(["I'm ", self.receiver])


class MyMl(IContent):

    def format(self):
        return ''.join(['<myML>', self.text, '</myML>'])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        # ''.join(["I'm ", sender])
        self.__sender = sender

    def set_receiver(self, receiver):
        # ''.join(["I'm ", receiver])
        self.__receiver = receiver

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):

        template = f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"

        return template


myml = MyMl('Hello, there!')
email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(myml)
print(email)
