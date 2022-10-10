from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon 

from ..Messages.Confirm import Confirm_Page
from ..Messages.Error import Error_Page

from ...security import generate_hash
from ...data.Ops import Ops 
from ...const import ADD_LOGO, PATH


class Create_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.firstname = QLineEdit(self)
        self.firstname.setPlaceholderText("Firstname*")
        self.firstname.setToolTip("Enter the firstname.")

        self.lastname = QLineEdit(self)
        self.lastname.setPlaceholderText("Lastname*")
        self.lastname.setToolTip("Enter the lastname")

        self.phone_number = QLineEdit(self)
        self.phone_number.setPlaceholderText("Phone number*")
        self.phone_number.setToolTip("Enter the phone number")

        self.address = QLineEdit(self)
        self.address.setPlaceholderText("Address (optional)")
        self.address.setToolTip("Enter an address")

        self.mail_address = QLineEdit(self)
        self.mail_address.setPlaceholderText("Mail Address (optional)")
        self.mail_address.setToolTip("Enter a Mail Address")

        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.setToolTip("Click to confirm the creation")
        self.confirm_button.clicked.connect(self.confirm)

        self.coloum_1 = QVBoxLayout()
        self.coloum_1.addWidget(self.firstname)
        self.coloum_1.addWidget(self.lastname)
        self.coloum_1.addWidget(self.phone_number)

        self.coloum_2 = QVBoxLayout()
        self.coloum_2.addWidget(self.address)
        self.coloum_2.addWidget(self.mail_address)
        self.coloum_2.addWidget(self.confirm_button)

        self.root_layout = QHBoxLayout()
        self.root_layout.addLayout(self.coloum_1)
        self.root_layout.addLayout(self.coloum_2)

        self.setWindowTitle(f"New entry")
        self.setGeometry(350, 350, 650, 250)
        self.setWindowIcon(QIcon(ADD_LOGO))
        self.setLayout(self.root_layout)
        self.exec_()

    def confirm(self) -> None :
        if self.firstname.text() == "" or self.lastname.text() == "" or self.phone_number.text() == "": 
            Error_Page("Please fill needed information.")
        else: 
            confirm_page = Confirm_Page()
            res = confirm_page.exec_()

            if res == QMessageBox.Cancel: 
                pass 
            else:
                fname = self.firstname.text()
                lname = self.lastname.text()
                phone = self.phone_number.text()
                mail = self.mail_address.text()
                addr = self.address.text()

                Ops.create_entry(fname, lname, phone, mail, addr)

                self.close()

        return None  
