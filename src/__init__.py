from PyQt5.QtWidgets import QApplication

from .templates.Home import Home 
from .setup import Setup

import sys 
import logging 

def main():
    app = QApplication(sys.argv)
    
    SETUP = Setup()

    logging.basicConfig(filename=SETUP.PATH+"/logs.log", encoding="utf-8", format='%(asctime)s %(message)s', level=logging.INFO)
    logging.info("Starting application [OK]")

    HOME = Home()

    sys.exit(app.exec_())