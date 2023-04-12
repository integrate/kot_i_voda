"""
при развороте кота его ведро должно оставаться на том же месте, где и было
"""


import time

import view,controller

while True:
    time.sleep(1/100)
    controller.process()
    view.draw()