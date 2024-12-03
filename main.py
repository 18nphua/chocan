
import provider as prov
import DatabaseApi as db
import ChocAnInterface as ui
def main():
    database = db.db_client()
    #provider = prov.Provider()
    menu = ui.chocan_interface()

    menu.start_menu()    



if __name__ == "__main__":
    main()