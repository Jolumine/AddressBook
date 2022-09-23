from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QComboBox
from PyQt5.QtGui import QIcon

from .Create.Create import Create_Dialog
from .Open.Open import Open_Dialog
from .Settings.Settings import Settings_Dialog

from .Messages.Error import Error_Page

from ..const import BOOK_CLOSED_LOGO
from ..data.Ops import Ops


class Home(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.search_line = QLineEdit(self)
        self.search_line.setPlaceholderText("Search")
        self.search_line.setToolTip("Enter a the name of an entry")
        self.search_line.textChanged.connect(self.search)

        self.entrys = QComboBox(self)
        self.entrys.setToolTip("Select the entry to open")
        self.entrys.addItems(Ops.get_entrys())
        
        self.open_button = QPushButton("Open", self)
        self.open_button.setToolTip("Click to open the selected entry")
        self.open_button.clicked.connect(self.read)

        self.create_button = QPushButton("Create", self)
        self.create_button.setToolTip("Click to create a new entry")
        self.create_button.clicked.connect(self.create)

        self.settings_button = QPushButton("Settings", self)
        self.settings_button.setToolTip("Click to open the settings")
        self.settings_button.clicked.connect(self.open_settings)

        self.root_layout = QVBoxLayout()
        self.root_layout.addWidget(self.search_line)
        self.root_layout.addWidget(self.entrys)
        self.root_layout.addWidget(self.open_button)
        self.root_layout.addWidget(self.create_button)
        self.root_layout.addWidget(self.settings_button)

        self.setWindowTitle("Address Book")
        self.setGeometry(300, 300, 375, 275)
        self.setWindowIcon(QIcon(QIcon(BOOK_CLOSED_LOGO)))
        self.setLayout(self.root_layout)
        self.show()

    def search(self):
        self.entrys.clear()
        entrys = Ops.get_entrys(self.search_line.text())
        if len(entrys) == 0 and self.search_line.text() != "": 
            self.entrys.addItem("--No entrys found--")
        else: 
            self.entrys.addItems(entrys)

    def read(self):
        selected = self.entrys.currentText()

        if selected != "":
            return Open_Dialog(number=self.entrys.currentText().split("-")[0],name=f"{self.entrys.currentText().split('-')[1]} {self.entrys.currentText().split('-')[2]}") 
        else: 
            Error_Page("No entry selected.")

        self.render_data()

    def create(self):
        Create_Dialog()
        self.render_data()

    def open_settings(self):
        return Settings_Dialog() 


    def render_data(self):
        self.entrys.clear()
        self.entrys.addItems(Ops.get_entrys())
