"""
когда капля касается зонтика или ведра - она исчезает
"""


import time

import view,controller,model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()