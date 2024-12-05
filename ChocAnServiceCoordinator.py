'''
File: ChocAnServiceCoordinator.py
Name: Huan Nguyen
Desc: WIP
'''

import valid 
import DatabaseApi as db
import datetime

PHONE_NUM_LENGTH = 10
MEMBER_ID_LENGTH = 9
PROVIDER_ID_LENGTH = 9
SERVICE_CODE_LENGTH = 6
COMMENT_MAX_LENGTH = 100
ZIP_CODE_LENGTH = 5
class chocan_service_cord():
    #Manager functions
    def add_member(self) -> None:
        database = db.db_client()
        was_added = False

        name = valid.read_string("Enter the name of member: ")
        phone_num = valid.read_int("Enter the member's phone number: ")

        while len(str(phone_num)) != 10:
            print(f"Please enter a {PHONE_NUM_LENGTH}-digit phone number")
            phone_num = valid.read_int("Enter the member's phone number: ")

        street_address = valid.read_string("Enter the member's street address: ")
        city = valid.read_string("Enter the member's home city: ")
        state = valid.read_string("Enter the member's home state: ")

        zip_code = valid.read_int("Enter the member's zip code: ")

        while len(str(zip_code)) != ZIP_CODE_LENGTH:
            print(f"Please enter a {ZIP_CODE_LENGTH}-digit zip code") 
            zip_code = valid.read_int("Enter the member's zip code: ")

        if not all([name, phone_num, street_address, city, state, zip_code]):
            print("Error: All fields must be filled out.")
            return False

        if database.add_member(name, phone_num, street_address, city, state, zip_code) == True:
            print("Member was successfully added.")

        else:
            print("That member is already in the database.")

        return
    
    def edit_member(self):
        database = db.db_client()  
        
        member_id = valid.read_int("Enter Member ID number to edit: ")

        #Verifies the member ID entered is 9-digits long.
        while len(str(member_id)) != MEMBER_ID_LENGTH:
            print(f"Please enter a {MEMBER_ID_LENGTH}-digit number.\n")
            member_id = valid.read_int("Enter target ID number to edit: ")

        print("Member attributes: name, phone_number, street_address, city, state, zip_code")

        attribute = valid.read_string("Enter the name of the attribute you would like to edit: ")

        match attribute:
            case "name":
                value = valid.read_string("Enter a new name: ")

            case "phone_number":
                value = valid.read_int("Enter a new phone number: ")

                while len(str(value)) != 10:
                    print(f"Please enter a {PHONE_NUM_LENGTH}-digit phone number")
                    value = valid.read_int("Enter a new phone number: ")

            case "street_address":
                value = valid.read_string("Enter a new street address: ")

            case "city":
                value = valid.read_string("Enter a city name (ex: Portland): ")

            case "state":
                value = valid.read_string("Enter a state name (ex: Oregon): ")

            case "zip_code":
                value = valid.read_int(f"Enter a new zip code ({ZIP_CODE_LENGTH} digits): ")

                while len(str(zip_code)) != ZIP_CODE_LENGTH:
                    print(f"Please enter a {ZIP_CODE_LENGTH}-digit zip code") 
                    zip_code = valid.read_int("Enter the member's zip code: ")

            case _:
                print("\nUnknown attribute")
                return
            
        if database.edit_member(member_id, value) == True:
            print(f"{attribute} has been updated for member with id {member_id}.")

        else:
            print("No edits were made.")

        return
        
    def remove_member(self) -> bool:
        database = db.db_client()
        was_removed = False

        member_id = valid.read_int("Enter Member ID number: ")

        #Verifies the member ID entered is 9-digits long.
        while len(str(member_id)) != MEMBER_ID_LENGTH:
            print(f"Please enter a {MEMBER_ID_LENGTH}-digit number.\n")
            member_id = valid.read_int("Enter the Member ID number: ")

        if database.remove_member(member_id) == True: 
            print("Member was successfully removed.")
            was_removed = True

        else:
            print("Member could not be found.")
 
        return was_removed

    def add_provider(self):
        database = db.db_client()
        was_added = False

        try:
            name = valid.read_string("Enter the name of provider: ")
            phone_num = valid.read_int("Enter the provider's phone number: ")

            while len(str(phone_num)) != 10:
                print(f"Please enter a {PHONE_NUM_LENGTH}-digit phone number")
                phone_num = valid.read_int("Enter the member's phone number: ")

            street_address = valid.read_string("Enter the provider's street address: ")
            city = valid.read_string("Enter the provider's home city: ")
            state = valid.read_string("Enter the provider's home state: ")

            zip_code = valid.read_int("Enter the provider's zip code: ")

            while len(str(zip_code)) != ZIP_CODE_LENGTH:
                print(f"Please enter a {ZIP_CODE_LENGTH}-digit zip code") 
                zip_code = valid.read_int("Enter the provider's zip code: ")

            if database.add_member(name, phone_num, street_address, city, state, zip_code) == True:
                print("Member was successfully added.")

            else:
                print("That member is already in the database.")

            if not all([name, phone_num, street_address, city, state, zip_code]):
                print("Error: All fields must be filled out.")
                return False

            was_added = database.add_provider(name, phone_num, street_address, city, state, zip_code)

            if was_added:
                print("Provider was successfully added.\n")
            else:
                print("That provider is already in the database..\n")

            return was_added

        except Exception as e:
            print(f"An error occurred while adding the provider: {e}")
            return False


    def remove_provider(self):
        database = db.db_client()
        was_removed = False

        try:
            provider_id = valid.read_int("Enter Provider ID number: ")

            # Verifies the provider ID entered is 9-digits long.
            while len(str(provider_id)) != PROVIDER_ID_LENGTH:
                print(f"Please enter a {PROVIDER_ID_LENGTH}-digit number.\n")
                provider_id = valid.read_int("Enter Provider ID number: ")

            was_removed = database.remove_provider(provider_id)

            if was_removed:
                print("Provider has been removed!\n")
            else:
                print("Provider has not been removed!\n")

        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except Exception as e:
            print(f"An error occurred while removing the provider: {e}")


    def edit_provider(self):
        database = db.db_client()
        was_edited = False

        try:
            provider_id = valid.read_int("Enter Provider ID number to edit: ")

            # Verifies the provider ID entered is 9-digits long.
            while len(str(provider_id)) != PROVIDER_ID_LENGTH:
                print(f"Please enter a {PROVIDER_ID_LENGTH}-digit number.\n")
                provider_id = valid.read_int("Enter the Provider ID number: ")

            print("Provider attributes: name, phone_number, street_address, city, state, zip_code")

            attribute = valid.read_string("Enter the name of the attribute you would like to edit: ")

            match attribute:
                case "name":
                    value = valid.read_string("Enter a new name: ")

                case "phone_number":
                    value = valid.read_int("Enter a new phone number: ")

                    while len(str(value)) != 10:
                        print(f"Please enter a {PHONE_NUM_LENGTH}-digit phone number")
                        value = valid.read_int("Enter a new phone number: ")

                case "street_address":
                    value = valid.read_string("Enter a new street address: ")

                case "city":
                    value = valid.read_string("Enter a city name (ex: Portland): ")

                case "state":
                    value = valid.read_string("Enter a state name (ex: Oregon): ")

                case "zip_code":
                    value = valid.read_int(f"Enter a new zip code ({ZIP_CODE_LENGTH} digits): ")

                    while len(str(zip_code)) != ZIP_CODE_LENGTH:
                        print(f"Please enter a {ZIP_CODE_LENGTH}-digit zip code") 
                        zip_code = valid.read_int("Enter the member's zip code: ")

                case _:
                    print("\nUnknown attribute")
                    return
            
            if database.edit_member(provider_id, value) == True:
                print(f"{attribute} has been updated for provider with id {provider_id}.")
                was_edited = True

            else:
                print("No edits were made.")

        except ValueError as ve:
            print(f"Invalid input: {ve}")
            return False

        except Exception as e:
            print(f"An error occurred while editing the provider: {e}")
            return False
    
        return was_edited

    def generate_weekly_report():
        pass

    #Provider functions
    def read_member_id(self) -> bool:
        member_is_valid = False
        member_status = None
        member_id = 0

        member_id = valid.read_int("Enter Member ID number: ")

        #Verifies the member ID entered is 9-digits long.
        while len(str(member_id)) != MEMBER_ID_LENGTH:
            print(f"Please enter a {MEMBER_ID_LENGTH}-digit number.\n")
            member_id = valid.read_int("Enter the Member ID number: ")

        #Obtains the status of the member associated with the 
        #specified member ID number.
        member_status = database.get_member_status(member_id)        

        #Displays the results of the database query.
        if member_status == "good standing":
            print("\nValidated")
            member_is_valid = True
    
        elif member_status == "suspended":
            print("\nMember suspended\n")

        else:
            print("\nInvalid Number\n")

        return member_is_valid

    def find_service_code(self) -> int:
        service_name = " "
        service_code = 0
        database = db.db_client()
    
        service_name = valid.read_string("Enter the provider role (e.g., dietitian, therapist): ")

        #Obtains the service corresponding to the specified service type.
        service_code = database.serv_get_code_from_name(service_name)

        #Displays the results of the database query.
        if service_code == 0:
            print("Invalid service type")
            
        else:
            print(f"Service Type: {service_name}    Service Code: {service_code}\n")
 
        return service_code

    def generate_bill(self) -> None:
        member_id = 0
        service_date = " "
        service_code = 0
        comments = " "

        member_status = None
        date_is_valid = False
        service_is_correct = 'n'
        comment_is_approved = 'n'
        now = datetime.datetime.now()
        formatted_date = " "

        database =  db.db_client()
        member_id = valid.read_int("Enter Member ID number: ")

        while len(str(member_id)) != MEMBER_ID_LENGTH:
            print(f"Please enter a {MEMBER_ID_LENGTH}-digit number.\n")
            member_id = valid.read_int("Enter the Member ID number: ")
 
        member_status = database.get_member_status(member_id)        

        if member_status == "good standing":
            print("\nValidated")        
 
            while date_is_valid == False:
                service_date = valid.read_string("\nEnter a date (MM-DD-YYYY): ")
                try:
                    datetime.datetime.strptime(service_date, "%m-%d-%Y")
                    date_is_valid = True

                except ValueError:
                    print("Invalid date format. Please use MM-DD-YYYY")

            #Repeatedly prompts the provider to enter the type of the service that was provided
            #until they indicate the information returned is correct     
            while service_is_correct == 'n':

                service_code = self.find_service_code()

                while service_code == 0: 
                    service_code = self.find_service_code()

                service_is_correct = valid.read_y_or_n("Is the above information correct? Please enter 'n' or 'y': ") 

            #Repeatedly prompts the provider to write a comment until they either indicate they are done or no 
            #longer wish to provide a comment with the bill.
            while comment_is_approved == 'n' and valid.read_y_or_n("Would you like write a comment? Please enter 'n' or 'y': ") == 'y':
                comments = valid.read_string("Please enter your comments below\n")

                #Ensures the comment is 100 characters or fewer.
                while len(str(comments)) != COMMENT_MAX_LENGTH:
                    print(f"Please keep your comments at 100 characters or fewer (including whitespaces).\n")
                    comments = valid.read_string("Please enter your comment below\n")

                #Displays what was written.
                print(f"\"{comments}\"")
                comment_is_approved = valid.read_y_or_n("\nDoes the comment you wrote look correct? Please enter 'n' or 'y': ")

            #Writes information to disk.
            #Obtains the current time.
            formatted_date = now.strftime("%m-%d-%Y %H:%M:%S")

            print("Bill sent.")

        elif member_status == "suspended": 
            print("Unable to generate a bill. The specified Member ID is suspended.")

        else: 
            print("Member ID not specified. Please enter a valid Member ID to generate a bill.")
        
        return
    
    def generate_member_report():
        pass 

    def log_service(self) -> None:
        pass

test = chocan_service_cord()
database = db.db_client()

prov_id = database.prov_get_name_from_id(20000002)

print(prov_id)
# test.add_provider()
test.edit_provider()