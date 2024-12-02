from DatabaseApi import db_client


client = db_client()

if client.add_provider("Jordan Dexter", 5419937235, "1234 SE Street St.", "Portland", "Oregon", 97221):
    print("added successfully")
else:
    print("an error has occured")


print(client.prov_get_id_from_name("Jordan Dexter"))