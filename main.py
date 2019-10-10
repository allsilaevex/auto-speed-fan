#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script allows you to automatically control the fan speed using the controller.
Controller must be a program that can receive commands NORMAL and MAX.
"""
from src.app import App


if __name__ == '__main__':
    app = App()

    try:
        app.run()
    except RuntimeError:
        exit(1)
