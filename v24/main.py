"""
начиная с уровня 4 с каждым уровнем капли начинают капать чаще.
теперь появление капель не должно зависеть от смены направления полета облака
"""


import time

import view,controller,model

while True:
    time.sleep(1/100)
    controller.process()
    model.go_go_go()
    view.draw()