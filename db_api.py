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

    def gen_id(self):
        return 1
    
    # MEMBER FUNCTIONALITY

    def add_member(self,
                   name: str,
                   phone_number : str,
                   street_address: str,
                   city: str,
                   state : str,
                   zip_code : int):

        id_num = 1 # self.gen_id()
        result = self.mem_cur.execute(f"""INSERT INTO members VALUES 
                ({id_num}, '{name}', {phone_number}, '{street_address}', '{city}', '{state}', {zip_code});
                """)
        return
    
    def edit_member(self, attribute : str, value):
        # to implement
        return
    
    def remove_member(self, name):
        #delete the member
        self.mem_cur.execute(f"DELETE FROM members WHERE name = ?", (name))#later change it to ID, but for now its name
        return
    
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