import socket


class OutputSocket:

    def __init__(self, host, port_out):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # try:
        self.s.connect((host, port_out))
        # except ConnectionRefusedError as e:
        #     print(e)

    def send_command(self, msg: str):
        self.s.send(msg.encode())
