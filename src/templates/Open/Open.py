from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon

from ..Messages.Confirm import Confirm_Page

from ...security import generate_hash
from ...const import BOOK_OPEN_LOGO, DELETE_LOGO, MODIFY_LOGO, SAVE_LOGO, CANCEL_LOGO, PATH
from ...data.Ops import ENTRYS, Ops

import json
import logging


class Open_Dialog(QDialog):
    def __init__(self, number, name, parent=None):
        super().__init__(parent)

        self.number = number

        with open(ENTRYS, "r") as f:
            self.parsed = json.load(f)

        entry = self.parsed["Contacts"][self.number]

        self.firstname = QLabel("Firstname:")

        self.fname = QLineEdit(self)
        self.fname.setReadOnly(True)
        self.fname.setText(entry["Firstname"])

        self.lastname = QLabel("Lastname:")

        self.lname = QLineEdit(self)
        self.lname.setReadOnly(True)
        self.lname.setText(entry["Lastname"])

        self.phone = QLabel("Phonenumber:")

        self.pnumber = QLineEdit(self)
        self.pnumber.setReadOnly(True)
        self.pnumber.setText(entry["Phonenumber"])

        self.address = QLabel("Adress:")

        self.addr = QLineEdit(self)
        self.addr.setReadOnly(True)
        self.addr.setText(entry["Address"])

        self.mail = QLabel("Mail Address:")

        self.mail_addr = QLineEdit(self)
        self.mail_addr.setReadOnly(True)
        self.mail_addr.setText(entry["Mail Address"])

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setIcon(QIcon(DELETE_LOGO))
        self.delete_button.setToolTip("Click to delete the current book entry")
        self.delete_button.clicked.connect(self.delete_function)

        self.modify_button = QPushButton("Modify", self)
        self.modify_button.setIcon(QIcon(MODIFY_LOGO))
        self.modify_button.setToolTip("Click to modify the current book entry")
        self.modify_button.clicked.connect(self.modify)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.setIcon(QIcon(CANCEL_LOGO))
        self.cancel_button.setToolTip("Click to cancel the modifications")
        self.cancel_button.clicked.connect(self.cancel)
        self.cancel_button.hide()

        self.save_button = QPushButton("Save", self)
        self.save_button.setIcon(QIcon(SAVE_LOGO))
        self.save_button.setToolTip("Click to save the modifications.")
        self.save_button.clicked.connect(self.save)
        self.save_button.hide()

        self.fname_layout = QHBoxLayout()
        self.fname_layout.addWidget(self.firstname)
        self.fname_layout.addWidget(self.fname)

        self.lname_layout = QHBoxLayout()
        self.lname_layout.addWidget(self.lastname)
        self.lname_layout.addWidget(self.lname)

        self.phone_layout = QHBoxLayout()
        self.phone_layout.addWidget(self.phone)
        self.phone_layout.addWidget(self.pnumber)

        self.address_layout = QHBoxLayout()
        self.address_layout.addWidget(self.address)
        self.address_layout.addWidget(self.addr)

        self.mail_layout = QHBoxLayout()
        self.mail_layout.addWidget(self.mail)
        self.mail_layout.addWidget(self.mail_addr)

        self.opt_layout = QHBoxLayout()
        self.opt_layout.addWidget(self.modify_button)
        self.opt_layout.addWidget(self.delete_button)

        self.coloum_1 = QVBoxLayout()
        self.coloum_1.addLayout(self.fname_layout)
        self.coloum_1.addLayout(self.lname_layout)
        self.coloum_1.addLayout(self.phone_layout)

        self.coloum_2 = QVBoxLayout()
        self.coloum_2.addLayout(self.address_layout)
        self.coloum_2.addLayout(self.mail_layout)
        self.coloum_2.addLayout(self.opt_layout)

        self.root_layout = QHBoxLayout()
        self.root_layout.addLayout(self.coloum_1)
        self.root_layout.addLayout(self.coloum_2)

        self.setWindowTitle(f"{name}")
        self.setGeometry(350, 350, 600, 250)
        self.setWindowIcon(QIcon(BOOK_OPEN_LOGO))
        self.setLayout(self.root_layout)
        self.exec_()

    def delete_function(self):
        confirm_page = Confirm_Page()
        res = confirm_page.exec_()

        if res == QMessageBox.Cancel:
            pass
        else:
            logging.basicConfig(filename=PATH+"/logs.log", encoding="utf-8", format='%(asctime)s %(message)s', level=logging.INFO)
            logging.info(f"User {generate_hash(Ops.get_fname(self.number))} deletion [OK]")

            Ops.delete_entry(self.number)            
            self.close()

    def modify(self):
        self.fname.setReadOnly(False)
        self.lname.setReadOnly(False)
        self.pnumber.setReadOnly(False)
        self.addr.setReadOnly(False)
        self.mail_addr.setReadOnly(False)

        self.opt_layout.removeWidget(self.modify_button)
        self.opt_layout.removeWidget(self.delete_button)
        self.modify_button.hide()
        self.delete_button.hide()

        self.opt_layout.addWidget(self.cancel_button)
        self.opt_layout.addWidget(self.save_button)
        self.cancel_button.show()
        self.save_button.show()

    def cancel(self):
        self.fname.setReadOnly(True)
        self.lname.setReadOnly(True)
        self.pnumber.setReadOnly(True)
        self.addr.setReadOnly(True)
        self.mail_addr.setReadOnly(True)

        self.opt_layout.removeWidget(self.cancel_button)
        self.opt_layout.removeWidget(self.save_button)
        self.cancel_button.hide()
        self.save_button.hide()

        self.opt_layout.addWidget(self.modify_button)
        self.opt_layout.addWidget(self.delete_button)
        self.modify_button.show()
        self.delete_button.show()

        self.render_data()


    def save(self):
        changed_entry_data = {
            "Firstname": self.fname.text(),
            "Lastname": self.lname.text(),
            "Phonenumber": self.pnumber.text(), 
            "Mail Address": self.mail_addr.text(),
            "Address": self.addr.text()
        } 


        self.parsed["Contacts"][self.number] = changed_entry_data

        with open(ENTRYS, "w") as f: 
            json.dump(self.parsed, f, indent=4, sort_keys=False)

        logging.basicConfig(filename=PATH+"/logs.log", encoding="utf-8", format='%(asctime)s %(message)s', level=logging.INFO)
        logging.info(f"User {generate_hash(self.fname.text())} modified [OK]")

        self.cancel()

    
    def render_data(self):
        self.fname.clear()
        self.lname.clear()
        self.pnumber.clear()
        self.addr.clear()
        self.mail_addr.clear()

        with open(PATH+"/entrys.json", "r") as f: 
            parsed = json.load(f)

        self.fname.setText(parsed["Contacts"][self.number]["Firstname"])
        self.lname.setText(parsed["Contacts"][self.number]["Lastname"])
        self.pnumber.setText(parsed["Contacts"][self.number]["Phonenumber"])
        self.addr.setText(parsed["Contacts"][self.number]["Address"])
        self.mail_addr.setText(parsed["Contacts"][self.number]["Mail Address"])
