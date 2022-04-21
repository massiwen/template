import queue
import re
import socket
import threading

from cfg.GsConfig import GsConfig
from topic.InputStreamTopic import InputStreamTopic


# import time


class InputSocket:
    """

    """

    def __init__(self, cfg: GsConfig, topic: InputStreamTopic):
        self.cfg = cfg
        self.topic = topic
        # self.sema = threading.Semaphore(1)
        self.msg_q = queue.Queue()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # try:
        self.s.connect((cfg.connection['ip'], cfg.connection['port_in']))
        # except ConnectionRefusedError as e:
        #     print(e)

    # def start_dispatching(self):
    #     while True:
    #         if not self.msg_q.empty():
    #             # Acquire shared resource
    #             self.sema.acquire()
    #             msg = self.msg_q.get()
    #             self.sema.release()
    #             # Dispatch message
    #             self.topic.dispatch(event='data', message=msg)
    #             time.sleep(2)

    def start_listening(self):
        s = threading.Semaphore(1)
        while True:
            msg = self.decode_gas_concentration(self.s.recv(2024).decode())
            # self.topic.dispatch(event='data', message=msg)

            thread = threading.Thread(target=self.topic.dispatch, args=('data', msg, s,), name='DispatchThread')
            thread.start()

            # # Acquire shared resource
            # self.sema.acquire()
            # self.msg_q.put_nowait(msg)
            # self.sema.release()

    def decode_gas_concentration(self, msg: str) -> map:
        """
        :param msg: Message from the GasSystem.
        :return: A map with the gas id as key and its concentration as value.
        """
        values_map = dict()
        code = self.cfg.command_code_map['concentration']
        for gas_id, v in self.cfg.gas_id_map.items():
            m = re.search(fr'(?<={code}{gas_id})\d+', msg)
            if m:
                value = int(m.group(0))
            else:
                value = None
            values_map[gas_id] = value

        return values_map
