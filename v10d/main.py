"""
облако должно раз в три секунды менять направление на случайное
"""


import time

import view,controller, model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()