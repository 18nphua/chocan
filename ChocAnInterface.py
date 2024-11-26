"""
File: ChocAnInterface.py
Name: Nicholas Phua 
Desc: This is the Interface Class which will work as an interface between 
      the user and the manager/provider classes.

"""
from ChocAnServiceCoordinator import *

class chocan_interface():
    def __init__(self):
        user_cord = chocan_service_cord()
        self.user_input = 0

    #Menu that shows up on startup
    def start_menu(self):
        pass

    #Provider menu this will work with the provider class
    def provider_menu(self):
        pass
    
    #Manager menu this will work with the provider class
    def manager_menu(self):
        pass


    def main(self):
        print("Hello this is the start of chocant")
        print("Hello this is a test.")
        self.start_menu()

if __name__ == "__main__":
    user_menu = chocan_interface()
    user_menu.main()
