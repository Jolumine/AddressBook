import json
import os
import urllib.request
import requests
import logging

from .const import LISTED_LOGOS


class Setup: 
    PATH = f"C:/Users/{os.getlogin()}/AppData/Local/AddressBookData/"
    def __init__(self):
        if not os.path.exists(self.PATH):
            os.mkdir(self.PATH)
            os.chdir(self.PATH)
            os.mkdir(self.PATH+"Logos")

            with open(self.PATH+"/logs.log", "w") as f: 
                f.close()
            
            with open(f"{self.PATH}/entrys.json", "w") as f: 
                entry_data = {"Contacts": {}}
                parsed = json.dumps(entry_data, indent=4, sort_keys=False)
                f.write(parsed)

            logging.basicConfig(filename=self.PATH+"/logs.log", encoding="utf-8", format='%(asctime)s %(message)s', level=logging.INFO)
            logging.info("Folder setup [OK]")
            
    
        if self.check_logos():
            pass 
        else: 
            try: 
                logging.basicConfig(filename=self.PATH+"/logs.log", encoding="utf-8", format='%(asctime)s %(message)s', level=logging.INFO)
                logging.info("Try downloading logos [?]")
                requests.get("https://www.google.com", timeout=5)
            except(requests.Timeout, requests.ConnectionError) as e:
                logging.basicConfig(filename=self.PATH+"/logs.log", encoding="utf-8", format='%(asctime)s %(message)s', level=logging.INFO)
                logging.error("Logo download failed. No internet connection. [x]") 
            else:  
                urllib.request.urlretrieve("https://cdn-icons-png.flaticon.com/512/32/32354.png", self.PATH+"/Logos/Book_Closed_Logo.png")
                urllib.request.urlretrieve("https://cdn-icons-png.flaticon.com/512/1387/1387940.png", self.PATH+"/Logos/Add_Logo.png")
                urllib.request.urlretrieve("https://cdn-icons-png.flaticon.com/512/171/171322.png", self.PATH+"/Logos/Book_Open_Logo.png")
                urllib.request.urlretrieve("https://cdn-icons-png.flaticon.com/512/1004/1004765.png", self.PATH+"/Logos/Confirm_Logo.png") 
                urllib.request.urlretrieve("https://cdn-icons-png.flaticon.com/512/159/159454.png", self.PATH+"/Logos/Error_Logo.png")
                urllib.request.urlretrieve("https://cdn-icons-png.flaticon.com/512/1827/1827933.png", self.PATH+"/Logos/Modify_Logo.png") 
                urllib.request.urlretrieve("https://cdn-icons-png.flaticon.com/512/1214/1214428.png", self.PATH+"/Logos/Delete_Logo.png")
                urllib.request.urlretrieve("https://cdn-icons-png.flaticon.com/512/3524/3524636.png", self.PATH+"/Logos/Settings_Logo.png")
                urllib.request.urlretrieve("https://cdn-icons-png.flaticon.com/512/149/149852.png", self.PATH+"/Logos/Search_Logo.png")
                urllib.request.urlretrieve("https://cdn-icons-png.flaticon.com/512/4743/4743125.png", self.PATH+"/Logos/Save_Logo.png") 
                urllib.request.urlretrieve("https://cdn-icons-png.flaticon.com/512/876/876215.png", self.PATH+"Logos/Cancel_Logo.png")

                logging.basicConfig(filename=self.PATH+"/logs.log", encoding="utf-8", format='%(asctime)s %(message)s', level=logging.INFO)
                logging.info("Logo download [OK]")

    @staticmethod
    def check_logos() -> bool:
        for logo in LISTED_LOGOS:
            if os.path.exists(logo):
                pass 
            else: 
                return False 
        return True 


    