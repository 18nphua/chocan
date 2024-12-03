"""
File: Provider.py
Name: Huan Nguyen 
Desc: This file contains the Provider class, which will manage all provider-specific information
      and operations for the ChocAn system.

"""
import valid as v
import DatabaseApi as db

PROVIDER_ID_LENGTH = 9

class Provider():
    def __init__(self) -> None:
        self.provider_id = 0
        self.provider_name = None
        self.database = db.db_client()

    def read_provider_num(self) -> bool: 
        validated = False
        self.provider_num = v.read_int("Please enter your provider number: ")

        while len(str(self.provider_id)) != PROVIDER_ID_LENGTH:
            print(f"Please enter a 9-digit number.\n")
            self.provider_id = v.read_int("Please enter your provider number: ")

        self.provider_name = self.database.prov_get_name_from_id(self.self.provider_id)        

        if self.provider_name is not None:
            print("Validated.")
            print(f"Welcome {self.provider_name}")
            validated = True

        else:
            print("Invalid provider number entered.")

        return validated

    def generate_bill(self) -> None:
        pass

    def log_service(self) -> None:
        pass
