"""
сделать слой воды толщиной 130 пикселей. волны на воде не должны растянуться
"""


import time

import view,controller

while True:
    time.sleep(1/100)
    controller.process()
    view.draw()