import socket


class GsConfig:

    def __init__(self):
        ip = socket.gethostname()

        self.connection = {
            "ip": ip,
            "port_in": 1231,
            "port_out": 1232
        }

        self.gas_id_map = {
            1: "gas_1",
            2: "gas_2",
            3: "gas_3",
        }

        self.command_code_map = {
            'concentration': 'LG',
            'aeration': 'AL',
            'aeration_stop': 'AN',
            'ventilation': 'VL',
            'ventilation_stop': 'VN',
            'gaa_Injection': 'IG',
            'gas_Injection_stop': 'AIG',
            'alert': 'AG'
        }

        self.alarm_threshold_lvl = {
            (0, 5): '',
            (6, 20): 'L',
            (21, 50): 'M',
            (51, 999): 'H'
        }

        self.aeration_threshold_lvl = {
            (0, 5): 'stop',
            (6, 10): '1',
            (11, 15): '2',
            (16, 20): '3'
        }

        self.ventilation_threshold_lvl = {
            (0, 20): 'stop',
            (21, 35): '1',
            (36, 50): '2',

        }

        self.gas_injection_threshold_lvl = {
            (0, 50): 'AIG',
            (51, 999): 'IG',
        }
