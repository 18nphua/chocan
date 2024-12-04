"""
File: Provider.py
Name: Huan Nguyen 
Desc: This file contains the Provider class, which will manage all provider-specific information
      and operations for the ChocAn system.

"""
import valid 
import DatabaseApi as db
import datetime

MEMBER_ID_LENGTH = 9
SERVICE_CODE_LENGTH = 5
COMMENT_MAX_LENGTH = 100

class Provider():
    def __init__(self) -> None:
        self.service_date = " "
        self.provider_id = 0
        self.member_id = 0
        self.service_date = None
        self.service_code = 0
        self.comments = ""
        self.database = db.db_client()

    def read_member_id(self) -> bool:
        member_is_valid = False
        member_status = None

        self.member_id = valid.read_int("Enter Member ID number: ")

        #Verifies the member ID entered is 9-digits long.
        while len(str(self.member_id)) != MEMBER_ID_LENGTH:
            print(f"Please enter a 9-digit number.\n")
            self.member_id = valid.read_int("Enter the Member ID number: ")

        #Obtains the status of the member associated with the 
        #specified member ID number.
        #member_status = self.database.mem_get_status(self.member_id)        

        #Displays the results of the database query.
        """
        if member_status is "good standing":
            print("\nValidated")
            member_is_valid = True
    
        elif member_status is "suspended":
            print("\nMember suspended\n")

        else:
            print("\nInvalid Number\n")

        """
        return member_is_valid

    def find_service_code(self) -> int:
        service_type = " "
        service_code = 0
    
        service_type = valid.read_string("Enter the provider role (e.g., dietitian, therapist): ")

        #Obtains the service corresponding to the specified service type.
        #service_code = self.database.get_service_code(service_type)

        #Displays the results of the database query.
        if service_code is 0:
            print("Invalid service type")
            
        else:
            print(f"Service Type: {service_type}    Service Code: {service_code}\n")
 
        return service_code

    def generate_bill(self) -> None:
        member_status = None
        date_is_valid = False
        service_type_is_valid = False
        service_is_correct = 'n'
        comment_is_approved = 'n'
        now = datetime.datetime.now()
        formatted_date = " "
 
        self.member_id = valid.read_int("Enter Member ID number: ")

        while len(str(self.member_id)) != MEMBER_ID_LENGTH:
            print(f"Please enter a 9-digit number.\n")
            self.member_id = valid.read_int("Enter the Member ID number: ")
 
        #member_status = self.database.mem_get_status(self.member_id)        

        """
        if member_status is "good standing":
            print("\nValidated")        
 
            while date_is_valid is False:
                self.service_date = valid.read_string("\nEnter a date (MM-DD-YYYY): ")
                try:
                    date = datetime.datetime.strptime(self.service_date, "%m-%d-%Y")
                    date_is_valid = True

                except ValueError:
                    print("Invalid date format. Please use MM-DD-YYYY")

            #Repeatedly prompts the provider to enter the type of the service that was provided
            #until they indicate the information returned is correct     
            while service_is_correct == 'n':
                while (self.service_code = self.find_service_code()) == 0: 
                service_is_correct = valid.read_y_or_n("Is the above information correct? Please enter 'n' or 'y': ") 

            #Repeatedly prompts the provider to write a comment until they either indicate they are done or no 
            #longer wish to provide a comment with the bill.
            while comment is approved == 'n' and valid.read_y_or_n("Would you like write a comment? Please enter 'n' or 'y': ") == 'y':
                self.comments = valid.read_string("Please enter your comments below\n")

                #Ensures the comment is 100 characters or fewer.
                while len(str(self.comments)) != COMMENT_MAX_LENGTH:
                    print(f"Please keep your comments at 100 characters or fewer (including whitespaces).\n")
                    self.comments = valid.read_string("Please enter your comment below\n")

                #Displays what was written.
                print(f"\"{self.comments}\"")
                comment_is_approved = read_y_or_n("\nDoes the comment you wrote look correct? Please enter 'n' or 'y': ")

            #Writes information to disk.
            #Obtains the current time.
            formatted_date = now.strftime("%m-%d-%Y %H:%M:%S")

        elif member_status is "suspended": 
            print("Unable to generate a bill. The specified Member ID is suspended.")

        else: 
            print("Member ID not specified. Please enter a valid Member ID to generate a bill.")
        
        """ 
 
        return

    def log_service(self) -> None:
        pass
