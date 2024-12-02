"""
File: Provider.py
Name: Huan Nguyen 
Desc: This file contains the Provider class, which will manage all provider-specific information
      and operations for the ChocAn system.

"""
import valid as v
import DatabaseApi as db

PROVIDER_NUM_LENGTH = 9

class Provider():
    def __init__(self) -> None:
        self.__provider_num = 0
        self.__name = " "
        self.__street = " "
        self.__city = " "
        self.__state = " "
        self.__zip_code = 0

    def read_provider_num(self, database: db.db_client) -> bool:
        self.__provider_num = v.read_int("Please enter your provider number: ")
        identity_verified = False

        while len(str(self.__provider_num)) != PROVIDER_NUM_LENGTH:
            print(f"Please enter a 9-digit number.\n")
            self.__provider_num = v.read_int("Please enter your provider number: ")

        #identity_verified = database.retrieve_provider_info(self)        
        
        return identity_verified

    def generate_bill(self) -> None:
        pass

    def log_service(self) -> None:
        pass
