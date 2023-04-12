"""
создать слой воды на карте толщиной 30 пикселей.
"""


import time

import view,controller

while True:
    time.sleep(1/100)
    controller.process()
    view.draw()