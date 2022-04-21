from abc import ABC, abstractmethod

from cfg.GsConfig import GsConfig


class EncoderStrategy(ABC):

    def __init__(self, cfg: GsConfig):
        self.cfg = cfg

    @abstractmethod
    def encode(self, commands: dict) -> str:
        """
        :param commands: A map with the reservoir number as key and the commend to be encoded as value.
        :return: The encoded string
        """
        pass
