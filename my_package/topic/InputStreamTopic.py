from threading import Semaphore

from topic.Topic import Topic


class InputStreamTopic(Topic):

    def __init__(self, events: list):
        super(InputStreamTopic, self).__init__(events)
        self.gas_overview = dict()

    def dispatch(self, event: str, message: dict, s: Semaphore, ):
        s.acquire()
        for gas_id, val in message.items():
            if val:
                self.gas_overview[gas_id] = val
        super(InputStreamTopic, self).dispatch(event, self.gas_overview)
        s.release()
