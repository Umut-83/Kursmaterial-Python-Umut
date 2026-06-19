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

# # # #
# # # # AUFGABE 6: STANDARDWERTE (EINFACH)
# # # #
# # # # Schreibe eine Funktion mit Standardwerten für Parameter.
# # # #
# # # # 0. Definiere die Funktion: def begruessung(name, anrede="Hallo"):
# # # # 1. Die Funktion gibt "[anrede] [name]!" aus
# # # # 2. Rufe die Funktion auf:
# # # #    2.a Mit nur einem Parameter (name) -> Standardwert "Hallo" wird verwendet
# # # #    2.b Mit zwei Parametern (name, anrede) -> Eigener Wert wird verwendet
# # # #
# # # # BEISPIEL:
# # # # begruessung("Anna") -> Hallo Anna!
# # # # begruessung("Ben", "Guten Morgen") -> Guten Morgen Ben!
# # # #

# # # #
# # # # AUFGABE 7: LISTE DURCHGEHEN (MITTEL)
# # # #
# # # # # Schreibe eine Funktion, die eine Liste von Zahlen als Parameter nimmt
# # # # # und den Durchschnitt berechnet.
# # # # #
# # # # # 0. Definiere die Funktion: def durchschnitt(zahlen_liste):
# # # # # 1. Die Funktion berechnet den Durchschnitt mit sum() und len()
# # # # # 2. Die Funktion gibt den Durchschnitt zurück
# # # # # 3. Erstelle eine Liste mit 5 Zahlen (OHNE Benutzereingabe)
# # # # # 4. Rufe die Funktion mit der Liste auf
# # # # # 5. Gib den Durchschnitt aus
# # # # #
# # # # BEISPIEL:
# # # # Liste: [4, 5, 6, 7, 8] -> Durchschnitt: 6.0
# # # # Liste: [10, 20, 30, 40, 50] -> Durchschnitt: 30.0
# # # #

# # # # AUFGABE 8: MEHRERE RÜCKGABEWERTE (MITTEL)
# # # #
# # # # Schreibe eine Funktion, die mehrere Werte zurückgibt.
# # # #
# # # # 0. Definiere die Funktion: def min_max(zahlen_liste):
# # def min_max(zahlen_liste):
# #     # 1. Die Funktion berechnet das Minimum und Maximum der Liste
# #     #    TIPP: min() und max() Funktionen verwenden
# #     min_wert = min(zahlen_liste)
# #     max_wert = max(zahlen_liste)
    
# #     # 2. Die Funktion gibt beide Werte zurück (TIPP: return min_wert, max_wert)
# #     return min_wert, max_wert

# # # 3. Erstelle eine Liste mit beliebigen Zahlen
# # # BEISPIEL 1:
# # liste_beispiel_1 = [5, 2, 8, 1, 9]

# # # 4. Rufe die Funktion auf und speichere beide Rückgabewerte
# # minimum_1, maximum_1 = min_max(liste_beispiel_1)

# # # 5. Gib Minimum und Maximum aus
# # print(f"Liste: {liste_beispiel_1} -> Minimum: {minimum_1}, Maximum: {maximum_1}")


# # # BEISPIEL 2:
# # liste_beispiel_2 = [3.5, 2.1, 7.8, 4.2]

# # # 4. Rufe die Funktion auf und speichere beide Rückgabewerte (für das zweite Beispiel)
# # minimum_2, maximum_2 = min_max(liste_beispiel_2)

# # # 5. Gib Minimum und Maximum aus (für das zweite Beispiel)
# # print(f"Liste: {liste_beispiel_2} -> Minimum: {minimum_2}, Maximum: {maximum_2}")


