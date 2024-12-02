import subprocess
import sqlite3
from time import sleep

"""
This file recreates the database files from scratch for use while debugging.

Usage: python.exe ResetAPI.py

Note: This will delete all database files and recreate them.
"""

databases   = ['members.db', 'providers.db', 'services_provided_log.db']
schemas     = ['(id INTEGER PRIMARY KEY, name varchar, phone_number int, street_address varchar, city varchar, state varchar, zip_code int, balance float)',
               '(id INTEGER PRIMARY KEY, name varchar, phone_number int, street_address varchar, city varchar, state varchar, zip_code int)',
               '(date_service_provided date, date_service_logged date, provider_id, member_id int, member_name varchar, service_code int, fee float)']

confirm = input("This will delete all data in ALL database files. Are you sure you'd like to continue (Y/n?: ")
if confirm != 'Y':
    exit()

for i in range(3):
    print(f"deleting {databases[i]}..")

    cmd = f"rm {databases[i]} -Force"
    subprocess.run(['powershell', '-Command', cmd], capture_output=True)
sleep(1)
print("done.")

for i in range(3):
    print(f"creating {databases[i]}...")

    cmd2 = f"New-Item {databases[i]} -ItemType File"
    subprocess.run(['powershell', '-Command', cmd2], capture_output=True)
    db = sqlite3.connect(databases[i])
    cur = db.cursor()
    result = cur.execute(f"CREATE TABLE {databases[i].strip('.db')} {schemas[i]}")
    

sleep(1)
print("done.")

# Keys setup


