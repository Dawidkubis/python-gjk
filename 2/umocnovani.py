

# ziskame zaklad
a = int(input("zadejte zaklad : "))
# ziskame exponent
e = int(input("zadejte exponent  : "))

i = 0 # tohle je iteracni promenna
# budeme totiz loopovat tolikrat, kolik mame exponent
# coz je trochu problem protoze exponent musi
# byt cele cislo
# no nic

prod = 1 # do tyhle promenny to budeme vsechno nasobit
# pozor; nemuze byt 0 protoze by nula je nulovy prvek
# grupy celych cisel s nasobenim; to je jedno
# proste by nam pohltila cely nasobeni a vysledek
# by byl nula

while i < e:
    
    prod *= a

    i += 1

print(prod)
