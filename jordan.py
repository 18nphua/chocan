from DatabaseApi import db_client


client = db_client()

if client.add_provider("Jordan Dexter", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221):
    print("added successfully")
else:
    print("an error has occured")


id_num = client.prov_get_id_from_name("Jordan Dexter")
client.edit_provider(id_num, "name", "Other Jordan")
client.edit_provider(id_num, "phone_number", 1234123123)
client.edit_provider(id_num, "street_address", "321 Street St.")
client.edit_provider(id_num, "state", "Arizona")
client.edit_provider(id_num, "city", "Pheonix")
client.edit_provider(id_num, "zip_code", 123123)

print(client.prov_get_all(id_num))