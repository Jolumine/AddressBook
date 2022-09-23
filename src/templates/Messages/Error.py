from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel 
from PyQt5.QtGui import QIcon 

from ...const import ERROR_LOGO

class Error_Page(QDialog):
    def __init__(self, text:str, parent=None):
        super().__init__(parent)

        self.label = QLabel(text)

        self.root_layout = QVBoxLayout()
        self.root_layout.addWidget(self.label)

        self.setWindowTitle("Error")
        self.setWindowIcon(QIcon(ERROR_LOGO))
        self.setGeometry(350, 350, 175, 60)
        self.setLayout(self.root_layout)
        self.exec_()