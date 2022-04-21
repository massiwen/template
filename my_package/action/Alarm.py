from action.Action import Action
from encoderstrategy.AlarmEncoder import AlarmEncoder
from cfg.GsConfig import GsConfig

from topic import CommandTopic


class Alarm(Action):

    def __init__(self, cfg: GsConfig, topic: CommandTopic):
        super(Alarm, self).__init__(cfg, topic)

    def evaluate_concentration(self, values: dict):
        command = dict()
        for gas_id, val in values.items():
            for threshold, lvl_code in self.cfg.alarm_threshold_lvl.items():
                if val in range(threshold[0], 1 + threshold[1]):
                    command[gas_id] = lvl_code

        self.dispatch_action(command, 'alarm', AlarmEncoder(self.cfg))
