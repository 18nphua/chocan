"""
File: sql_api.py
Name: Jordan Dexter
Desc: This file defines the functionality of the mySQL api used by chocan to enable standerized communication
      between providers and managers with the various databases found in Chocan network.
"""

import sqlite3
import datetime

class db_client():
    def __init__(self):
        # Initalize connection to each db
        path = "database"
        self.db = sqlite3.connect(f'{path}/chocan.db')
        self.cur = self.db.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")

        # Ranges
        self.MEMBER_ID_RANGE    = 100000000
        self.PROVIDER_ID_RANGE  = 200000000
        self.SERVICE_CODE_RANGE = 300000

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
        self.cur.execute("""SELECT EXISTS (SELECT 1 FROM members WHERE name = ? 
                                AND phone_number = ? AND street_address = ? 
                                AND city = ? AND state = ? AND zip_code = ?)""", 
                                (name, phone_number, street_address, city, state, zip_code))
        
        if self.cur.fetchone()[0] == 0:#if person doesn't exist in the database -> add to database
            #add the member to the data base
            result = self.cur.execute(f"""INSERT INTO members (id, name, phone_number, street_address, city, state, zip_code, last_payment_date, status, balance) VALUES 
                ( NULL, '{name}', {phone_number}, '{street_address}', '{city}', '{state}', {zip_code}, NULL, "VALIDATED", 0.00)
                """)
            self.cur.execute("COMMIT")

            return True# a new entry was added
        
        #if the person deos already exist in the database then don't add
        return False #no new entries was added
    
    
    def print_members(self):
        result = self.cur.execute("SELECT * FROM members")
        print(result.fetchall())
    

    #the function requires three parameters, the target member(using ID), the value that will be
    #changed(attribute, example is name) and the parameter value is what will be used to replace
    #the old value. Returns true if a change happended and false if nothing was changed.
    def edit_member(self, target_id : int, attribute : str, value):
        # attribute options: name, phone_number, street_address, city, state, zip_code
        # match case
        match attribute:
                # change name
            case "name":
                self.cur.execute("UPDATE members SET name = ? WHERE id = ?", (value, target_id))

                # change phone number
            case "phone_number":
                self.cur.execute("UPDATE members SET phone_number = ? WHERE id = ?", (value, target_id))

                # change steet address
            case "street_address":
                self.cur.execute("UPDATE members SET street_address = ? WHERE id = ?", (value, target_id))

                # change city
            case "city":
                self.cur.execute("UPDATE members SET city = ? WHERE id = ?", (value, target_id))

                # change state
            case "state":
                self.cur.execute("UPDATE members SET state = ? WHERE id = ?", (value, target_id))

                # change zip code
            case "zip_code":
                self.cur.execute("UPDATE members SET zip_code = ? WHERE id = ?", (value, target_id))
            case _:
                print("Unkown attribute")
                return False#nothing was changed

        #this determines wether or not the database actually edited a member or not
        if self.cur.rowcount == 0:#didn't change
            return False
        else:
            self.cur.execute("COMMIT")#save changes
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
        self.cur.execute("DELETE FROM members WHERE id = ?", (member_ID,))
            
        #this determines wether or not the database actually removed a member or not
        if self.cur.rowcount == 0:#didn't change, no members removed
            return False
        else:
            self.cur.execute("COMMIT")#save the change
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
        self.cur.execute("""SELECT EXISTS (SELECT 1 FROM providers WHERE name = ? 
                                AND phone_number = ? AND street_address = ? 
                                AND city = ? AND state = ? AND zip_code = ?)""", 
                                (name, phone_number, street_address, city, state, zip_code))
        
        if self.cur.fetchone()[0] == 0:#if provider doesn't exist in the database -> add to database
            #add the provider to the data base
            result = self.cur.execute(f"""INSERT INTO providers (id, name, phone_number, street_address, city, state, zip_code) VALUES 
                ( NULL, '{name}', {phone_number}, '{street_address}', '{city}', '{state}', {zip_code});
                """)
            self.cur.execute("COMMIT")

            return True# a new entry was added
        
        #if the person deos already exist in the database then don't add
        return False #no new entries was added
    
    def edit_provider(self, target_id : int, attribute : str, value):
        # attribute options: name, phone_number, street_address, city, state, zip_code
        # match case
        match attribute:
            case "name":
                self.cur.execute("UPDATE providers SET name = ? WHERE id = ?", (value, target_id))

                # change phone number
            case "phone_number":
                self.cur.execute("UPDATE providers SET phone_number = ? WHERE id = ?", (value, target_id))

                # change steet address
            case "street_address":
                self.cur.execute("UPDATE providers SET street_address = ? WHERE id = ?", (value, target_id))

                # change city
            case "city":
                self.cur.execute("UPDATE providers SET city = ? WHERE id = ?", (value, target_id))

                # change state
            case "state":
                self.cur.execute("UPDATE providers SET state = ? WHERE id = ?", (value, target_id))

                # change zip code
            case "zip_code":
                self.cur.execute("UPDATE providers SET zip_code = ? WHERE id = ?", (value, target_id))
            case _:
                print("Unkown attribute")
                return False#nothing was changed

        #this determines wether or not the database actually edited a provider or not
        if self.cur.rowcount == 0:#didn't change
            return False
        else:
            self.cur.execute("COMMIT")#save changes
            return True #a provider was edited

    
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
        self.cur.execute("DELETE FROM providers WHERE id = ?", (provider_ID,))
            
        #this determines wether or not the database actually removed a provider or not
        if self.cur.rowcount == 0:#didn't change, no provider removed
            return False
        else:
            self.cur.execute("COMMIT")#save the change
            return True#a provider was removed
        
    #################################### END  ##################################


     ################################### REPORTS AND MISCELLANEOUS ###################################

    # Finds member id given member name
    def mem_get_id_from_name(self, member_name : str):
        if not member_name:
            return None
        
        result = self.cur.execute(f'SELECT id FROM members WHERE name="{member_name}"')
        result = result.fetchone()
        
        if result:
            # the actual id value stored in the database is would like like "42", adding
            # the self.MEMBER_ID_RANGE is simply for padding the number to 9 digits
            return self.MEMBER_ID_RANGE + result[0]
        return None
    
    
    def mem_get_name_from_id(self, member_id_num : int):
        if not member_id_num:
            return None
        
        member_id_num = self.clean_id(member_id_num, self.MEMBER_ID_RANGE) - self.MEMBER_ID_RANGE
        result = self.cur.execute(f'SELECT name FROM members WHERE id={member_id_num}')
        name_val = result.fetchone()

        if name_val:
            return name_val[0]
        return None

    def mem_get_status_from_id(self, member_id_num):
        if not member_id_num:
            return None
        
        member_id_num = self.clean_id(member_id_num, self.MEMBER_ID_RANGE) - self.MEMBER_ID_RANGE
        result = self.cur.execute(f'SELECT status FROM members WHERE id={member_id_num}')
        status = result.fetchone()

        if status:
            return status[0]
        return None
    
    def mem_set_status_from_id(self, member_id_num : int, status : str):
        if not member_id_num:
            return True
        
        status = status.upper()
        if status != "VALIDATED" and status != "SUSPENDED":
            return False
        
        member_id_num = self.clean_id(member_id_num, self.MEMBER_ID_RANGE) - self.MEMBER_ID_RANGE
        self.cur.execute(f'UPDATE members SET status="{status}" WHERE id={member_id_num}')
        self.cur.execute(f'COMMIT')

        return True

    
    def prov_get_id_from_name(self, provider_name : str):
        result = self.cur.execute(f'SELECT id FROM providers WHERE name="{provider_name}"')
        result = result.fetchone()

        if result:
            return self.PROVIDER_ID_RANGE + result[0]
        return None
    
    def prov_get_name_from_id(self, provider_id_num : int):
        if not provider_id_num or provider_id_num <= 0:
            return None
        
        provider_id_num = self.clean_id(provider_id_num, self.PROVIDER_ID_RANGE)
        if not provider_id_num:
            return None
        provider_id_num = provider_id_num - self.PROVIDER_ID_RANGE
        result = self.cur.execute(f'SELECT name FROM providers WHERE id={provider_id_num}')
        name_val = result.fetchone()

        if name_val:
            return name_val
        return None

    def prov_get_all(self, provider_num : int):
        result = self.cur.execute(f'SELECT * FROM providers WHERE id="{provider_num}"')
        r = result.fetchone()

        if r:
            return r
        return None
    
    def serv_get_code_from_name(self, service_name : str):
        result = self.cur.execute(f'SELECT service_code FROM services WHERE UPPER(name)=UPPER("{service_name}")')
        result = result.fetchone()
        

        if result:
            return self.clean_id(result[0], self.SERVICE_CODE_RANGE)
        return None
    
    def serv_get_name_from_code(self, service_code : int):
        result = self.cur.execute(f'SELECT name FROM services WHERE service_code={service_code}')
        result = result.fetchone()

        if result:
            return result[0]
        return None
    
    def serv_get_all_services(self):
        result = self.cur.execute(f'SELECT * FROM services')
        result = result.fetchall()

        if result:
            return result
        return None
    
    def serv_get_fee_from_service_code(self, service_code):
        result  = self.cur.execute(f'SELECT fee FROM services WHERE service_code={service_code}')
        result = result.fetchone()

        if result:
            return result[0]
        return None
    
    def serv_get_service_code_from_name(self, service_name):
        result  = self.cur.execute(f'SELECT service_code FROM services WHERE name="{service_name}"')
        result = result.fetchone()

        if result:
            return result[0]
        return None
    
    def log_service(self, current_date_time : str,
                     date_service_provided : str, 
                     provider_id_num : int, 
                     member_id_num : int, 
                     service_code : int):
        
        # Sanitize id's
        if not member_id_num:
            return False
        if not provider_id_num:
            return False
        
        member_id_num = self.clean_id(member_id_num, self.MEMBER_ID_RANGE) - self.MEMBER_ID_RANGE
        provider_id_num = self.clean_id(provider_id_num, self.PROVIDER_ID_RANGE) - self.PROVIDER_ID_RANGE

        member_name = self.mem_get_name_from_id(member_id_num)
        fee = self.serv_get_fee_from_service_code(service_code)

        if not fee:
            return False
        
        result = self.cur.execute(f"""INSERT INTO services_provided_log(date_service_logged, date_service_provided, provider_id, member_id, member_name, s_code, fee) VALUES
                                        ("{current_date_time}", "{date_service_provided}", {provider_id_num}, {member_id_num}, "{member_name}", {service_code}, {fee})""")
        result = self.cur.execute(f'COMMIT')

        return True

    def generate_report(self, report_type, id_num : int):
        # id_num can be either a member number or a provider number
        #
        # if the report type is "all_services_weekly", id num MUST BE None.
        #
        # if the report requested is "member_weekly" the program returns all
        # services provided to that member in one big array
        #       like this: [(blah, blah...), (blah, blah...), ...]
        # 

        current_date = datetime.datetime.now()
        a_week_ago = current_date - datetime.timedelta(days=7)

        current_date = current_date.strftime("%Y/%m/%d %H:%M:%S")
        a_week_ago = a_week_ago.strftime("%Y/%m/%d %H:%M:%S")

        # MEMBER WEEKLY REPORTING
        if report_type == "member_weekly":
            if not id_num:
                return None
            id_num = self.clean_id(id_num, self.MEMBER_ID_RANGE)
            id_num = id_num - self.MEMBER_ID_RANGE
            result = self.cur.execute(f'SELECT * FROM services_provided_log WHERE member_id={id_num} AND date_service_provided<"{current_date}" AND date_service_provided>"{a_week_ago}"')

            return result.fetchall()
        
        # PROVIDER WEEKLY REPORTING
        if report_type == "provider_weekly":
            if not id_num:
                return None
            
            id_num = self.clean_id(id_num, self.PROVIDER_ID_RANGE)
            id_num = id_num - self.PROVIDER_ID_RANGE
            result = self.cur.execute(f'SELECT * FROM services_provided_log WHERE provider_id={id_num} AND date_service_provided<"{current_date}" AND date_service_provided>"{a_week_ago}"')

            return result.fetchall()
        
        # ALL SERVICES PROVIDED REPORTING
        if report_type == "all_services_weekly":
            if id_num:
                return None

            result = self.cur.execute(f'SELECT * FROM services_provided_log WHERE date_service_provided<"{current_date}" AND date_service_provided>"{a_week_ago}"')

            return result.fetchall()

        return None


    #calculates the total fees the member made from all the services
    def calculate_member_fees(self, member_ID) -> float:
        #get all service_logs where the member ID is the same as member_ID
        service_list = self.cur.execute("""SELECT fee FROM services_provided_log
                                                WHERE member_id = ?""", (member_ID,))
        service_list = self.cur.fetchall()

        total_fee = float(0)#make a varaible to be used as the return of all the fees combined
        for i in total_fee:#iterate through each service_log
            total_fee += service_list[0]

        return total_fee


    #calculate the total balance for the provider from all the services they provided
    #returns the total balance that ChocAn owes them.
    def calculate_provider_balances(self, provider_ID) -> float:
        #get all service_logs where the provider ID is the same as provider_ID
        service_list = self.cur.execute("""SELECT fee FROM services_provided_log
                                                WHERE provider_id = ?""", (provider_ID,))
        service_list = self.cur.fetchall()

        total_balance = float(0)#make a varaible to be used as the return of all the fees combined
        for i in total_balance:#iterate through each service_log
            total_balance += service_list[0]

        return total_balance
    

    #changes the members balance by addition or subtraction. will return the new
    #balance in the members account after the transaction.
    def deposit_member_balance(self, target_ID, amount: float) -> float:
        #validate member_ID
        if not isinstance(target_ID, int):
            if isinstance(target_ID, str):#if its a string then convert to a int
                target_ID = int(target_ID)
            else:
                print("Invalid ID")
                return None
            
        #validate amount is a float, otherwise return false
        if not isinstance(amount, float):
            if isinstance(amount, int):#if its a string then convert to a int
                amount = float(amount)
            else:
                print("Invalid amount type")
                return None
        
        #get the current balance and then add amount to it.
        current_balance = self.cur.execute("""SELECT balance from members
                                                    WHERE id = ?""", (target_ID,))
        current_balance = self.cur.fetchall()
        
        #create the new balance for the member
        new_balance = current_balance[0] + amount

        #insert the new balance to the member to update the balance variable
        self.cur.execute("UPDATE members SET balance = ? WHERE id = ?", (new_balance, target_ID))
        
        return new_balance #return the current balance of the member.
    
    def add_service(self, service_name : str, fee : float):
        if not service_name or not fee:
            return False
        
        var_test = self.cur.execute(f'SELECT name FROM services WHERE name="{service_name}"')
        var_test = var_test.fetchone()
        if var_test:
            return False

        self.cur.execute(f'INSERT INTO services (name, fee) VALUES ("{service_name}", {fee})')
        self.cur.execute(f'COMMIT')
        return True
    
    def remove_service(self, service_code : int):
        if not service_code:
            return False
        
        service_code = self.clean_id(service_code, self.SERVICE_CODE_RANGE) - self.SERVICE_CODE_RANGE
        var_test = self.cur.execute(f'SELECT name FROM services WHERE service_code={service_code}')
        var_test = var_test.fetchone()
        if not var_test:
            return False

        self.cur.execute(f'DELETE FROM services WHERE service_code={service_code}')
        self.cur.execute(f'COMMIT')
        return True

    def clean_id(self, id_num, id_range):
        if id_num < id_range and id_num > 0:
            id_num = id_num + id_range
            return id_num
        if id_num > id_range and id_num < id_range * 10:
            return id_num
        if id_num == id_range:
            return None
        return None
    #################################### END  ###################################