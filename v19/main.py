"""
сделайте, чтобы окончание слова "капель" было правильным для все цифр.
например: 1 капля, 2 капли, 12 капель
"""


import time

import view,controller,model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()