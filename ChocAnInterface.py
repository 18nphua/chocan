"""
File: ChocAnInterface.py
Name: Nicholas Phua 
Desc: This is the Interface Class which will work as an interface between 
      the user and the manager/provider classes.

"""
import valid as v
import provider as prov

from ChocAnServiceCoordinator import *

class chocan_interface():
    def __init__(self):
        #user_cord = chocan_service_cord()
        self.user_input = 0
        self.provider = prov.Provider()

    #Menu that shows up on startup
    def start_menu(self):
        term_choice = 1

        while(term_choice != 3):
            print("Welcome to the ChocAn Terminal!\n")
            #print("Please choose which terminal to use\n")
            print("1. Provider Terminal")
            print("2. Manager Terminal")
            print("3. Quit\n")
            term_choice = v.read_int("Please choose which terminal to use: ")
            
            if (term_choice == 1):
                if(self.provider.read_provider_id() == True):
                    self.provider_menu()
            elif (term_choice == 2):
                self.manager_menu()
            elif (term_choice < 1 or term_choice > 3):
                print("\nInvalid choice selected.")

    #Provider menu this will work with the provider class
    def provider_menu(self):
        prov_choice = 1
        while (prov_choice != 0):
            print("Welcome to the provider menu!")
            print("1. ")
        
    
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
