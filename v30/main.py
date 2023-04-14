"""
при появлении солнца уменьшаются
    скорость движения тучи,
    скорость падения капли,
    частота падения капли,
    уровень воды

новое солнце нельзя показать, пока не исчезло старое
"""


import time

import view,controller,model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()