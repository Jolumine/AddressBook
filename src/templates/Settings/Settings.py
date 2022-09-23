from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton
from PyQt5.QtGui import QIcon 


from ...const import SETTINGS_LOGO


class Settings_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.root_layout = QVBoxLayout()

        self.setWindowTitle("Settings")
        self.setGeometry(350, 350, 650, 250)
        self.setWindowIcon(QIcon(SETTINGS_LOGO))
        self.setLayout(self.root_layout)
        self.exec_()