import subprocess
import sqlite3
from time import sleep

"""
This file recreates the database files from scratch for use while debugging.

Usage: python.exe ResetAPI.py

Note: This will delete all database files and recreate them.
"""
path = "database"

databases   = ['members.db', 'providers.db', 'services_provided_log.db', 'services.db']
schemas     = ['(id INTEGER PRIMARY KEY, name varchar, phone_number int, street_address varchar, city varchar, state varchar, zip_code int, balance float)',
               '(id INTEGER PRIMARY KEY, name varchar, phone_number int, street_address varchar, city varchar, state varchar, zip_code int)',
               '(date_service_provided DATETIME, date_service_logged DATETIME, provider_id int, member_id int, member_name varchar, service_code int, fee float)',
               '(service_code INTEGER PRIMARY KEY, name varchar, fee float)']

confirm = input("This will delete all data in ALL database files. Are you sure you'd like to continue (Y/n?: ")
if confirm != 'Y':
    exit()

for i in range(4):
    print(f"deleting {databases[i]}..")

    cmd = f"rm {path}/{databases[i]} -Force"
    subprocess.run(['powershell', '-Command', cmd], capture_output=True)
sleep(1)
print("")

for i in range(4):
    print(f"creating {databases[i]}...")

    cmd2 = f"New-Item {path}/{databases[i]} -ItemType File"
    subprocess.run(['powershell', '-Command', cmd2], capture_output=True)
    db = sqlite3.connect(f'{path}/{databases[i]}')
    cur = db.cursor()
    result = cur.execute(f"CREATE TABLE {databases[i].strip('.db')} {schemas[i]}")

sleep(1)

print("     adding service codes...")
codes = [874526, 230984, 563120, 982345, 781049, 346879, 129543, 460382, 591204, 735860]
names = ["Massage", "Therapy", "Chiropracty", "Physical Therapy", "Rehabilition", "Shock Therapy", "Anti-Chocolate Tablets", "Retreat", "Couples Counciling", "Psycoanalysis"]
costs = [100.00, 250.00, 50.00, 150.00, 300.00, 75.00, 5.00, 15.00, 200.00, 40.00]

service_db = sqlite3.connect(f"{path}/services.db")
cur = service_db.cursor()

for i in range(10):
    cur.execute(f'INSERT INTO services(service_code, name, fee) VALUES ({codes[i]}, "{names[i]}", {costs[i]})')
    cur.execute("COMMIT")

print("done.")

# Keys setup