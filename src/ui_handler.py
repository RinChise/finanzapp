class UIHandler:
    def __init__(self):
        pass

    def show_menu(self):
        """Zeigt das Hauptmenü an."""
        print("\nWillkommen in der FinanzApp!")
        print("1. Neue Transaktion hinzufügen")
        print("2. Transaktionen anzeigen")
        print("3. Programm beenden")

    def get_user_input(self, message):
        """Fragt den Benutzer nach einer Eingabe."""
        return input(message)

    def get_user_choice(self):
        """Fragt die Benutzerauswahl ab."""
        return self.get_user_input("Wähle eine Option: ")

    def show_message(self, message):
        """Zeigt eine Nachricht an den Benutzer."""
        print(message)

    def get_transaction_data(self):
        """Fragt die Daten für eine neue Transaktion ab."""
        account_id = self.get_user_input("Gib die Konto-ID ein: ")
        amount = float(self.get_user_input("Betrag: "))
        transaction_type = self.get_user_input("Typ (income/expense): ")
        description = self.get_user_input("Beschreibung: ")
        return account_id, amount, transaction_type, description
