#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script allows you to automatically control the fan speed using the controller.
Controller must be a program that can receive commands NORMAL and MAX.
"""
import sys
import argparse

from time import sleep

from sensors import Sensors
from controller import FanController

# Defaults arguments
DEFAULTS = {
    'timeout': 5,
    'max_temp': 75,
    'controller_path': './fan_controller.pl',
}


def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--path', default=DEFAULTS['controller_path'])
    parser.add_argument('--temp', default=DEFAULTS['max_temp'])
    parser.add_argument('--sleep', default=DEFAULTS['timeout'])

    params = parser.parse_args(sys.argv[1:])

    return [params.path, params.temp, params.sleep]


def control(sensors, controller, max_temp, sleep_time_sec):
    # take control
    controller.normal()
    max_speed_active = False

    while True:
        temp = sensors.max_temp()

        if temp > max_temp and not max_speed_active:
            controller.max()
            max_speed_active = True
        elif temp <= max_temp and max_speed_active:
            controller.normal()
            max_speed_active = False

        sleep(sleep_time_sec)


if __name__ == '__main__':
    controller_path, max_temp, sleep_time_sec = arguments()

    try:
        control(
            Sensors(),
            FanController(controller_path),
            max_temp,
            sleep_time_sec
        )
    except RuntimeError:
        exit(1)
