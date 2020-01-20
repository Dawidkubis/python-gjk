#!/usr/bin/python

from math import gcd # importuju greatest common divisor
					 # aby se mi snaz kratily zlomky

# definujeme novou tridu
class Fraction:
	
	# definujeme co se ma dit pri vytvoreni objektu
	def __init__(self, up, down):
		self.up = up # self.up != up
		self.down = down
		self.base() # bude se hodit pri zbytku implementaci
					# zarucuje ze nebudeme muset explicitne volat
					# metodu `base` nikde jinde

	# kraceni zlomku
	# vsimneme si ze narozdil od funkci, u metod
	# je v pohode i jiny typ vraceni z funkce nez
	# jenom pomoci `return`
	# - metoda muze menit objekt kterymu nalezi
	def base(self):
		divisor = gcd(self.up, self.down) # ziskavame nejvedsi spolecny delitel
		if divisor > 1: # zjistujeme jestli muzeme kratit
			self.up = self.up // divisor # znena sebe sama
			self.down = self.down // divisor # a zase

		if self.up < 0 and self.down < 0:
			self.up = -self.up
			self.down = -self.down


	# scitani zlomku
	def add(self, other):
		return Fraction(self.up * other.down + other.up * self.down, self.down * other.down)
				# ^- tohle mi zaruci ze se ten zlomek automaticky zkrati
				# jelikoz tvorim novy objekt a v initu mam `self.base()`
				# taky vracim jiny objekt a nemenim ty, ktere jsem dostal

	# nasobeni zlomku
	def multiply(self, other):
		return Fraction(self.up * other.up, self.down * other.down)
	
	# odcitani zlomku
	def subtract(self, other):
		return Fraction(self.up * other.down - other.up * self.down, self.down * other.down)
	
	# deleni
	# prosim tady nepouzivat pythonovsky deleni, je velice nepresny
	def divide(self, other):
		return Fraction(self.up * other.down, self.down * other.up)

	# aby se mi to hezky printlo
	def show(self):
		return f"{self.up}/{self.down}"

# testy

for x in range(1, 4):
	for y in range(1, 4):
		a = Fraction(x, y)
		b = Fraction(y, x)

		print(f"\na: {a.show()}\nb: {b.show()}\n")

		print("+", a.add(b).show())
		print("*", a.multiply(b).show())
		print("-", a.subtract(b).show())
		print("/", a.divide(b).show())

# ez
