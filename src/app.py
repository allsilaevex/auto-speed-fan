import sys
import argparse

from time import sleep
from datetime import datetime

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

    # Information about the active mode
    max_speed_active = False

    def __init__(self):
        """App constructor"""
        self.__arguments()

        self.sensors = Sensors()
        self.controller = FanController(self.controller_path)

    def run(self):
        """Application run"""

        # take control
        self.__activate_normal_mode(self.sensors.max_temp())

        while True:
            temp = self.sensors.max_temp()

            if temp > self.max_temp_c and not self.max_speed_active:
                self.__activate_max_mode(temp)
            elif temp <= self.max_temp_c and self.max_speed_active:
                self.__activate_normal_mode(temp)
            else:
                self.__print_info('max' if self.max_speed_active else 'normal', temp)

            sleep(self.sleep_sec)

    def __activate_normal_mode(self, temp):
        """Activate normal mode"""
        self.controller.normal()
        self.max_speed_active = False
        self.__print_info('normal', temp)

    def __activate_max_mode(self, temp):
        """Activate max mode"""
        self.controller.max()
        self.max_speed_active = True
        self.__print_info('max', temp)

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

    @staticmethod
    def __print_info(mode, temp):
        """Print information"""
        time = datetime.today().strftime("%d-%m-%Y %H:%M:%S")

        print(f'[{time}] [+{temp}°C] {mode}')
