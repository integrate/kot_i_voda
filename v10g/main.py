"""
каждые три секунды, из облака должна выпадать капля
"""


import time

import view,controller, model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()