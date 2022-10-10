import os 
import json 
import logging

from ..security import generate_hash
from ..const import PATH

ENTRYS = f"C:/Users/{os.getlogin()}/AppData/Local/AddressBookData/entrys.json"

class Ops: 
    @staticmethod
    def create_entry(fname, lname, phone, eaddr, addr) -> None:
        data = {"Firstname": fname, "Lastname": lname, "Phonenumber": phone, "Mail Address": eaddr, "Address": addr}

        with open(ENTRYS, "r") as f: 
            parsed = json.load(f)
            f.close()


        with open(ENTRYS, "w") as f: 
            parsed["Contacts"][str(len(parsed["Contacts"])+1)] = data
            new = json.dumps(parsed, indent=4, sort_keys=False)
            f.write(new)
            f.close()

        logging.basicConfig(filename=PATH+"/logs.log", encoding="utf-8", format='%(asctime)s %(message)s', level=logging.INFO)
        logging.info(f"User {generate_hash(fname)} created [OK]")

        return None 

    @staticmethod
    def get_entrys(filter="") -> list: 
        result = []

        with open(ENTRYS, "r") as f: 
            parsed = json.load(f)

        if filter != "":
            for entry in parsed["Contacts"]:
                if filter in parsed['Contacts'][entry]['Firstname'] or filter in parsed['Contacts'][entry]['Lastname']:
                    result.append(f"{entry}-{parsed['Contacts'][entry]['Firstname']}-{parsed['Contacts'][entry]['Lastname']}") 
                else: 
                    pass 
        else:
            for entry in parsed["Contacts"]: 
                result.append(f"{entry}-{parsed['Contacts'][entry]['Firstname']}-{parsed['Contacts'][entry]['Lastname']}")

        return result

    @staticmethod
    def delete_entry(num):
        with open(ENTRYS, "r") as f: 
            parsed = json.load(f)
            f.close()
        
        del parsed["Contacts"][num]    
        parsed_data = json.dumps(parsed, indent=4, sort_keys=False)

        with open(ENTRYS, "w") as f: 
            f.close()

        with open(ENTRYS, "w") as f: 
            f.write(parsed_data)

        logging.basicConfig(filename=PATH+"/logs.log", encoding="utf-8", format='%(asctime)s %(message)s', level=logging.INFO)
        logging.info(f"User {generate_hash(Ops.get_fname(num))} deletion [OK]")

    @staticmethod
    def get_fname(num):
        with open(ENTRYS, "r") as f: 
            parsed = json.load(f)

            for entry in parsed["Contacts"]: 
                if entry == num: 
                    return parsed["Contacts"][entry]["Firstname"]
                
            return None
