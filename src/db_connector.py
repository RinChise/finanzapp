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
        """Stellt die Verbindung zur MySQL-Datenbank her."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                return True
        except Error as e:
            if "1045" in str(e):  # Fehler: Access denied
                print("Falsches Passwort!")
            else:
                print(f"Fehler bei der Verbindung: {e}")
            self.connection = None
        return False

    def close(self):
        """Schließt die Verbindung zur Datenbank."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Verbindung zur Datenbank geschlossen.")
