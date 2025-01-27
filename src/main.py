from db_connector import DatabaseConnector
from ui_handler import UIHandler
from logic import Logic

if __name__ == "__main__":
    ui = UIHandler()

    # Zugangsdaten abfragen
    user = ui.get_user_input("Gib den MySQL-Benutzernamen ein: ")
    password = ui.get_user_input("Gib das MySQL-Passwort ein: ")

    # Datenbankkonfiguration
    db_config = {
        "host": "localhost",
        "user": user,
        "password": password,
        "database": "finanz_db"  # Name der Datenbank
    }

    # Verbindung zur Datenbank testen
    db = DatabaseConnector(**db_config)
    if not db.connect():  # Verbindung fehlgeschlagen
        ui.show_message("Verbindung zur Datenbank fehlgeschlagen. Programm wird beendet.")
        db.close()
        exit()

    # Verbindung erfolgreich
    ui.show_message("Verbindung zur Datenbank erfolgreich hergestellt!")

    # Initialisiere die Geschäftslogik
    logic = Logic(db)

    # Hauptprogramm
    while True:
        ui.show_menu()
        choice = ui.get_user_choice()

        if choice == "1":
            # Neue Transaktion hinzufügen
            data = ui.get_transaction_data()
            logic.add_transaction(*data)
        elif choice == "2":
            # Transaktionen anzeigen
            transactions = logic.get_transactions()
            for transaction in transactions:
                print(transaction)
        elif choice == "3":
            # Programm beenden
            ui.show_message("Programm beendet.")
            break
        else:
            ui.show_message("Ungültige Auswahl. Bitte versuche es erneut.")

    # Verbindung schließen
    db.close()
