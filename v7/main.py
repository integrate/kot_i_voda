"""
при нажатии на пробел кот должен поворачиваться в другую сторону
"""


import time

import view,controller

while True:
    time.sleep(1/100)
    controller.process()
    view.draw()