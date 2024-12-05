from DatabaseApi import db_client



client = db_client()



id_num = client.prov_get_id_from_name("Jordan Dexter")
client.edit_provider(id_num, "name", "Other Jordan")
client.edit_provider(id_num, "phone_number", 1234123123)
client.edit_provider(id_num, "street_address", "321 Street St.")
client.edit_provider(id_num, "state", "Arizona")
client.edit_provider(id_num, "city", "Pheonix")
client.edit_provider(id_num, "zip_code", 123123)

client.add_provider("John Doe 0", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("John Doe 1", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("John Doe 2", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("John Doe 3", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("John Doe 4", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("John Doe 5", 1235431111, "123 Street St", "Portland", "Oregon", 97123)
client.add_provider("John Doe 6", 1235431111, "123 Street St", "Portland", "Oregon", 97123)

client.add_member("Jordan Dexter 0", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("Jordan Dexter 1", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("Jordan Dexter 2", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("Jordan Dexter 3", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("Jordan Dexter 4", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("Jordan Dexter 5", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("Jordan Dexter 6", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("Jordan Dexter 7", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("Jordan Dexter 8", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221)
client.add_member("Jordan Dexter 9", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221)

prov_id_num = client.prov_get_id_from_name("John Doe 5")
mem_id_num = client.mem_get_id_from_name("Jordan Dexter 7")

if client.log_service("2024/12/03 10:21:00", "2024/11/30 10:25:00", prov_id_num, mem_id_num, 874526):
    #print("logged")
    pass
else:
    print("an error occured")

result = client.generate_report("member_weekly", mem_id_num)

print(result)