'''
File: ChocAnServiceCoordinator.py
Name: Huan Nguyen
Desc: This file contains the chocan_service_cord() class, which will manage a
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
    def __init__(self):
        self.user_id = 0
        self.database = db.db_client()

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
        database = db.db_client()
        member_is_valid = False
        member_status = None
        member_id = 0
        database = db.db_client()

        member_id = valid.read_int("Enter Member ID number: ")

        #Verifies the member ID entered is 9-digits long.
        while len(str(member_id)) != MEMBER_ID_LENGTH:
            print(f"Please enter a {MEMBER_ID_LENGTH}-digit number.\n")
            member_id = valid.read_int("Enter the Member ID number: ")
        
        #Obtains the status of the member associated with the 
        #specified member ID number.
        member_status = database.mem_get_status_from_id(member_id)      

        #Displays the results of the database query.
        if member_status == "VALIDATED":
            print("\nValidated.")
            member_is_valid = True
    
        elif member_status == "SUSPENDED":
            print("\nMember suspended\n")

        else:
            print("\nMember not found\n")

        return member_is_valid

    def find_service_code(self) -> int:
        service_name = " "
        service_code = 0
        database = db.db_client()
    
        service_name = valid.read_string("Enter the Service name (or type all, 0 to exit): ")

        #Obtains the service corresponding to the specified service type.
        
        if service_name.upper() == 'ALL':
            result = database.serv_get_all_services()

            for service in result:
                print(f"Service Name: {service[1]}")
                print(f"\tService Code: {database.serv_get_code_from_name(service[1])}")
            return None
        
        service_code = database.serv_get_code_from_name(service_name)

        #Displays the results of the database query.
        if service_code == None:
            print("Invalid service")
        else:
            print(f"Service Name: {service_name}    Service Code: {service_code}\n")
 
        return service_code

    def generate_bill(self) -> None:
        path = "reports/"
        database =  db.db_client()
        member_id = valid.read_int("Enter the Member ID number: ")
        timecode = datetime.datetime.now().strftime("%m-%d-%Y")

        while len(str(member_id)) != MEMBER_ID_LENGTH:
            print(f"Please enter a {MEMBER_ID_LENGTH}-digit number.\n")
            member_id = valid.read_int("Enter the Member ID number: ")

        member = database.mem_get_name_from_id(member_id)
        if not member:
            print("Member not found. Aborting.")
            return
        
        result = database.generate_report('member_weekly', member_id)
        
        if result:
            with open(f'{path}{member.replace(' ', '_')}_{timecode}.txt', 'w') as file:
                count = 1
                total_cost = 0
                current_balance = database.mem_get_balance_from_id(member_id)
                
                # Do the writing
                file.write(f'Name: {member}\t\tGenerated on: {timecode}\n')
                file.write('======================================================\n')
                file.write(f'{'service':<10}{'service_name':<30}{'date_service_logged':<25}{'date_service_provided':<25}{'provider_id':<25}{'member_id':<25}{'member_name':<25}{'fee':<25}\n\n')
                for service in result:
                    total_cost = total_cost + service[6]
                    mem_id = database.clean_id(member_id, database.MEMBER_ID_RANGE)
                    prov_id = database.clean_id(service[2], database.PROVIDER_ID_RANGE)
                    
                    file.write(f'{str(count) + '.':<10}{database.serv_get_name_from_code(service[5]):<30}')
                    file.write(f'{service[0]:<25}')
                    file.write(f'{service[1]:<25}')
                    file.write(f'{database.clean_id(service[2], database.PROVIDER_ID_RANGE):<25}')
                    file.write(f'{database.clean_id(service[3], database.MEMBER_ID_RANGE):<25}')
                    file.write(f'{service[4]:<25}')
                    file.write(f'${service[6]:.2f}')
                    file.write('\n')
                    count = count + 1
                
                current_balance = current_balance + total_cost
                file.write('======================================================\n')
                file.write(f"\nTOTAL: ${total_cost:.2f}   TOTAL SERVICES PROVIDED: {count}   CURRENT BALANCE: ${current_balance:.2f}")
            file.close()

            print(f"\nReport Written to: {path}{member_id}_{timecode}.txt\n")


    def log_service(self) -> None:
        service_code_valid = False
        date_provided = input("Date Service was Provided (format: YYYY/MM/DD): ")

        s_code = -1
        member_id = valid.read_int("Enter the Member ID number: ")
        while len(str(member_id)) != MEMBER_ID_LENGTH:
            print(f"Please enter a {MEMBER_ID_LENGTH}-digit number.\n")
            member_id = valid.read_int("Enter the Member ID number: ")

        member = self.database.mem_get_name_from_id(member_id)
        if not member:
            print("Member not found. Aborting.")
            return
        while service_code_valid == False:
            while len(str(s_code)) != SERVICE_CODE_LENGTH:
                print(f"Please enter a {SERVICE_CODE_LENGTH}-digit number.")
                print("     Type 0 to exit\n")
                s_code = input("Enter service code (or type 'all' to view codes available): ")

                if s_code == 'all':
                    result = self.database.serv_get_all_services()
                    for service in result:
                        temp_code = self.database.clean_id(service[0], self.database.SERVICE_CODE_RANGE)
                        print(f'Service Code: {temp_code}   Service Name: {service[1]} Fee: ${service[2]:.2f}')
                if s_code == '0':
                    return
            
            s_name = self.database.serv_get_name_from_code(int(s_code))
            if s_name:
                s_fee = self.database.serv_get_fee_from_service_code(int(s_code))
                if not s_fee:
                    return

                if self.database.log_service(datetime.datetime.now(), datetime.datetime.strptime(date_provided, "%Y/%m/%d"), self.user_id, member_id - self.database.MEMBER_ID_RANGE, int(s_code)):
                    print("Logged successfully.")
                else:
                    print("An error has occured. Aborting")
                return
            else:
                print("Service code not found. Try again.")
                s_code = -1
        pass