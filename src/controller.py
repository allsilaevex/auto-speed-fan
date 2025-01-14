import os
import re


class FanController:
    """
    Fan Controller class
    """

    # Script executor
    EXECUTOR = 'perl'

    # Available commands
    COMMANDS = {
        'normal': 'NORMAL',
        'max': 'MAX',
    }

    # Part of answer for successful execution of command
    SUCCESS_RESPONSE = r'Successfully sent command'

    def __init__(self, path):
        """Constructor"""
        self.path = path
        self.success_test = re.compile(self.SUCCESS_RESPONSE)

    def normal(self):
        """Set normal mode"""
        res = self.__run_command(self.COMMANDS['normal'])

        self.__test(res)

    def max(self):
        """Set max mode"""
        res = self.__run_command(self.COMMANDS['max'])

        self.__test(res)

    def __test(self, res):
        """Verify success"""
        if not self.success_test.search(res):
            raise RuntimeError(res)

    def __run_command(self, command):
        """Run command from COMMANDS"""
        return os.popen(self.__make_command(command)).read()

    def __make_command(self, command):
        """Make a command for the script"""
        return f'{self.EXECUTOR} {self.path} {command}'
