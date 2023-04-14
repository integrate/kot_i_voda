"""
когда количество капель до ускорения достигает 0, скорость облака должна увеличиться
"""


import time

import view,controller,model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()