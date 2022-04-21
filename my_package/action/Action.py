from abc import ABC, abstractmethod

from encoderstrategy.EncoderStrategy import EncoderStrategy
from cfg.GsConfig import GsConfig
from topic import CommandTopic


class Action(ABC):

    def __init__(self, cfg: GsConfig, topic: CommandTopic):
        self.cfg = cfg
        self.topic = topic

    @abstractmethod
    def evaluate_concentration(self, values: dict):
        """ Encapsulates the logic of the action.
        :param values: A map with gas id as key and concentration as values.
        """
        pass

    def dispatch_action(self, commands: dict, event: str, strategy: EncoderStrategy):
        """ Will dispatch the encoded action message to the CommandTopic if not empty.
        :param commands: A map with gas id as key and action as values to be encoded.
        :param event: The chanel on witch to dispatch the message
        :param strategy: The EncoderStrategy to use to encode the commands
        """
        if len(commands) > 0:
            msg = strategy.encode(commands)
            self.topic.dispatch(event, msg)
