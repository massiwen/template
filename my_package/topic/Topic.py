from abc import ABC


class Topic(ABC):

    def __init__(self, events):
        super().__init__()

        self.events = {event: dict()
                       for event in events}

    def get_subscribers(self, event):
        return self.events[event]

    def subscribe(self, event: str, sub: object, callback: classmethod):
        """
        :param event: The channel where the subscribers is listening
        :param sub: The subscriber to be notified with a callback function
        :param callback: sub.method_foo is equivalent to "method_foo"
        :return:
        """
        self.get_subscribers(event)[sub] = callback

    def unsubscribe(self, event, sub: object):
        del self.get_subscribers(event)[sub]

    def dispatch(self, event: str, message: dict):
        """
        :param event: The channel where the message is dispatched
        :param message: A map with the gas id as key and the encoded data as value
        """
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)

    # @abstractmethod
    # def get_message(self) -> object:
    #     pass