# # #
# # AUFGABE 9: FUNKTION MIT SCHLEIFE (MITTEL)
# #
# # Schreibe eine Funktion, die eine Liste von Namen bekommt
# # und jeden Namen mit einer Begrüßung ausgibt.
# #
# # 0. Definiere die Funktion: def begruesse_alle(namen_liste):
# # 1. Die Funktion geht mit einer for-Schleife durch die Liste
# # 2. Für jeden Namen wird "Hallo [name]!" ausgegeben
# # 3. Erstelle eine Liste mit 5 Namen (OHNE Benutzereingabe)
# # 4. Rufe die Funktion mit der Liste auf
# #
# # BEISPIEL:
# # Liste: ["Anna", "Ben", "Clara", "David", "Emma"]
# # Ausgabe:
# # Hallo Anna!
# # Hallo Ben!
# # Hallo Clara!
# # Hallo David!
# # Hallo Emma!
# #

# # # AUFGABE 10: FUNKTIONEN ZUSAMMENSETZEN (SCHWER)
# # #
# # # Schreibe mehrere kleine Funktionen, die zusammen ein Programm ergeben.
# # #
# # # 0. Definiere die Funktionen:
# # #    0.a def eingabe_zahl(prompt): gibt input als float zurück
# def eingabe_zahl(prompt):
#     return float(input(prompt))

# # #    0.b def berechne_flaeche(breite, hoehe): gibt breite * hoehe zurück
# def berechne_flaeche(breite, hoehe):
#     return breite * hoehe

# # #    0.c def ausgabe(flaeche): gibt "Die Fläche ist: [flaeche]" aus
# def ausgabe(flaeche):
#     print(f"Die Fläche ist: {flaeche}")

# # # 1. Rufe die Funktionen in der richtigen Reihenfolge auf:
# # #    1.a Breite mit eingabe_zahl() einlesen
# breite_eingabe = eingabe_zahl("Breite: ")

# # #    1.b Höhe mit eingabe_zahl() einlesen
# hoehe_eingabe = eingabe_zahl("Höhe: ")

# # #    1.c Fläche mit berechne_flaeche() berechnen
# ergebnis_flaeche = berechne_flaeche(breite_eingabe, hoehe_eingabe)

# # #    1.d Ergebnis mit ausgabe() anzeigen
# ausgabe(ergebnis_flaeche)
# #
# # 

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




#==================================THEMA: MODULARISIEREN &TYPE ANNOTATIONS==================================
#
# THEMA: Funktionen in Module auslagern und mit Type Hints arbeiten
#
# HINWEIS: Für diese Aufgaben brauchst du mehrere Dateien.
# Erstelle folgende Dateien im gleichen Ordner:
# - main.py (Hauptprogramm)
# - rechner.py (Rechner-Funktionen)
# - hilfe.py (Hilfsfunktionen)
# - daten.py (Datenbank-Funktionen)
#

#
# AUFGABE 1: EINFACHE MODULARISIERUNG (EINFACH)
#
# Lagere einfache Funktionen in separate Module aus.
#
# 1. Erstelle die Datei 'rechner.py' mit folgenden Funktionen:
#    1.a def addieren(a: float, b: float) -> float:
#    1.b def subtrahieren(a: float, b: float) -> float:
#    1.c def multiplizieren(a: float, b: float) -> float:
#    1.d def dividieren(a: float, b: float) -> float:
#         TIPP: Bei Division durch 0 eine Fehlermeldung ausgeben
#
# 2. In 'main.py' importiere die Funktionen aus 'rechner.py'
# 3. Der Benutzer gibt 2 Zahlen und eine Operation ein
# 4. Rufe die passende Funktion auf
# 5. Gib das Ergebnis mit korrekter Type Annotation aus
#
# BEISPIEL:
# Erste Zahl: 10
# Zweite Zahl: 5
# Operation (+, -, *, /): +
# Ergebnis: 10 + 5 = 15
#

