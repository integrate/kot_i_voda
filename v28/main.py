"""
через 3 секунды после нажатия солнце должно исчезнуть
"""


import time

import view,controller,model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()