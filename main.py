# #==================================THEMA: DICTIONARIES==================================
# #
# # AUFGABE 1: TELEFONBUCH (SEHR EINFACH)
# #
# # Erstelle ein Wörterbuch, das Namen als Schlüssel und Telefonnummern als Wert speichert.
# #
# # 0. Leeres Wörterbuch anlegen: phonebook = {}
# # 1. Der Benutzer gibt 3 Namen und Telefonnummern ein (OHNE Schleife)
# # # 2. Jeder Eintrag wird im Wörterbuch gespeichert
# # # 3. Gib das gesamte Telefonbuch aus
# # # 4. Frage den Benutzer nach einem Namen und gib die dazugehörige Nummer aus
# # #
# # # BEISPIEL:
# # # Eingabe: Name = "Anna", Nummer = "0123456789"
# # # Eingabe: Name = "Ben", Nummer = "9876543210"
# # # Eingabe: Name = "Clara", Nummer = "5551234567"
# # # Ausgabe: Telefonbuch: {'Anna': '0123456789', 'Ben': '9876543210', 'Clara': '5551234567'}
# # # Suche: "Anna" -> Anna hat die Nummer 0123456789
# # #
# # default_user = {
# #     "username": "SQZ0111",
# #     "isActive": False,
# #     #"repositories": ["https://abc.com"]
# #     "lastSeen": "today"
    
# # }

# # #for key,value default_user.items():
# #     #das dictionary nur gelesen oder vorhandene Einträge verändert werden

# # # 0. Leeres Wörterbuch anlegen
# # phonebook = {}  
   
# # while True:
# #     # 1. Der Benutzer gibt den Namen ein
# #     name = input("Name der Person. To exit type [q].\n>>>")
# #     if name.lower() == "q":
# #         break
    
# #     # Der Benutzer gibt die dazugehörige Nummer ein
# #     nummer = input(f"Telefonnummer für {name}.\n>>>")
    
# #     # 2. Jeder Eintrag wird im Wörterbuch gespeichert
# #     phonebook[name] = nummer
            

# # # 3. Gib das gesamte Telefonbuch aus
# # print("Telefonbuch:", phonebook)

# # # default_user["isActive"] = True
# # # default_user["hasAccess"] = False
            
# # print(default_user)

# # # 4. Frage den Benutzer nach einem Namen und gib die dazugehörige Nummer aus
# # suche = input("Nach welchem Namen möchtest du suchen?\n>>>")
# # if suche in phonebook:
# #     print(f"{suche} hat die Nummer {phonebook[suche]}")
# # else:
# #     print(f"{suche} wurde nicht gefunden.")




# #
# # AUFGABE 2: NOTENSPEICHER (SEHR EINFACH)
# #
# # Erstelle ein Wörterbuch, das Fächer als Schlüssel und Noten als Wert speichert.
# #
# # 0. Leeres Wörterbuch anlegen: grades = {}
# # 1. Der Benutzer gibt 3 Fächer und Noten ein (OHNE Schleife)
# # 2. Die Note wird als float gespeichert (TIPP: float() für Umwandlung)
# # 3. Gib alle Fächer und Noten aus
# # 4. Berechne den Notendurchschnitt (TIPP: sum() und len())
# #
# # BEISPIEL:
# # Eingabe: Fach = "Mathe", Note = 2.0
# # Eingabe: Fach = "Deutsch", Note = 1.5
# # Eingabe: Fach = "Englisch", Note = 2.5
# # Ausgabe: Mathe: 2.0, Deutsch: 1.5, Englisch: 2.5
# # Durchschnitt: 2.0
# #

# #
# # AUFGABE 3: LÄNDER-HAUPTSTÄDTE (SEHR EINFACH)
# #
# # Erstelle ein Wörterbuch mit vordefinierten Ländern und Hauptstädten.
# # Der Benutzer soll nach einem Land fragen und die Hauptstadt angezeigt bekommen.
# #
# # 0. Wörterbuch mit 3 Ländern erstellen: countries = {"Deutschland": "Berlin", "Frankreich": "Paris", "Italien": "Rom"}
# # 1. Gib dem Benutzer die Auswahl: Zeige alle Länder an
# # 2. Der Benutzer gibt ein Land ein
# # 3. Wenn das Land existiert, gib die Hauptstadt aus
# # 4. Wenn das Land nicht existiert, gib "Land nicht gefunden" aus
# #
# # BEISPIEL:
# # Länder: Deutschland, Frankreich, Italien
# # Eingabe: "Deutschland" -> Die Hauptstadt von Deutschland ist Berlin
# # # Eingabe: "Spanien" -> Spanien nicht gefunden
# # #

