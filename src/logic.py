class Logic:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def add_transaction(self, account_id, amount, transaction_type, description):
        """Fügt eine neue Transaktion in die Datenbank ein."""
        try:
            query = """
                INSERT INTO transactions (account_id, amount, transaction_type, description, transaction_date)
                VALUES (%s, %s, %s, %s, NOW())
            """
            params = (account_id, amount, transaction_type, description)
            cursor = self.db_connector.connection.cursor()
            cursor.execute(query, params)
            self.db_connector.connection.commit()
            print("Transaktion erfolgreich hinzugefügt!")
        except Exception as e:
            print(f"Fehler beim Hinzufügen der Transaktion: {e}")

    def get_transactions(self):
        """Holt alle Transaktionen aus der Datenbank."""
        try:
            query = "SELECT * FROM transactions"
            cursor = self.db_connector.connection.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Fehler beim Abrufen der Transaktionen: {e}")
            return []
