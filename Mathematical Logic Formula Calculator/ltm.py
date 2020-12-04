import re
pattern = "[a-uw-z]"
letters = []
print("Format wpisywania danych: ")
print("~ negacja")
print("^ koniunkcja")
print("v alternatywa")
print("<=> równoważność")
print("=> implikacja")
print("Proszę zwrócić uwagę, że pomiędzy znakami musi być spacja np. ( ( p ^ q ) v r => s ) <=> t")
print("Proszę podać formułę klasycznego rachunku zdań: ")
zol = input()
for element in zol:
    if re.search(pattern, element):
        if element not in letters:
            letters.append(element)
letters.sort()
zol = zol.replace("^", "&")
zol = zol.replace("v", "|")
zol = zol.replace("<=>", "==")
zol = zol.replace("=>", "<=")
cnfpart = []
for permutation in range(pow(2,len(letters))):
    temporaryzol = zol
    binary = bin(permutation)[2:].zfill(len(letters))
    temporary = 0
    for number in binary:
        temporaryzol = temporaryzol.replace(letters[temporary], number)
        temporary = temporary + 1
    temporaryzol = temporaryzol.replace("~ 0", "1")
    temporaryzol = temporaryzol.replace("~ 1", "0")
    if (eval(temporaryzol) == False):
        cnfpart.append(binary)
cnfpart.reverse()
cnf = ""
temporary = 0
for element in cnfpart:
    temporary1 = 0
    cnf += "( "
    for number in element:
        if (number == "0"):
            cnf += letters[temporary1]
            if (temporary1 != len(letters) - 1):
                cnf += " v "
        elif (number == "1"):
            cnf += "~ "
            cnf += letters[temporary1]
            if (temporary1 != len(letters) - 1):
                cnf += " v "
        temporary1 = temporary1 + 1
    if (temporary != len(cnfpart) - 1):
        cnf += " ) ^ "
    else:
        cnf += " )"
    temporary = temporary + 1
if (cnf == ""):
    cnf += "( " + letters[0] + " v ~ " + letters[0] + " )"
print(cnf)
brackets = 0
for element in cnf:
    if (element == "("):
        brackets = brackets + 1
for letter in letters:
    cnf = cnf.replace("~ " + letter, letter.upper())
cnf = cnf.replace(" ^ ", "^")
cnf = cnf.replace("( ", "")
cnf = cnf.replace(" )", "")
cnf = cnf.replace(" v ", "")
temporary = cnf.split("^")
oppositeletters = 0
for element in temporary:
    for piece in element:
        if (piece.isupper()):
            pattern = piece.lower()
            if re.search(pattern, element):
                oppositeletters = oppositeletters + 1
                break
if (brackets == oppositeletters):
    print("Formuła jest tautologią klasycznego rachunku zdań.")
else:
    print("Formuła nie jest tautologią klasycznego rachunku zdań.")