# # # 0. Wörterbuch mit 3 Ländern erstellen
# # countries = {"Deutschland": "Berlin", "Frankreich": "Paris", "Italien": "Rom"}

# # # 1. Gib dem Benutzer die Auswahl: Zeige alle Länder an
# # # .keys() holt die Ländernamen, ", ".join() verbindet sie lesbar mit Komma
# # print("Verfügbare Länder:", ", ".join(countries.keys()))

# # # 2. Der Benutzer gibt ein Land ein
# # eingabe = input("Bitte gib ein Land ein: ")

# # # 3. & 4. Prüfen, ob das Land existiert und passende Nachricht ausgeben
# # if eingabe in countries:
# #     hauptstadt = countries[eingabe]
# #     print(f"Die Hauptstadt von {eingabe} ist {hauptstadt}.")
# # else:
# #     print(f"{eingabe} nicht gefunden.")


# # AUFGABE 4: WÖRTERBUCH ERWEITERN (SEHR EINFACH)
# #
# # Starte mit einem leeren Wörterbuch und füge nach und nach Einträge hinzu.
# #
# # # 0. Leeres Wörterbuch anlegen: my_dict = {}
# # my_dict = {}

# # # 1. Füge 3 Schlüssel-Wert-Paare hinzu (ohne Benutzereingabe, direkt im Code)
# # #    TIPP: my_dict["key1"] = "value1"
# # my_dict["name"] = "Anna"
# # my_dict["alter"] = 25
# # my_dict["stadt"] = "Berlin"

# # # 2. Ändere den Wert von einem Schlüssel
# # #    TIPP: my_dict["key1"] = "neuer_wert"
# # my_dict["alter"] = 26

# # # 3. Lösche einen Schlüssel mit del
# # #    TIPP: del my_dict["key2"]
# # del my_dict["alter"]

# # # 4. Gib das fertige Wörterbuch aus
# # print(my_dict)



# #
# # AUFGABE 5: EINKAUFSZETTEL (EINFACH MIT SCHLEIFE)
# #
# # Erstelle ein Wörterbuch für einen Einkaufszettel. Der Benutzer kann Produkte und Mengen eingeben.
# #
# # 0. Leeres Wörterbuch: shopping_list = {}
# # 1. Schleife für die Eingabe (3 Durchgänge)
# # 2. Pro Durchgang: Produktname und Menge eingeben
# # 3. Speichere im Wörterbuch: shopping_list[produkt] = menge
# # 4. Nach der Schleife: Gib den gesamten Einkaufszettel aus
# # 5. Frage den Benutzer, ob er ein Produkt löschen möchte (ja/nein)
# # 6. Wenn ja: Produktname eingeben und aus Wörterbuch löschen
# #
# # BEISPIEL:
# # 1. Produkt: "Äpfel", Menge: 3
# # 2. Produkt: "Milch", Menge: 1
# # 3. Produkt: "Brot", Menge: 2
# # Einkaufszettel: Äpfel: 3, Milch: 1, Brot: 2
# # Löschen? ja
# # Welches Produkt? "Milch"
# # Neuer Einkaufszettel: Äpfel: 3, Brot: 2
# #

# # AUFGABE 5: EINKAUFSZETTEL (EINFACH MIT SCHLEIFE)
# #
# # Erstelle ein Wörterbuch für einen Einkaufszettel. Der Benutzer kann Produkte und Mengen eingeben.
# #
# # 0. Leeres Wörterbuch: shopping_list = {}
# shopping_list = {}

# # 1. Schleife für die Eingabe (3 Durchgänge)
# # range(3) sorgt dafür, dass die Schleife genau 3-mal läuft (von 0 bis 2)
# for i in range(3):
#     print(f"\n--- {i+1}. Produkt ---")
#     # 2. Pro Durchgang: Produktname und Menge eingeben
#     produkt = input("Produktname: ")
#     # Da eine Menge eine Zahl ist, wandeln wir sie direkt in ein Integer (int) um
#     menge = int(input("Menge: "))
    
