
import provider as prov
import DatabaseApi as db
def main():
    database = db.db_client()
    provider = prov.Provider()

    provider.read_provider_num()


if __name__ == "__main__":
    main()