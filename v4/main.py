"""
кот должен легко перемещаться вместе с предметами по нажатию на пробел
"""


import time

import view,controller

while True:
    time.sleep(1/100)
    controller.process()
    view.draw()