#     # 3. Speichere im Wörterbuch: shopping_list[produkt] = menge
#     shopping_list[produkt] = menge

# # 4. Nach der Schleife: Gib den gesamten Einkaufszettel aus
# print("\nEinkaufszettel:", shopping_list)

# # 5. Frage den Benutzer, ob er ein Produkt löschen möchte (ja/nein)
# loeschen_antwort = input("\nMöchtest du ein Produkt löschen? (ja/nein): ").lower()

# # 6. Wenn ja: Produktname eingeben und aus Wörterbuch löschen
# if loeschen_antwort == "ja":
#     loesch_produkt = input("Welches Produkt soll gelöscht werden? ")
    
# #     # Sichergehen, dass das Produkt auch wirklich auf dem Zettel steht
# #     if loesch_produkt in shopping_list:
# #         del shopping_list[loesch_produkt]
# #         print(f"\n{loesch_produkt} wurde gelöscht.")
# #     else:
# #         print(f"\n{loesch_produkt} steht nicht auf dem Einkaufszettel.")

# # # Zum Schluss den aktualisierten Zettel anzeigen
# # print("Neuer Einkaufszettel:", shopping_list)





# # #
# # # ALLGEMEINE TIPS FÜR ALLE AUFGABEN:
# # #
# # # - Wörterbücher werden mit {} erstellt
# # # - Auf Werte zugreifen: dictionary[key]
# # # - Werte setzen: dictionary[key] = value
# # # - Auf Existenz prüfen: if key in dictionary:
# # # - Löschen: del dictionary[key] oder dictionary.pop(key)
# # # - Alle Schlüssel: dictionary.keys()
# # # - Alle Werte: dictionary.values()
# # # - Alle Paare: dictionary.items()
# # # - Bei Eingaben mit input() immer den richtigen Datentyp verwenden (int, float, str)




# # #==================================THEMA: FUNKTIONEN==================================
# # #
# # # AUFGABE 1: BEGRÜSSUNGS-FUNKTION (SEHR EINFACH)
# # #
# # # Schreibe eine Funktion, die einen Namen als Parameter nimmt und eine Begrüßung ausgibt.
# # #
# # # 0. Definiere die Funktion: def gruesse(name):
# # # 1. Die Funktion gibt "Hallo [name]!" aus
# # # 2. Rufe die Funktion mit 3 verschiedenen Namen auf (OHNE Schleife)
# # #
# # # BEISPIEL:
# # # gruesse("Anna") -> Hallo Anna!
# # # gruesse("Ben") -> Hallo Ben!
# # # gruesse("Clara") -> Hallo Clara!
# # #
# # def gruesse(name):
# #     print(f"Hallo {name}!")

# # gruesse("Anna")
# # gruesse("Ben")
# # gruesse("Clara")



# # ## 0. Definiere die Funktion: def summe(zahl1, zahl2):
# # def summe(zahl1, zahl2):
# #     # 1. Die Funktion berechnet die Summe und gibt sie mit return zurück
# # #     return zahl1 + zahl2


# # # 2. Rufe die Funktion mit 3 verschiedenen Zahlenpaaren auf
# # # 3. Gib die Ergebnisse aus
# # ergebnis1 = summe(5, 3)
# # print(f"summe(5, 3) -> {ergebnis1}")

# # ergebnis2 = summe(10, 7)
# # print(f"summe(10, 7) -> {ergebnis2}")

# # ergebnis3 = summe(2.5, 4.5)
# # print(f"summe(2.5, 4.5) -> {ergebnis3}")

# # #

# # AUFGABE 3: QUADRAT-FUNKTION (SEHR EINFACH)
# #
# # Schreibe eine Funktion, die eine Zahl als Parameter nimmt und das Quadrat zurückgibt.
# #
# # 0. Definiere die Funktion: def quadrat(zahl):
# def quadrat(zahl):
#     # 1. Die Funktion berechnet zahl * zahl und gibt es mit return zurück
#     return zahl * zahl


# # 2. Der Benutzer gibt eine Zahl ein (input)
# # Wichtig: input() liefert Text, daher wandeln wir ihn mit float() in eine Zahl um
# eingabe = float(input("Bitte gib eine Zahl ein: "))

