from encoderstrategy.EncoderStrategy import EncoderStrategy
from cfg.GsConfig import GsConfig


class VentilationEncoder(EncoderStrategy):

    def __init__(self, cfg: GsConfig):
        super(VentilationEncoder, self).__init__(cfg)

    def encode(self, commands: dict) -> str:
        """
        :param commands: A map with the reservoir number as key and the commend to be encoded as value.
        :return: The encoded string
        """
        msg = ""
        for gs_id, lvl in commands.items():
            if lvl == 'stop':
                msg += f"{self.cfg.command_code_map['ventilation_stop']}\n"
            else:
                msg += f"{self.cfg.command_code_map['ventilation']}{lvl}\n"
        return msg
