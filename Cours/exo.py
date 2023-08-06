TEST_ARRAY = [1, 2, 6, 4, 2, 2, 7, 3, 0, 6, 4, 5, 2]
TEST_STRINGS = ['laval', 'jesus']


# Niveau 2
# Version plus dure:
# Le faire en 4 lignes sans casser la convention de style PEP8
# def triangle(number):
#
#     for etage in range(number+1):
#         if etage > 2 and etage != number:
#             print("X"+"O"*(etage-2)+"X")
#         else :
#             print("X"*etage)

# Niveau 1
# def higher_or_lower(number):
#
#     while True:
#         choix = int(input(" >"))
#         if choix > number :
#             print("moins")
#         elif choix < number :
#             print("plus")
#         else :
#             break
#
# higher_or_lower(5)


# Niveau 3
# Version plus dure:
# Le faire en au moins 6 lignes sans casser la convention de style PEP8
last = -1
last_last=0
def fibonacci(count):
    global last, last_last
    if count > 0 :
        lapin = last + last_last
        print(lapin)
        last_last = last
        last = lapin
        fibonacci(count-1)



# Niveau 1
# def find_last(array, number):
#     temp = -1
#     for index, value in enumerate(array) :
#         if number == value :
#             temp = index
#     if temp == -1 :
#         print("existe po")
#     else :
#         print(temp+1)



# Niveau 3
def gnome(array):
    pass


# Niveau 2
# Version plus dure:
# Le faire en 4 lignes sans casser la convention de style PEP8
# def palindrom(string):
#     good_lettre = 0
#     for index, lettre in enumerate(string) :
#         if lettre != string[-index-1] :
#             print("Ce n'est pas un palindrom")
#             break
#         else :
#             good_lettre += 1
#     if good_lettre == len(string):
#         print("C'est un palindrome")


# triangle(10)

fibonacci(10)
# find_last(TEST_ARRAY, 2)
gnome(TEST_ARRAY)

# palindrom("kayayk")
