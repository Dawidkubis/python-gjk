# yeehaw
# budeme hledat prvocisla
# fakt super
# zacnu od udelani funkce ktera bere
# horni hranici intervalu a vrati mi seznam
# vsech prvocisel do tyto hranice

# generate_primes(10) ma vyhodit [2, 3, 5, 7]
def generate_primes(lim): # lim je horni hranice intervalu
    nums = list(range(2, lim)) # seznam vsech cisel od 2 do lim
    primes = [] # prazny seznam
    
    x = nums[0] # ulozime si prvni cislo
    # ktery je prvocislo
    while x < int(lim**0.5): # staci ze hledam do odmocniny z lim
        # teoreticky bych mohl napsat jenom
        # while nums[0] < lim
        # ale je to pomalejsi
        # jo a int() mi z toho udela cele cislo
        # coz odmocnina neni
        x = nums[0] # aktualizace x, ma smysl az po prvnim cyklu 
        # prvocislo

        temp = [] # temporary seznam do kteryho budeme kopirovat

        primes.append(x) # ukladame prvocislo do seznamu prvocisel

        for i in nums: # prochazime nums a snazime se rasove cistit
            # cili nechat jenom cisla ktery nejsou delitelna nove pridanym
            # prvocislem
            if i % x:
                temp.append(i) # temp nam slouzi jako budouci nums

        nums = temp # pozirame temp a aktualizujeme nums

    primes += nums # jinak by mi chybely cisla protoze jsem nahore
    # napsal : 
    # while x< int(lim**0.5)
    # kdybych to tam nenapsal tak tohle muzu vynechat

    return primes # vracim cisla

print(generate_primes(int(input("zadej cislo : "))))
# tohle je mozna trochu prasacky
# mohl jsem to rozepsat jako : 

# i = int(input("zadej cislo : "))
# print(generate_primes(i))

# ale nechtelo se mi lol
