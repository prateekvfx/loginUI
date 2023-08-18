import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from loginUI import Ui_Form


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ILM Login")
        # self.setGeometry(1100, 400, 500, 500)
        self.setWindowIcon(QIcon("icons/ilm.png"))

        self.ui = Ui_Form()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())

