from ChocAnProvider import *
from ChocAnManager import *

class chocan_interface():
    def __init__(self):
        self.user_input = 0

    #Menu that shows up on startup
    def start_menu(self):
        pass

    def provider_menu(self):
        pass
    
    def manger_menu(self):
        pass


    def main(self):
        print("Hello this is the start of chocant")
        print("Hello this is a test.")
        self.start_menu()

if __name__ == "__main__":
    user_menu = chocan_interface()
    user_menu.main()
