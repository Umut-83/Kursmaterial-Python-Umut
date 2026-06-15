#Einen Rechner mit den vier Grundrechnenoperationen schreibt

#1. Nehme durch das Terminal zwei Operatoren als Eingabe und speichere diese
    #1.1 input()....
    #1.2 in variablen speichern

first_operator = float(input("Gebe eine Zahl ein:\n"))
second_operator = float(input("Gebe eine Zahl ein:\n"))


#Tip input typecasting (umwandeln in anderen Datentypen)
# user_number = float(input("Gebe eine Zahl ein:\n"))
# user_number = user_number + 2
# print(user_number)
# user_number = user_number * 2
# print(user_number)


#2. Führe mit alle Grundrechenoperation mit den Operatoren aus
   #2.1 Speichere das Ergebnis in jeweils einer Variablen
result_div = first_operator / second_operator
result_mul = first_operator * second_operator
result_add = first_operator + second_operator
result_sub = first_operator - second_operator


#3. Gebe die Ergebnisse einzeln oder als Ganzes aus
  #3.1 f-String im print (f"... {...}...")
#print(f"result divide: {result_div}\nresult sub: {result_sub}\nresult mul: {result_mul}\nresult div: {result_div}")
# print(f"""
# result divide: {result_div}
# result sub: {result_sub}
# result mul: {result_mul}
# result div: {result_div}
# """)
print("result divide:" ,result_div, "result sub: ", result_sub, "result mul: ", result_mul, "result div: ",result_div)