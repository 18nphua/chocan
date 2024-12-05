import subprocess
import sqlite3
from time import sleep

"""
This file recreates the database files from scratch for use while debugging.

Usage: python.exe ResetAPI.py

Note: This will delete all database files and recreate them.
"""
path = "database"

database    =  'chocan.db'
tables      = ['members', 'providers', 'services_provided_log', 'services']
schemas     = ['(id INTEGER PRIMARY KEY, name varchar, phone_number int, street_address varchar, city varchar, state varchar, zip_code int, last_payment_date DATETIME, status varchar, balance float)',
               '(id INTEGER PRIMARY KEY, name varchar, phone_number int, street_address varchar, city varchar, state varchar, zip_code int)',
               '(date_service_logged DATETIME, date_service_provided DATETIME, provider_id int, member_id int, member_name varchar, s_code int, fee float, FOREIGN KEY (member_id) REFERENCES members(id), FOREIGN KEY (provider_id) REFERENCES providers(id), FOREIGN KEY (s_code) REFERENCES services(service_code))',
               '(service_code INTEGER PRIMARY KEY, name varchar, fee float)']

confirm = input("This will delete all data in ALL database files. Are you sure you'd like to continue (Y/n?: ")
if confirm != 'Y':
    exit()


print(f"deleting {database}..")

cmd = f"rm {path}/{database} -Force"
subprocess.run(['powershell', '-Command', cmd], capture_output=True)
sleep(1)


print(f"creating {database}...")

cmd2 = f"New-Item {path}/{database} -ItemType File"
subprocess.run(['powershell', '-Command', cmd2], capture_output=True)
db = sqlite3.connect(f'{path}/{database}')
cur = db.cursor()
cur.execute("PRAGMA foreign_keys = ON")
for i in range(4):
    result = cur.execute(f"CREATE TABLE {tables[i]} {schemas[i]}")
sleep(1)

print("done.")

# Keys setup