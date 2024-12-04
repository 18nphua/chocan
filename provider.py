"""
File: Provider.py
Name: Huan Nguyen 
Desc: This file contains the Provider class, which will manage all provider-specific information
      and operations for the ChocAn system.

"""
import valid 
import DatabaseApi as db
import datetime

PROVIDER_ID_LENGTH = 9
MEMBER_ID_LENGTH = 9

class Provider():
    def __init__(self) -> None:
        self.service_date = " "
        self.provider_id = 0
        self.member_id = 0
        self.service_code = 0
        self.comments = ""
        self.database = db.db_client()

    def read_provider_id(self) -> bool: 
        validated = False
        provider_name = None

        self.provider_id = valid.read_int("Please enter your provider ID number: ")

        while len(str(self.provider_id)) != PROVIDER_ID_LENGTH:
            print(f"Please enter a 9-digit number.\n")
            self.provider_id = valid.read_int("Please enter your provider ID number: ")

        provider_name = self.database.prov_get_name_from_id(self.provider_id)        

        if provider_name is not None:
            print("Validated.")
            print(f"\nWelcome {provider_name}")
            validated = True

        else:
            print("\nInvalid Number.\n")

        return validated

    def read_member_id(self):
        validated = False
        member_status = None

        self.member_id = valid.read_int("Enter the member's ID number: ")

        while len(str(self.provider_id)) != PROVIDER_ID_LENGTH:
            print(f"Please enter a 9-digit number.\n")
            self.provider_id = valid.read_int("Enter the member's ID number: ")

        #member_status = self.database.mem_get_status(self.member_id)        

        """
        if member_status is "validated":
            print("\nValidated")
            validated = True
    
        elif member_status is "suspended":
            print("\nMember suspended\n")

        else:
            print("\nInvalid Number.\n")

        """
        return validated

    def find_service_code(self):
        pass

    def generate_bill(self) -> None:
        pass

    def log_service(self) -> None:
        pass
