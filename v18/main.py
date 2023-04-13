"""
добавьте надпись "0 капель"
если капля попала в ведро - количество капель увеличивается
"""


import time

import view,controller,model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()