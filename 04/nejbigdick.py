# tady te mam docente
def gp(n):
    return [n[0]] + gp([i for i in n[1:] if i%n[0] != 0]) if n else [] # mnohem rychlejsi

print(gp(range(2, int(input('zadej cislo : ')))))
# touche
