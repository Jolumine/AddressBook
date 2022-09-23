import unittest

import Ops
import json
import os 

PATH = f"C:/Users/{os.getlogin()}/AppData/Local/AddressBookData/entrys.json"


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.test_firstname = "Testfname"
        self.test_lastname = "Testlname"
        self.test_phonenumber = "12345678910"

    def test1creation(self):
        test_creation = Ops.Ops.create_entry(self.test_firstname, self.test_lastname, self.test_phonenumber, "", "")

        with open(PATH, "r") as f:
            parsed = json.load(f)

        self.assertEqual(test_creation, None)

        self.assertEqual(len(parsed["Contacts"]), 1)
        self.assertEqual(parsed["Contacts"]["1"]["Firstname"], self.test_firstname)
        self.assertEqual(parsed["Contacts"]["1"]["Lastname"], self.test_lastname)
        self.assertEqual(parsed["Contacts"]["1"]["Phonenumber"], self.test_phonenumber)


    def test2getentrys(self):
        returned_data = Ops.Ops.get_entrys()

        self.assertEqual(len(returned_data), 1)
        self.assertTrue(isinstance(returned_data, list))  

    def test3getfirstname(self):
        returned_data = Ops.Ops.get_fname("1")
        self.assertEqual(Ops.Ops.get_fname("2"), None)
        self.assertEqual(returned_data, self.test_firstname) 

    def test4delete(self):
        returned_data = Ops.Ops.delete_entry("1")
        with open(PATH, "r") as f:
            parsed = json.load(f)
        self.assertEqual(returned_data, None)
        self.assertEqual(len(parsed["Contacts"]), 0)



if __name__ == "__main__":
    unittest.main()