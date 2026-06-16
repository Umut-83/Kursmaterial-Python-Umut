# 0. Eine leere Liste erstellen
users = []

# 1. Loop für die Eingabemöglichkeit
while True:
    # Tipp aus der Aufgabe nutzen (.lower() wandelt alles in Kleinbuchstaben um)
    user_entry = input("Gib einen Usernamen ein (oder 'quit' zum Beenden): ").lower()
    
    # 1.a Bei Eingabe von "quit" den Loop abbrechen
    if user_entry == "quit":
        break
        
    # 2. Nach dem Eingeben den User der Liste hinzufügen
    users.append(user_entry)
    
    # Optional: Falls die Liste 10 Einträge groß ist, Programm beenden
    if len(users) == 10:
        print("Maximale Anzahl von 10 Usern erreicht.")
        break

# Bestehende Liste mit den Usern ausgeben
print("Bestehende User-Liste:", users)