# # 3. Rufe die Funktion mit der eingegebenen Zahl auf
# ergebnis = quadrat(eingabe)

# # 4. Gib das Ergebnis aus
# print(f"Das Quadrat von {eingabe} ist {ergebnis}")


# #
# # 0. Definiere die Funktion
# def ist_gerade(zahl):
#     # 1. Gibt True zurück, wenn die Zahl gerade ist, sonst False
#     if zahl % 2 == 0:
#         return True
#     else:
#         return False

# # 2. Der Benutzer gibt eine Zahl ein (Zahl muss in eine Ganzzahl/int umgewandelt werden)
# eingabe = input("Bitte gib eine Zahl ein: ")
# user_zahl = int(eingabe)

# # 3. Rufe die Funktion mit der eingegebenen Zahl auf
# ergebnis = ist_gerade(user_zahl)

# # 4. Gib aus, ob die Zahl gerade oder ungerade ist
# if ergebnis:
#     print(f"Die Zahl {user_zahl} ist gerade")
# else:
#     print(f"Die Zahl {user_zahl} ist ungerade")

# ## 0. Definiere die Funktionen
# # 0.a Funktion zum Addieren
# def addieren(a, b):
#     return a + b

# # 0.b Funktion zum Subtrahieren
# def subtrahieren(a, b):
#     return a - b

# # 0.c Funktion zum Multiplizieren
# def multiplizieren(a, b):
#     return a * b

# # 1. Der Benutzer gibt 2 Zahlen und eine Operation ein
# zahl1 = float(input("Erste Zahl: "))
# zahl2 = float(input("Zweite Zahl: "))
# operation = input("Operation (+, -, *): ")

# # 2. Rufe die passende Funktion auf und 3. Gib das Ergebnis aus
# if operation == "+":
#     ergebnis = addieren(zahl1, zahl2)
#     print(f"{zahl1} + {zahl2} = {ergebnis}")
# elif operation == "-":
#     ergebnis = subtrahieren(zahl1, zahl2)
#     print(f"{zahl1} - {zahl2} = {ergebnis}")
# elif operation == "*":
#     ergebnis = multiplizieren(zahl1, zahl2)
#     print(f"{zahl1} * {zahl2} = {ergebnis}")
# else:
#     print("Ungültige Operation! Bitte nutze nur +, - oder *.")

# # #
# # # AUFGABE 6: STANDARDWERTE (EINFACH)
# # #
# # # Schreibe eine Funktion mit Standardwerten für Parameter.
# # #
# # # 0. Definiere die Funktion: def begruessung(name, anrede="Hallo"):
# # # 1. Die Funktion gibt "[anrede] [name]!" aus
# # # 2. Rufe die Funktion auf:
# # #    2.a Mit nur einem Parameter (name) -> Standardwert "Hallo" wird verwendet
# # #    2.b Mit zwei Parametern (name, anrede) -> Eigener Wert wird verwendet
# # #
# # # BEISPIEL:
# # # begruessung("Anna") -> Hallo Anna!
# # # begruessung("Ben", "Guten Morgen") -> Guten Morgen Ben!
# # #

# # #
# # # AUFGABE 7: LISTE DURCHGEHEN (MITTEL)
# # #
# # # # Schreibe eine Funktion, die eine Liste von Zahlen als Parameter nimmt
# # # # und den Durchschnitt berechnet.
# # # #
# # # # 0. Definiere die Funktion: def durchschnitt(zahlen_liste):
# # # # 1. Die Funktion berechnet den Durchschnitt mit sum() und len()
# # # # 2. Die Funktion gibt den Durchschnitt zurück
# # # # 3. Erstelle eine Liste mit 5 Zahlen (OHNE Benutzereingabe)
# # # # 4. Rufe die Funktion mit der Liste auf
# # # # 5. Gib den Durchschnitt aus
# # # #
# # # BEISPIEL:
# # # Liste: [4, 5, 6, 7, 8] -> Durchschnitt: 6.0
# # # Liste: [10, 20, 30, 40, 50] -> Durchschnitt: 30.0
# # #

