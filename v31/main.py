"""
каждое появление солнца должно стоить 10 монет.
если монет недостаточно, то солнце не появляется
"""


import time

import view,controller,model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()