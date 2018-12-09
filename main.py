import sys
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow
import time
import threading


app = QApplication(sys.argv)
calculator = CalculatorWindow()
#calculator2 = CalculatorWindow()


def my_timer(ui_calc):
    while True:
        ui_calc.clock()
        time.sleep(1)


my_thread = threading.Thread(target=my_timer, args=[calculator, ])
my_thread.start()


sys.exit(app.exec_())

