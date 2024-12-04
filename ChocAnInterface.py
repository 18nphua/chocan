"""
File: ChocAnInterface.py
Name: Nicholas Phua 
Desc: This is the Interface Class which will work as an interface between 
      the user and the manager/provider classes.

"""
import valid 
import provider as prov

from ChocAnServiceCoordinator import *

class chocan_interface():
    def __init__(self):
        #user_cord = chocan_service_cord()
        self.user_input = 0
        self.provider = prov.Provider()

    #Menu that shows up on startup
    def start_menu(self):
        term_choice = 0

        while(term_choice != 3):
            print("ChocAn System\n")
            #print("Please choose which terminal to use\n")
            print("1. Provider Terminal"
                  "\n2. Manager Terminal"
                  "\n3. Quit\n")
            term_choice = valid.read_int("Please choose which terminal to use: ")
            
            if (term_choice == 1):
                if(self.provider.read_provider_id() == True):
                    self.provider_menu()

            elif (term_choice == 2):
                self.manager_menu()

            elif (term_choice < 1 or term_choice > 3):
                print("\nInvalid choice selected.")

    #Provider menu this will work with the provider class
    def provider_menu(self):
        prov_choice = 0
        while (prov_choice != 5):
            print("Provider Menu\n")
            print("1. Verify Member ID"
                  "\n2. Look Up Service Code"
                  "\n3. Generate Bill"
                  "\n4. Log Service"
                  "\n5. Quit"
                )

            if (prov_choice == 1):
                self.provider.read_member_id()

            elif (prov_choice == 2):
                self.provider.find_service_code()

            elif (prov_choice == 3):
                self.provider.generate_bill()
  
            elif (prov_choice == 4): 
                self.provider.log_service()

            elif (prov_choice < 1 or prov_choice > 5):
                print("\nInvalid choice selected.")


    
    #Manager menu this will work with the provider class
    def manager_menu(self):
        print("This is a test for the manager menu")


    def main(self):
        print("Hello this is the start of chocant")
        print("Hello this is a test.")
        self.start_menu()

if __name__ == "__main__":
    user_menu = chocan_interface()
    user_menu.main()
