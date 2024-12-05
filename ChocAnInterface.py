"""
File: ChocAnInterface.py
Name: Nicholas Phua 
Desc: This is the Interface Class which will work as an interface between 
      the user and the manager/provider classes.
"""
import valid 
import DatabaseApi as db

from ChocAnServiceCoordinator import *

PROVIDER_ID_LENGTH = 9

class chocan_interface():
    def __init__(self):
        self.user_cord = chocan_service_cord()

    #Menu that shows up on startup
    def start_menu(self):
        terminal_choice = 0

        while(terminal_choice != 3):
            print("\n********** ChocAn System **********")
            #print("Please choose which terminal to use\n")
            print("1. Provider Terminal"
                  "\n2. Manager Terminal"
                  "\n3. Quit\n")
            terminal_choice = valid.read_int("Please choose which terminal to use: ")
            
            if (terminal_choice == 1):
                if(self.read_provider_id() == True):
                    self.provider_menu()

            elif (terminal_choice == 2):
                self.manager_menu()

            elif (terminal_choice < 1 or terminal_choice > 3):
                print("Invalid choice selected\n")
            
        
    def read_provider_id(self) -> bool: 
        validated = False
        provider_id = 0
        provider_name = None
        database = db.db_client()

        provider_id = valid.read_int("\nPlease enter your provider ID number: ")

        while len(str(provider_id)) != PROVIDER_ID_LENGTH:
            print(f"Please enter a {PROVIDER_ID_LENGTH}-digit number.\n")
            provider_id = valid.read_int("Please enter your Provider ID number: ")

        provider_name = database.prov_get_name_from_id(provider_id)        

        if provider_name != None:
            print("Validated.")
            print(f"\nWelcome {provider_name}")
            validated = True

        else:
            print("\nInvalid Provider Number\n")

        return validated

    #Allows users to view and select provider-specific actions.
    def provider_menu(self):
        prov_choice = 0
        
        while (prov_choice != 5):
            print("\n********** Provider Menu **********\n")
            print("1. Verify Member ID"
                  "\n2. Look Up Service Code"
                  "\n3. Generate Bill"
                  "\n4. Log Service"
                  "\n5. Quit\n"
                )

            prov_choice = valid.read_int("Please choose an option: ")

            if (prov_choice == 1):
                self.user_cord.read_member_id() #done

            elif (prov_choice == 2):
                self.user_cord.find_service_code()

            elif (prov_choice == 3):
                self.user_cord.generate_bill()
  
            elif (prov_choice == 4): 
                self.user_cord.log_service()

            elif (prov_choice < 1 or prov_choice > 5):
                print("\nInvalid choice selected.")


    
    #Manager menu this will work with the provider class
    def manager_menu(self):
        manager_choice = 0

        while (manager_choice != 8):
            print("\n********** Manager Menu **********\n")
            print("1. Add Member"
                  "\n2. Remove Member"
                  "\n3. Update Member Record"
                  "\n4. Add Provider"
                  "\n5. Remove Provider"
                  "\n6. Update Provider Record"
                  "\n7. Generate Report"
                  "\n8. Quit"
                )
            manager_choice = valid.read_int("Please choose an option: ")
            if(manager_choice == 1):
                self.user_cord.add_member()
            elif (manager_choice == 2):
                self.user_cord.remove_member()
            elif (manager_choice == 3):
                self.user_cord.edit_member()
            elif (manager_choice == 4):
                self.user_cord.add_provider()
            elif (manager_choice == 5):
                self.user_cord.remove_provider()
            elif (manager_choice == 6):
                self.user_cord.edit_provider()
            elif (manager_choice == 7):
                self.user_cord.generate_weekly_report()
            elif (manager_choice < 1 or manager_choice > 8):
                print("\nInvalid Option.")
