from abc import ABC, abstractmethod


# Abstract Implementor
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass


# Concrete Implementors
class EmailChannel(NotificationChannel):
    def send(self, message, recipient):
        print(f"Sending email to {recipient}: {message}")


class SMSChannel(NotificationChannel):
    def send(self, message, recipient):
        print(f"Sending SMS to {recipient}: {message}")


# Abstraction
class MessageSender(ABC):
    def __init__(self, channel: NotificationChannel):
        self.channel = channel

    @abstractmethod
    def send_message(self, message, recipient):
        pass


# Concreate Abstractions
class UrgentMessageSender(MessageSender):
    def send_message(self, message, recipient):
        print("Marking message as urgent...")
        self.channel.send(message, recipient)


class NormalMessageSender(MessageSender):
    def send_message(self, message, recipient):
        self.channel.send(message, recipient)


# Client Code
def main():
    email_channel = EmailChannel()
    urgent_email_sender = UrgentMessageSender(email_channel)
    urgent_email_sender.send_message("Important: Please check your account!", "user@example.com")

    print("\n")

    sms_channel = SMSChannel()
    normal_sms_sender = NormalMessageSender(sms_channel)
    normal_sms_sender.send_message("Reminder: Meeting tomorrow.", "+1234567890")


if __name__ == "__main__":
    main()
