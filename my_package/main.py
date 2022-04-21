import os
import threading
from time import sleep

from action.Aeration import Aeration
from action.Alarm import Alarm
from action.GasInjection import GasInjection
from action.Ventilation import Ventilation
from cfg.GsConfig import GsConfig
from socketgs.InputSocket import InputSocket
from socketgs.OutputSocket import OutputSocket
from topic.CommandTopic import CommandTopic
from topic.InputStreamTopic import InputStreamTopic


def main():
    # INITIALISE TOPICS
    input_stream_topic = InputStreamTopic(['data'])
    command_topic = CommandTopic(['command', 'alarm', 'aeration', 'gas_injection', 'ventilation'])

    # INITIALISE OBJECTS
    cfg = GsConfig()
    alarm = Alarm(cfg, command_topic)
    aeration = Aeration(cfg, command_topic)
    ventilation = Ventilation(cfg, command_topic)
    gas_injection = GasInjection(cfg, command_topic)

    in_sock = InputSocket(cfg, input_stream_topic)
    out_sock = OutputSocket(cfg.connection['ip'], cfg.connection['port_out'])

    # SUBSCRIPTIONS TO INPUT_STREAM_TOPIC
    input_stream_topic.subscribe(event='data', sub=alarm, callback=alarm.evaluate_concentration)
    input_stream_topic.subscribe(event='data', sub=aeration, callback=aeration.evaluate_concentration)
    input_stream_topic.subscribe(event='data', sub=ventilation, callback=ventilation.evaluate_concentration)
    input_stream_topic.subscribe(event='data', sub=gas_injection, callback=gas_injection.evaluate_concentration)

    # SUBSCRIPTIONS TO COMMAND_TOPIC
    command_topic.subscribe(event='command', sub=out_sock, callback=out_sock.send_command)

    # START THREADS
    listening_thread = threading.Thread(target=in_sock.start_listening, name='ListeningThread')
    listening_thread.start()


if __name__ == "__main__":
    # a = os.system("start " + '../resources/GasSystemSimulationLab.jar')
    sleep(4)
    print('GasSystem Control  - Started')
    main()
    print('GasSystem Control - Ended')
