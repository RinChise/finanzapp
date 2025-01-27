import mysql.connector
from mysql.connector import Error

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            # Verbindung zur Datenbank herstellen
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("\nVerbindung zur Datenbank erfolgreich hergestellt!")
        except Error as e:
            print(f"Fehler bei der Verbindung: {e}")

    def close(self):
        # Verbindung schließen
        if self.connection.is_connected():
            self.connection.close()
            print("Verbindung geschlossen.")