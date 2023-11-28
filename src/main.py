import sys
from PyQt5.QtWidgets import QApplication
from views import CalculatorView

def main():
    app = QApplication(sys.argv)
    view = CalculatorView()
    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()