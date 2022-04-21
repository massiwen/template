from action.Action import Action
from encoderstrategy.GasInjectionEncoder import GasInjectionEncoder
from cfg.GsConfig import GsConfig

from topic import CommandTopic


class GasInjection(Action):

    def __init__(self, cfg: GsConfig, topic: CommandTopic):
        super(GasInjection, self).__init__(cfg, topic)

    def evaluate_concentration(self, values: dict):
        command = dict()
        for gas_id, val in values.items():
            if val:
                for threshold, lvl_code in self.cfg.gas_injection_threshold_lvl.items():
                    if val in range(threshold[0], 1 + threshold[1]):
                        command[gas_id] = lvl_code

        self.dispatch_action(command, 'gas_injection', GasInjectionEncoder(self.cfg))
