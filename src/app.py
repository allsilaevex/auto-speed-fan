import sys
import argparse

from time import sleep

from .sensors import Sensors
from .controller import FanController


class App:
    """App class"""

    # Time between temperature checks
    sleep_sec = 5

    # Upper limit to enable turbo mode
    max_temp_c = 75

    # Path to fan controller
    controller_path = './fan_controller.pl'

    def __init__(self):
        """App constructor"""
        self.__arguments()

        self.sensors = Sensors()
        self.controller = FanController(self.controller_path)

    def run(self):
        """Application run"""

        # take control
        self.controller.normal()
        max_speed_active = False

        while True:
            temp = self.sensors.max_temp()

            if temp > self.max_temp_c and not max_speed_active:
                self.controller.max()
                max_speed_active = True
            elif temp <= self.max_temp_c and max_speed_active:
                self.controller.normal()
                max_speed_active = False

            sleep(self.sleep_sec)

    def __arguments(self):
        """Parse arguments"""
        parser = argparse.ArgumentParser()

        parser.add_argument('--path', default=self.controller_path)
        parser.add_argument('--temp', default=self.max_temp_c)
        parser.add_argument('--sleep', default=self.sleep_sec)

        params = parser.parse_args(sys.argv[1:])

        self.sleep_sec = params.sleep
        self.max_temp_c = params.temp
        self.controller_path = params.path
