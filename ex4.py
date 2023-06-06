"""
Scrieţi un program care verifică dacă litera "a" se află pe a 2-a poziţie într-un String citit de la tastatură.
"""

sir = input("Introduceți un șir de caractere: ")


if len(sir) >= 2 and sir[1] == 'a':
    print("Litera 'a' se află pe a doua poziție în șirul citit.")
else:
    print("Litera 'a' nu se află pe a doua poziție în șirul citit.")