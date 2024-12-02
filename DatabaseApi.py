"""
File: sql_api.py
Name: Jordan Dexter
Desc: This file defines the functionality of the mySQL api used by chocan to enable standerized communication
      between providers and managers with the various databases found in Chocan network.
"""

import sqlite3

class db_client():
    def __init__(self):
        # Initalize connection to each db
        self.member_db      = sqlite3.connect('members.db')
        self.provider_db    = sqlite3.connect('providers.db')
        self.spl_db         = sqlite3.connect('services_provided_log.db')

        # Initialize a cursor for each db
        self.mem_cur        = self.member_db.cursor()
        self.provider_cur   = self.provider_db.cursor()
        self.spl_cur        = self.spl_db.cursor()
    
    # MEMBER FUNCTIONALITY

    #this function will be used to add new members to the database,
    #along with stopping from making duplicate members. Returns true if a 
    #new member was added to the database, false otherwise.
    def add_member(self,
                   name: str,
                   phone_number : int,
                   street_address: str,
                   city: str,
                   state : str,
                   zip_code : int):

        #check if there exists a member with the same name, phone number, street adress, etc.
        #to prevent duplications of members in the database.
        self.mem_cur.execute("""SELECT EXISTS (SELECT 1 FROM members WHERE name = ? 
                                AND phone_number = ? AND street_address = ? 
                                AND city = ? AND state = ? AND zip_code = ?)""", 
                                (name, phone_number, street_address, city, state, zip_code))
        
        if self.mem_cur.fetchone()[0] == 0:#if person doesn't exist in the database -> add to database
            #add the member to the data base
            result = self.mem_cur.execute(f"""INSERT INTO members (id, name, phone_number, street_address, city, state, zip_code) VALUES 
                ( NULL, '{name}', {phone_number}, '{street_address}', '{city}', '{state}', {zip_code});
                """)
            self.mem_cur.execute("COMMIT")

            return True# a new entry was added
        
        #if the person deos already exist in the database then don't add
        return False #no new entries was added
    
    
    def print_members(self):
        result = self.mem_cur.execute("SELECT * FROM members")
        print(result.fetchall())
    

    #the function requires three parameters, the target member(using ID), the value that will be
    #changed(attribute, example is name) and the parameter value is what will be used to replace
    #the old value. Returns true if a change happended and false if nothing was changed.
    def edit_member(self, target_id : int, attribute : str, value):
        # match case
        match attribute:
            # change ID
            case "id_num":
                self.mem_cur.execute("UPDATE members SET id_num = ? WHERE id_num = ?", (value, target_id))

                # change name
            case "name":
                self.mem_cur.execute("UPDATE members SET name = ? WHERE id_num = ?", (value, target_id))

                # change phone number
            case "phone_number":
                self.mem_cur.execute("UPDATE members SET phone_number = ? WHERE id_num = ?", (value, target_id))

                # change steet address
            case "street_address":
                self.mem_cur.execute("UPDATE members SET street_address = ? WHERE id_num = ?", (value, target_id))

                # change city
            case "city":
                self.mem_cur.execute("UPDATE members SET city = ? WHERE id_num = ?", (value, target_id))

                # change state
            case "state":
                self.mem_cur.execute("UPDATE members SET state = ? WHERE id_num = ?", (value, target_id))

                # change zip code
            case "zip_code":
                self.mem_cur.execute("UPDATE members SET zip_code = ? WHERE id_num = ?", (value, target_id))
            case _:
                print("Unkown attribute")
                return False#nothing was changed

        #this determines wether or not the database actually edited a member or not
        if self.mem_cur.rowcount == 0:#didn't change
            return False
        else:
            return True#a member was edited
    

    #the function will remove the member that has the same id as member_ID, will return true if removed
    # or false if nothing was removed. One small problem with this function is that it will remove all
    #members with the same ID, however this shouldn't be a problem since all members have a unique ID.
    def remove_member(self, member_ID):
        #delete the member from the database
        self.mem_cur.execute("DELETE FROM members WHERE id_num = ?", (member_ID,))
            
        #this determines wether or not the database actually removed a member or not
        if self.mem_cur.rowcount == 0:#didn't change, no members removed
            return False
        else:
            return True#a member was removed
        
    
    # PROVIDER FUNCTIONALITY
    def add_provider(self,
                   name: str,
                   phone_number : str,
                   street_address: str,
                   city: str,
                   state : str,
                   zip_code : int):

        id_num = 1 # self.gen_id()

        result = self.mem_cur.execute(f"""INSERT INTO providers VALUES 
                ({id_num}, '{name}', {phone_number}, '{street_address}', '{city}', '{state}', {zip_code});
                """)
        return
    
    def edit_provider(self, attribute : str, value):
        # to implement
        return
    
    def remove_provider(self, name):
        # to implement
        return
    
    def generate_report(self, report_type : str, path):
        # to implement
        return