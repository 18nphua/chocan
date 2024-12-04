"""
File: Provider.py
Name: Huan Nguyen 
Desc: This file contains the Provider class, which will manage all provider-specific information
      and operations for the ChocAn system.

"""
import valid 
import DatabaseApi as db
import datetime

#PROVIDER_ID_LENGTH = 9
MEMBER_ID_LENGTH = 9
COMMENT_MAX_LENGTH = 100

class Provider():
    def __init__(self) -> None:
        self.service_date = " "
        self.provider_id = 0
        self.member_id = 0
        self.service_code = 0
        self.comments = ""
        self.database = db.db_client()

    """
    def read_provider_id(self) -> bool: 
        validated = False
        provider_name = None

        self.provider_id = valid.read_int("Please enter your provider ID number: ")

        while len(str(self.provider_id)) != PROVIDER_ID_LENGTH:
            print(f"Please enter a 9-digit number.\n")
            self.provider_id = valid.read_int("Please enter your Provider ID number: ")

        provider_name = self.database.prov_get_name_from_id(self.provider_id)        

        if provider_name is not None:
            print("Validated.")
            print(f"\nWelcome {provider_name}")
            validated = True

        else:
            print("\nInvalid Number.\n")

        return validated 
    """

    def read_member_id(self):
        validated = False
        member_status = None

        self.member_id = valid.read_int("Enter Member ID number: ")

        while len(str(self.member_id)) != MEMBER_ID_LENGTH:
            print(f"Please enter a 9-digit number.\n")
            self.member_id = valid.read_int("Enter the Member ID number: ")

        #member_status = self.database.mem_get_status(self.member_id)        

        """
        if member_status is "good standing":
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

        now = datetime.datetime.now()
        formatted_date = now.strftime("%m-%d-%Y %H:%M:%S")
        member_status = None

        self.member_id = valid.read_int("Enter Member ID number: ")

        while len(str(self.member_id)) != MEMBER_ID_LENGTH:
            print(f"Please enter a 9-digit number.\n")
            self.member_id = valid.read_int("Enter the Member ID number: ")
 
        #member_status = self.database.mem_get_status(self.member_id)        

        """
        if member_status is "good standing":
            print("\nValidated")

            
    
        elif member_status is "suspended": 
            print("Unable to generate a bill. The specified Member ID is suspended.")

        else: 
            print("Member ID not specified. Please enter a valid Member ID to generate a bill.")
            return

        """
 
        return


    def log_service(self) -> None:
        pass
