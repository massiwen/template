from action.Action import Action
from cfg.GsConfig import GsConfig
from encoderstrategy.VentilationEncoder import VentilationEncoder

from topic.CommandTopic import CommandTopic


class Ventilation(Action):
    def __init__(self, cfg: GsConfig, topic: CommandTopic):
        super(Ventilation, self).__init__(cfg, topic)

        self.gas_overview = dict()
        for gas_id, v in cfg.gas_id_map.items():
            self.gas_overview[gas_id] = 0

    def evaluate_concentration(self, values: dict):
        """

        :param values:
        :return:
        """

        command = dict()

        self.update_gas_overview(values)

        max_value = max(self.gas_overview.values())
        for threshold, lvl_code in self.cfg.ventilation_threshold_lvl.items():
            if max_value in range(threshold[0], 1 + threshold[1]):
                command['undef'] = lvl_code

        self.dispatch_action(command, 'ventilation', VentilationEncoder(self.cfg))

    def update_gas_overview(self, values: dict):
        for gas_id, val in values.items():
            if val:
                self.gas_overview[gas_id] = val
