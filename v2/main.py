"""добавьте коту зонтик"""

import time

import view,controller

while True:
    time.sleep(1/100)
    controller.process()
    view.draw()