# # # AUFGABE 8: MEHRERE RÜCKGABEWERTE (MITTEL)
# # #
# # # Schreibe eine Funktion, die mehrere Werte zurückgibt.
# # #
# # # 0. Definiere die Funktion: def min_max(zahlen_liste):
# def min_max(zahlen_liste):
#     # 1. Die Funktion berechnet das Minimum und Maximum der Liste
#     #    TIPP: min() und max() Funktionen verwenden
#     min_wert = min(zahlen_liste)
#     max_wert = max(zahlen_liste)
    
#     # 2. Die Funktion gibt beide Werte zurück (TIPP: return min_wert, max_wert)
#     return min_wert, max_wert

# # 3. Erstelle eine Liste mit beliebigen Zahlen
# # BEISPIEL 1:
# liste_beispiel_1 = [5, 2, 8, 1, 9]

# # 4. Rufe die Funktion auf und speichere beide Rückgabewerte
# minimum_1, maximum_1 = min_max(liste_beispiel_1)

# # 5. Gib Minimum und Maximum aus
# print(f"Liste: {liste_beispiel_1} -> Minimum: {minimum_1}, Maximum: {maximum_1}")


# # BEISPIEL 2:
# liste_beispiel_2 = [3.5, 2.1, 7.8, 4.2]

# # 4. Rufe die Funktion auf und speichere beide Rückgabewerte (für das zweite Beispiel)
# minimum_2, maximum_2 = min_max(liste_beispiel_2)

# # 5. Gib Minimum und Maximum aus (für das zweite Beispiel)
# print(f"Liste: {liste_beispiel_2} -> Minimum: {minimum_2}, Maximum: {maximum_2}")


# #
# AUFGABE 9: FUNKTION MIT SCHLEIFE (MITTEL)
#
# Schreibe eine Funktion, die eine Liste von Namen bekommt
# und jeden Namen mit einer Begrüßung ausgibt.
#
# 0. Definiere die Funktion: def begruesse_alle(namen_liste):
# 1. Die Funktion geht mit einer for-Schleife durch die Liste
# 2. Für jeden Namen wird "Hallo [name]!" ausgegeben
# 3. Erstelle eine Liste mit 5 Namen (OHNE Benutzereingabe)
# 4. Rufe die Funktion mit der Liste auf
#
# BEISPIEL:
# Liste: ["Anna", "Ben", "Clara", "David", "Emma"]
# Ausgabe:
# Hallo Anna!
# Hallo Ben!
# Hallo Clara!
# Hallo David!
# Hallo Emma!
#

# # AUFGABE 10: FUNKTIONEN ZUSAMMENSETZEN (SCHWER)
# #
# # Schreibe mehrere kleine Funktionen, die zusammen ein Programm ergeben.
# #
# # 0. Definiere die Funktionen:
# #    0.a def eingabe_zahl(prompt): gibt input als float zurück
def eingabe_zahl(prompt):
    return float(input(prompt))

# #    0.b def berechne_flaeche(breite, hoehe): gibt breite * hoehe zurück
def berechne_flaeche(breite, hoehe):
    return breite * hoehe

# #    0.c def ausgabe(flaeche): gibt "Die Fläche ist: [flaeche]" aus
def ausgabe(flaeche):
    print(f"Die Fläche ist: {flaeche}")

# # 1. Rufe die Funktionen in der richtigen Reihenfolge auf:
# #    1.a Breite mit eingabe_zahl() einlesen
breite_eingabe = eingabe_zahl("Breite: ")

# #    1.b Höhe mit eingabe_zahl() einlesen
hoehe_eingabe = eingabe_zahl("Höhe: ")

# #    1.c Fläche mit berechne_flaeche() berechnen
ergebnis_flaeche = berechne_flaeche(breite_eingabe, hoehe_eingabe)

# #    1.d Ergebnis mit ausgabe() anzeigen
ausgabe(ergebnis_flaeche)
#
# 

#

#
# ALLGEMEINE TIPS FÜR ALLE AUFGABEN:
#
# - Funktionen werden mit def definiert: def funktionsname(parameter):
# - Der Code einer Funktion wird eingerückt
# - Mit return gibt eine Funktion einen Wert zurück
# - Ohne return gibt die Funktion None zurück
# - Funktionen werden mit funktionsname(argument) aufgerufen
# - Parameter können Standardwerte haben: def name(parameter="wert"):
# - Mehrere Rückgabewerte: return wert1, wert2
# - Die Dokumentation findest du unter:
#   https://www.w3schools.com/python/python_functions.asp