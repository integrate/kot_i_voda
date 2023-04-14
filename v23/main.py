"""
добавьте надпись о том, какой сейчас уровень.
уровень должен увеличиваться с каждым окончанием обратного отсчета
"""


import time

import view,controller,model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()