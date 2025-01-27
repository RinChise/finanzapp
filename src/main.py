from db_connector import DatabaseConnector

# Dynamische Eingabe der Zugangsdaten
user = input("Gib den MySQL-Benutzernamen ein: ")
password = input("Gib das MySQL-Passwort ein: ")

# Datenbankkonfiguration
db_config = {
    "host": "localhost",
    "user": user,
    "password": password,
    "database": "finanz_db"
}

# Verbindung testen
if __name__ == "__main__":
    db = DatabaseConnector(**db_config)
    db.connect()
    db.close()

