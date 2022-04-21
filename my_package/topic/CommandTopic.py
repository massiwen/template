from topic.Topic import Topic


class CommandTopic(Topic):

    def __init__(self, events: list):
        super(CommandTopic, self).__init__(events)
        self.commands = ''

    def dispatch(self, event: str, message: dict):
        self.commands += message
        if event == 'gas_injection':
            # last command of the batch is gas_injection
            super(CommandTopic, self).dispatch('command', self.commands)
            self.commands = ""