#
# AUFGABE 2: MEHRERE MODULE (MITTEL)
#
# Erstelle drei Module mit verschiedenen Funktionalitäten.
#
# 1. Erstelle 'hilfe.py' mit:
#    1.a def zeige_menu() -> None:
#         Gibt ein Menü aus
#    1.b def eingabe_zahl(prompt: str) -> float:
#         Nimmt eine Zahl als input und gibt sie als float zurück
#    1.c def bestaetigung(prompt: str) -> bool:
#         Gibt True zurück bei "ja", sonst False
#         TIPP: Verwende .lower() für die Eingabe
#
# 2. Erstelle 'daten.py' mit:
#    2.a def speichere_daten(dateiname: str, daten: dict) -> None:
#         Speichert ein Wörterbuch in eine Datei
#         TIPP: Verwende open() mit "w" und write()
#    2.b def lade_daten(dateiname: str) -> dict:
#         Lädt ein Wörterbuch aus einer Datei
#         TIPP: Verwende open() mit "r" und read()
#
# 3. In 'main.py' importiere die Funktionen aus beiden Modulen
# 4. Verwende die Funktionen für ein kleines Programm
#
# BEISPIEL:
# hilfe.zeige_menu()
# zahl1 = hilfe.eingabe_zahl("Erste Zahl: ")
# if hilfe.bestaetigung("Speichern? "):
#     daten.speichere_daten("zahlen.txt", {"zahl1": zahl1})
#
#
# AUFGABE 1: EINFACHE MODULARISIERUNG (EINFACH)
#
# Lagere einfache Funktionen in separate Module aus.
#
# 1. Erstelle die Datei 'rechner.py' mit folgenden Funktionen:
#    1.a def addieren(a: float, b: float) -> float:
#    1.b def subtrahieren(a: float, b: float) -> float:
#    1.c def multiplizieren(a: float, b: float) -> float:
#    1.d def dividieren(a: float, b: float) -> float:
#         TIPP: Bei Division durch 0 eine Fehlermeldung ausgeben

def addieren(a: float, b: float) -> float:
    return a + b

def subtrahieren(a: float, b: float) -> float:
    return a - b

def multiplizieren(a: float, b: float) -> float:
    return a * b

def dividieren(a: float, b: float) -> float:
    if b == 0:
        print("Fehler: Division durch Null ist nicht erlaubt!")
        return 0.0
    return a / b


#
# AUFGABE 2: MEHRERE MODULE (MITTEL)
#
# Erstelle drei Module mit verschiedenen Funktionalitäten.
#
# 1. Erstelle 'hilfe.py' mit:
#    1.a def zeige_menu() -> None:
#         Gibt ein Menü aus
#    1.b def eingabe_zahl(prompt: str) -> float:
#         Nimmt eine Zahl als input und gibt sie als float zurück
#    1.c def bestaetigung(prompt: str) -> bool:
#         Gibt True zurück bei "ja", sonst False
#         TIPP: Verwende .lower() für die Eingabe

def zeige_menu() -> None:
    print("\n--- HAUPTMENÜ ---")
    print("1. Rechner starten")
    print("2. Zahl speichern")
    print("3. Beenden")

