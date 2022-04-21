from encoderstrategy.EncoderStrategy import EncoderStrategy
from cfg.GsConfig import GsConfig


class GasInjectionEncoder(EncoderStrategy):
    def __init__(self, cfg: GsConfig):
        super(GasInjectionEncoder, self).__init__(cfg)

    def encode(self, commands: dict) -> str:
        """
        :param commands: A map with the reservoir number as key and the commend to be encoded as value.
        :return: The encoded string
        """
        msg = ""
        for gs_id, lvl in commands.items():
            msg += f"{lvl}{gs_id}\n"
        return msg
