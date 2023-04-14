"""
сделайте обратный отсчет капель, выпущенных облаком от 5 до 0.
при достижении 0 отсчет начинается заново
"""


import time

import view,controller,model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()