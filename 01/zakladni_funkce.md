# Základní funkce
V naší první hodině jsme probrali několik funkcí. 
Funkce je kus kódu, který můžeme volat na vícero místech (to si ale do detailu probereme později).

## Syntax volání
Nyní potřebujete znát hlavně základní syntax volání funkcí. Funkce může dostávat nějaké argumenty, což jsou jakési vstupy, které funkce zpracovává.
Různé funkce mají různý počet argumentů.
Je to asi nějak takhle:
```python
jmeno_funkce(argument1, argument2, ...)
```
Funkce může vracet nějaký výstup, který si můžeme například uložit do proměnné. Třeba takhle:
```python
ahoj = nejaka_funkce()
```

## Pár funkcí do základní výbavy
My jsme probrali několik funkcí. 
### print
Nejzákladnější je funkce `print`. Ta bere neomezený počet argumentů, které spojí mezerou a vypíše do konzole.
Příklad
```python
print("Hello World")

jmeno = "Dawid"
print("Ahoj", jmeno) # Vypíše Ahoj Dawid
```

### input
Dále jsme probrali funkci `input`. Ta bere maximálně jeden argument. 
Funguje tak, že čeká, dokud uživatel nezadá nějaký vstup a zmáčkne enter a vrátí vstup, který uživatel zadal. 
Když dostane argument, tak jej vypíše uživateli před místo, kam zadává vstup.

```python
jmeno = input("Zadej prosím své jméno.")
```

### int
Jako poslední jsme probrali funkci int (což je spíše datový typ, ale my budeme předstírat, že je to funkce). 
Ta nám převede nějaký string (zadaný jako argument) na celé číslo, pokud je to možné. Jestliže to možné není, tak hodí chybu (později se naučíme, jak se s takovouhle chybou vyrovnat).

Příklad:
```python
ahoj = "1234" # Všimněte si, že ahoj je string (typ str)
ahoj_cislo = int(ahoj) # ahoj_cislo je nyní celé číslo
```
