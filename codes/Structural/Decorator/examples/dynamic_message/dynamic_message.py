from abc import ABC, abstractmethod


# Component
class Message(ABC):
    @abstractmethod
    def get_text(self):
        pass


# ConcreteComponent
class SimpleMessage(Message):
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text


# Decorator
class MessageDecorator(Message):
    def __init__(self, message):
        self._message = message

    def get_text(self):
        return self._message.get_text()


# ConcreteDecoratorA
class PMessageDecorator(MessageDecorator):
    def get_text(self):
        return f"<p>{super().get_text()}</p>"


# ConcreteDecoratorB
class JSMessageDecorator(MessageDecorator):
    def get_text(self):
        return f"<script>{super().get_text()}</script>"


# ConcreteDecoratorC
class LinkMessageDecorator(PMessageDecorator):
    def __init__(self, message, link):
        super().__init__(message)
        self._link = link


    def get_text(self):
        return f"<a href='{self._link}'>{super().get_text()}</a>"


# Client code
def main():
    simple = SimpleMessage("Hello, World!")
    print("Simple:", simple.get_text())

    html_message = PMessageDecorator(simple)
    print("P:", html_message.get_text())

    js_message = JSMessageDecorator(html_message)
    print("P + JavaScript:", js_message.get_text())

    link_message = LinkMessageDecorator(simple, "https://www.example.com")
    print("P + Link:", link_message.get_text())


if __name__ == "__main__":
    main()
