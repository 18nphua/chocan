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
        path = "database"
        self.member_db      = sqlite3.connect(f'{path}/members.db')
        self.provider_db    = sqlite3.connect(f'{path}/providers.db')
        self.spl_db         = sqlite3.connect(f'{path}/services_provided_log.db')

        # Initialize a cursor for each db
        self.mem_cur        = self.member_db.cursor()
        self.provider_cur   = self.provider_db.cursor()
        self.spl_cur        = self.spl_db.cursor()
    
    #################################### MEMBER FUNCTIONALITY ###################################

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
                # change name
            case "name":
                self.mem_cur.execute("UPDATE members SET name = ? WHERE id = ?", (value, target_id))

                # change phone number
            case "phone_number":
                self.mem_cur.execute("UPDATE members SET phone_number = ? WHERE id = ?", (value, target_id))

                # change steet address
            case "street_address":
                self.mem_cur.execute("UPDATE members SET street_address = ? WHERE id = ?", (value, target_id))

                # change city
            case "city":
                self.mem_cur.execute("UPDATE members SET city = ? WHERE id = ?", (value, target_id))

                # change state
            case "state":
                self.mem_cur.execute("UPDATE members SET state = ? WHERE id = ?", (value, target_id))

                # change zip code
            case "zip_code":
                self.mem_cur.execute("UPDATE members SET zip_code = ? WHERE id = ?", (value, target_id))
            case _:
                print("Unkown attribute")
                return False#nothing was changed

        #this determines wether or not the database actually edited a member or not
        if self.mem_cur.rowcount == 0:#didn't change
            return False
        else:
            return True #a member was edited
    

    #the function will remove the member that has the same id as member_ID, will return true if removed
    # or false if nothing was removed. One small problem with this function is that it will remove all
    #members with the same ID, however this shouldn't be a problem since all members have a unique ID.
    def remove_member(self, member_ID):
        #validate member_ID
        if not isinstance(member_ID, int):
            if isinstance(member_ID, str):#if its a string then convert to a int
                member_ID = int(member_ID)
            else:
                return False
            
        #delete the member from the database
        self.mem_cur.execute("DELETE FROM members WHERE id = ?", (member_ID,))
            
        #this determines wether or not the database actually removed a member or not
        if self.mem_cur.rowcount == 0:#didn't change, no members removed
            return False
        else:
            self.mem_cur.execute("COMMIT")#save the change
            return True#a member was removed
        
    #################################### END  ###################################


    ########################### PROVIDER FUNCTIONALITY ##########################
    def add_provider(self,
                   name: str,
                   phone_number : str,
                   street_address: str,
                   city: str,
                   state : str,
                   zip_code : int):

         #Similarly to add_member, check if there exists a provider with the same name, phone number, street adress, etc.
        #to prevent duplications of providers in the database.
        self.provider_cur.execute("""SELECT EXISTS (SELECT 1 FROM providers WHERE name = ? 
                                AND phone_number = ? AND street_address = ? 
                                AND city = ? AND state = ? AND zip_code = ?)""", 
                                (name, phone_number, street_address, city, state, zip_code))
        
        if self.provider_cur.fetchone()[0] == 0:#if provider doesn't exist in the database -> add to database
            #add the provider to the data base
            result = self.provider_cur.execute(f"""INSERT INTO providers (id, name, phone_number, street_address, city, state, zip_code) VALUES 
                ( NULL, '{name}', {phone_number}, '{street_address}', '{city}', '{state}', {zip_code});
                """)
            self.provider_cur.execute("COMMIT")

            return True# a new entry was added
        
        #if the person deos already exist in the database then don't add
        return False #no new entries was added
    
    def edit_provider(self, target_id : int, attribute : str, value):
        # match case
        match attribute:
            case "name":
                self.provider_cur.execute("UPDATE providers SET name = ? WHERE id = ?", (value, target_id))

                # change phone number
            case "phone_number":
                self.provider_cur.execute("UPDATE providers SET phone_number = ? WHERE id = ?", (value, target_id))

                # change steet address
            case "street_address":
                self.provider_cur.execute("UPDATE providers SET street_address = ? WHERE id = ?", (value, target_id))

                # change city
            case "city":
                self.provider_cur.execute("UPDATE providers SET city = ? WHERE id = ?", (value, target_id))

                # change state
            case "state":
                self.provider_cur.execute("UPDATE providers SET state = ? WHERE id = ?", (value, target_id))

                # change zip code
            case "zip_code":
                self.provider_cur.execute("UPDATE providers SET zip_code = ? WHERE id = ?", (value, target_id))
            case _:
                print("Unkown attribute")
                return False#nothing was changed
    
    #the function will remove the provider that has the same id as provider_ID, will return true if removed
    # or false if nothing was removed. One small problem with this function is that it will remove all
    #members with the same ID, however this shouldn't be a problem since all members have a unique ID.
    def remove_provider(self, provider_ID):
        #validate provider_ID
        if not isinstance(provider_ID, int):
            if isinstance(provider_ID, str):#if its a string then convert to a int
                provider_ID = int(provider_ID)
            else:
                return False
            
        #delete the provider from the database
        self.provider_cur.execute("DELETE FROM providers WHERE id = ?", (provider_ID,))
            
        #this determines wether or not the database actually removed a provider or not
        if self.provider_cur.rowcount == 0:#didn't change, no provider removed
            return False
        else:
            self.provider_cur.execute("COMMIT")#save the change
            return True#a provider was removed
        
    #################################### END  ##################################


     ################################### REPORTS AND MISCELLANEOUS ###################################

    def mem_get_id_from_name(self, member_name : str):
        result = self.mem_cur.execute(f'SELECT id FROM members WHERE name="{member_name}"')
        id_val = 10000 + result.fetchone()[0]

        if id_val:
            return id_val
        return None
    
    def mem_get_name_from_id(self, member_id_num : int):
        member_id_num = member_id_num - 10000
        result = self.mem_cur.execute(f'SELECT name FROM members WHERE id={member_id_num}')

        name_val = result.fetchone()[0]

        if name_val:
            return name_val
        return None
    
    def prov_get_name_from_id(self, provider_id_num : int):
        member_id_num = member_id_num - 10000
        result = self.provider_cur.execute(f'SELECT name FROM providers WHERE id={provider_id_num}')
        name_val = result.fetchone()[0]

        if name_val:
            return name_val
        return None
    
    def prov_get_id_from_name(self, provider_name : str):
        result = self.provider_cur.execute(f'SELECT id FROM providers WHERE name="{provider_name}"')
        id_val = 10000 + result.fetchone()[0]

        if id_val:
            return id_val
        return None

    def prov_get_all(self, provider_num : int):
        result = self.provider_cur.execute(f'SELECT * FROM providers WHERE id="{provider_num}"')
        r = result.fetchone()

        if r:
            return r
        return None
    def get_fee_from_service_code(self, service_code):
        # to implement
        return 1.00
    
    def log_service(self, current_date_time : str,
                     date_service_provided : str, 
                     provider_id_num : int, 
                     member_id_num : int, 
                     service_code : int):
        
        member_name = self.mem_get_name_from_id(member_id_num)
        fee = self.get_fee_from_service_code(service_code)

        print()
        result = self.spl_cur.execute(f"""INSERT INTO services_provided_log(date_service_provided, date_service_logged, provider_id, member_id, member_name, service_code, fee) VALUES
                                      ("{current_date_time}", "{date_service_provided}", {provider_id_num}, {member_id_num}, "{member_name}", {service_code}, {fee} )""")
        result = self.spl_cur.execute(f'COMMIT')

        return

    def generate_report(self, report_type, id_num : int):
        if report_type == "member_weekly":
            result = self.spl_cur.execute(f'SELECT * FROM services_provided_log WHERE member_id={id_num}')
            return result.fetchall()
        if report_type == "provider_weekly":
            # To implement
            return None
        if report_type == "all_services_weekly":
            # To implement
            return None
        return

    #calculates the total fees the member made from all the services
    def calculate_member_fees(self, member_ID) -> float:
        #get all service_logs where the member ID is the same as member_ID
        service_list = self.spl_cur.execute("""SELECT fee FROM services_provided_log
                                                WHERE member_id = ?""", (member_ID,))
        service_list = self.spl_cur.fetchall()

        total_fee = float(0)#make a varaible to be used as the return of all the fees combined
        for i in total_fee:#iterate through each service_log
            total_fee += service_list[0]

        return total_fee


    #calculate the total balance for the provider from all the services they provided
    #returns the total balance that ChocAn owes them.
    def calculate_provider_balances(self, provider_ID) -> float:
        #get all service_logs where the provider ID is the same as provider_ID
        service_list = self.spl_cur.execute("""SELECT fee FROM services_provided_log
                                                WHERE provider_id = ?""", (provider_ID,))
        service_list = self.spl_cur.fetchall()

        total_balance = float(0)#make a varaible to be used as the return of all the fees combined
        for i in total_balance:#iterate through each service_log
            total_balance += service_list[0]

        return total_balance


    #gets the status of whether or not the member's account is active.
    def member_status(self, target_ID) -> bool:
        #to implement
        return True

    #changes the members balance by addition or subtraction.
    def deposit_member_balance(self, target_ID, amount: float):
        # to implement
        return

    #################################### END  ###################################