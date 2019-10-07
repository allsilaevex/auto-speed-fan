import os
import re


class Sensors:
    """
    Sensors class
    """

    COMMAND = 'sensors'

    def __init__(self):
        """Constructor"""
        self.clear_info = re.compile(r'\([^\)]+\)')
        self.find_temps = re.compile(r'\+([\d\.]+)°C')

    def max_temp(self):
        """Get max temperature from monitoring data"""
        temps = self.__parse(self.__run_command())
        return max(list(map(float, temps)))

    def __run_command(self):
        """Get monitoring data"""
        return os.popen(self.COMMAND).read()

    def __parse(self, res):
        """Parse monitoring data"""
        res = self.clear_info.sub('', res)
        return self.find_temps.findall(res)
