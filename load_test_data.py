from DatabaseApi import db_client



client = db_client()

client.add_provider("Provider 0", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("Provider 1", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("Provider 2", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("Provider 3", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("Provider 4", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("Provider 5", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("Provider 6", 1235431111, "123 Street St", "Portland", "Oregon", 97123)

client.add_member("Jordan Dexter", 1234567890, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("Nick Lastname", 3334445555, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("ppiliF", 1112223333, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("Changster", 1231231234, "1234 SE Street St.", "Portland", "Oregon", 97221)

prov_id_num = client.prov_get_id_from_name("John Doe 5")
mem_id_num = client.mem_get_id_from_name("Jordan Dexter 7")

names = ["Massage", "Therapy", "Chiropracty", "Physical Therapy", "Rehabilition", "Shock Therapy", "Anti-Chocolate Tablets", "Retreat", "Couples Counciling", "Psycoanalysis"]
costs = [100.00, 250.00, 50.00, 150.00, 300.00, 75.00, 5.00, 15.00, 200.00, 40.00]

for i in range(len(names)):
    client.add_service(names[i], costs[i])

client.log_service("2024/12/04 10:21:00", "2024/12/01 10:00:00", prov_id_num, mem_id_num, client.serv_get_service_code_from_name('Physical Therapy'))
client.log_service("2024/12/04 10:21:00", "2024/11/28 10:00:00", prov_id_num, mem_id_num, client.serv_get_service_code_from_name('Retreat'))
client.log_service("2024/12/04 10:21:00", "2024/12/02 10:00:00", prov_id_num, mem_id_num, client.serv_get_service_code_from_name('Shock Therapy'))
client.log_service("2024/12/04 10:21:00", "2024/11/29 10:00:00", prov_id_num, mem_id_num, client.serv_get_service_code_from_name('Anti-Chocolate Tablets'))