def eingabe_zahl(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungültige Eingabe! Bitte eine Zahl eingeben.")

def bestaetigung(prompt: str) -> bool:
    antwort = input(prompt).lower().strip()
    return antwort in ["ja", "j", "yes", "y"]


#
# AUFGABE 3: DATENBANK-MODUL MIT TYPE ANNOTATIONS (MITTEL)
#
# Erstelle ein Modul für eine einfache Datenbank von Benutzern.
#
# 1. Erstelle 'user_db.py' mit:
#    1.a def benutzer_hinzufuegen(datenbank: dict, name: str, alter: int) -> dict:
#         Fügt einen neuen Benutzer zur Datenbank hinzu
#         Gibt die aktualisierte Datenbank zurück
#    1.b def benutzer_loeschen(datenbank: dict, name: str) -> dict:
#         Löscht einen Benutzer aus der Datenbank
#         Gibt die aktualisierte Datenbank zurück
#    1.c def benutzer_suchen(datenbank: dict, name: str) -> dict | None:
#         Sucht einen Benutzer und gibt ihn zurück (oder None)
#    1.d def zeige_alle_benutzer(datenbank: dict) -> None:
#         Gibt alle Benutzer aus
#    1.e def durchschnittsalter(datenbank: dict) -> float:
#         Berechnet das Durchschnittsalter aller Benutzer
#
# 2. In 'main.py' importiere die Funktionen
# 3. Erstelle ein Menü für die Benutzerverwaltung
# 4. Verwende Type Annotations für alle Funktionen
# 5. TIPP: Für Typ | None verwende from typing import Optional oder Union
#    ODER: from typing import Optional, dann Optional[dict]
#
# BEISPIEL:
# db = {}
# db = user_db.benutzer_hinzufuegen(db, "Anna", 25)
# db = user_db.benutzer_hinzufuegen(db, "Ben", 30)
# user_db.zeige_alle_benutzer(db)
# durchschnitt = user_db.durchschnittsalter(db)
# print("Durchschnittsalter:", durchschnitt)
#

#
# AUFGABE 4: FUNKTIONEN MIT DEFAULT-WERTEN UND ANNOTATIONS (MITTEL)
#
# Erstelle Funktionen mit Type Annotations und Default-Werten.
#
# 1. Erstelle 'formatierer.py' mit:
#    1.a def zentriere_text(text: str, breite: int = 50) -> str:
#         Zentriert den Text in einer Zeile der gegebenen Breite
#         TIPP: Verwende text.center(breite)
#    1.b def trennlinie(zeichen: str = "-", laenge: int = 50) -> str:
#         Erstellt eine Trennlinie aus dem Zeichen
#         TIPP: Verwende zeichen * laenge
#    1.c def ausgabe_mit_rahmen(text: str, zeichen: str = "*") -> None:
#         Gibt den Text mit einem Rahmen aus
#         TIPP: Kombiniere zentriere_text und trennlinie
#    1.d def farbiger_text(text: str, farbe: str = "gruen") -> str:
#         Gibt den Text in einer Farbe zurück
#         TIPP: ANSI-Farbcodes verwenden
#
# 2. In 'main.py' importiere die Funktionen
# 3. Teste die Funktionen mit verschiedenen Parametern
#
# BEISPIEL:
# formatierer.zentriere_text("Hallo Welt")
# formatierer.trennlinie("=", 30)
# formatierer.ausgabe_mit_rahmen("Wichtig!", "#")
# print(formatierer.farbiger_text("Fehler", "rot"))
#

#
# AUFGABE 5: KOMPLEXE TYPE ANNOTATIONS (SCHWER)
#
# Verwende komplexere Type Annotations für Listen, Dictionaries und Optionale Werte.
#
# 1. Erstelle 'statistik.py' mit:
#    1.a from typing import List, Dict, Optional, Union
#    1.b def berechne_durchschnitt(zahlen: List[float]) -> float:
#         Berechnet den Durchschnitt einer Liste
#    1.c def finde_maximum(zahlen: List[float]) -> Optional[float]:
#         Findet das Maximum oder gibt None zurück bei leerer Liste
#    1.d def haeufigkeit(woerter: List[str]) -> Dict[str, int]:
#         Zählt die Häufigkeit von Wörtern in einer Liste
#    1.e def zusammenfuegen(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
#         Fügt zwei Wörterbücher zusammen (addiert Werte bei gleichen Schlüsseln)
#    1.f def filtere_dict(daten: Dict[str, int], grenze: int) -> Dict[str, int]:
#         Filtert ein Wörterbuch nach Werten (nur Werte > grenze behalten)
#
# 2. In 'main.py' importiere die Funktionen
# 3. Teste die Funktionen mit verschiedenen Daten
# 4. Verwende die Type Hints korrekt mit List, Dict, Optional
#
# BEISPIEL:
# zahlen = [1, 2, 3, 4, 5]
# durchschnitt = statistik.berechne_durchschnitt(zahlen)
# max_wert = statistik.finde_maximum(zahlen)
# woerter = ["a", "b", "a", "c", "b", "a"]
# haeufigkeit = statistik.haeufigkeit(woerter)
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# merged = statistik.zusammenfuegen(dict1, dict2)
#

#
# AUFGABE 6: DATENBANK MIT FUNKTIONEN (SCHWER)
#
# Erstelle eine vollständige Datenbank mit Funktionen für eine Bibliothek.
#
# 1. Erstelle 'bibliothek.py' mit:
#    1.a from typing import Dict, List, Optional, Tuple
#    1.b def buch_hinzufuegen(bibliothek: Dict[str, Dict], titel: str, autor: str, jahr: int) -> Dict:
#         Fügt ein Buch zur Bibliothek hinzu
#         Struktur: { "titel": {"autor": "Name", "jahr": 2024} }
#    1.c def buch_loeschen(bibliothek: Dict[str, Dict], titel: str) -> Dict:
#         Löscht ein Buch aus der Bibliothek
#    1.d def buch_suchen(bibliothek: Dict[str, Dict], suchbegriff: str) -> List[Tuple[str, Dict]]:
#         Sucht nach Büchern (Titel oder Autor)
#         Gibt eine Liste von (titel, buch_info) zurück
#    1.e def buecher_nach_jahr(bibliothek: Dict[str, Dict], jahr: int) -> List[str]:
#         Gibt alle Bücher aus einem bestimmten Jahr zurück
#    1.f def zeige_bibliothek(bibliothek: Dict[str, Dict]) -> None:
#         Gibt alle Bücher aus
#    1.g def durchschnittsjahr(bibliothek: Dict[str, Dict]) -> float:
#         Berechnet das durchschnittliche Erscheinungsjahr
#
# 2. In 'main.py' importiere die Funktionen
# 3. Erstelle ein Menü für die Bibliotheksverwaltung
# 4. Verwende Type Hints für alle Funktionen
# 5. TIPP: Für komplexe Typen importiere Dict, List, Tuple, Optional
#
# BEISPIEL:
# bibliothek = {}
# bibliothek = bibliothek.buch_hinzufuegen(bibliothek, "Python 101", "Max", 2023)
# bibliothek = bibliothek.buch_hinzufuegen(bibliothek, "Data Science", "Anna", 2024)
# suchergebnisse = bibliothek.buch_suchen(bibliothek, "Python")
# bibliothek.zeige_bibliothek(bibliothek)
# durchschnitt = bibliothek.durchschnittsjahr(bibliothek)
# print("Durchschnittsjahr:", durchschnitt)
#

#
# ALLGEMEINE TIPS FÜR ALLE AUFGABEN:
#
# - Type Annotations: def funktion(parameter: typ) -> rueckgabetyp:
# - Wichtige Typen: int, float, str, bool, None, List, Dict, Tuple, Optional
# - Optional verwenden: Optional[Dict] oder Union[Dict, None]
# - Module importieren: import modulname oder from modul import funktion
# - Module müssen im gleichen Ordner oder im PYTHONPATH sein
# - Verwende from typing import List, Dict, Optional, Union, Tuple
# - Module werden mit def und Code in einer .py-Datei erstellt
# - Die Hauptdatei (main.py) importiert und verwendet die Funktionen
# - Bei "from module import *" importiert man alles (nicht empfohlen)
# - Spezifische Importe sind besser: from module import funktion1, funktion2
#
# DOKUMENTATION:
# - Type Hints: https://docs.python.org/3/library/typing.html
# - Module: https://docs.python.org/3/tutorial/modules.html
# - Import: https://docs.python.org/3/reference/import.html