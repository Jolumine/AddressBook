from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

from ...const import CONFIRM_LOGO

class Confirm_Page(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Confirm")
        self.setWindowIcon(QIcon(CONFIRM_LOGO))
        self.setText("Please confirm the process.")
        self.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
        self.setDefaultButton(QMessageBox.Cancel)
