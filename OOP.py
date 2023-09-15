#Atgādne

#OOP
#Galvenie jēdzieni
#Klase - ir veidne (template)
#īpašības 
#metodes def
#konstruktors - īpašību inicializācija __init__
#Objekti - klases piemērs (instance)

class Masinas():
    #konstruktors
    #self jābūt vienmēr
    def __init__(self, bakasTilpums, pasazieruSkaits, motoraTilpums, motoraJauda):
        self.bakasTilpums = bakasTilpums
        self.pasazieruSkaits = pasazieruSkaits
        self.motoraTilpums = motoraTilpums
        self.motoraJauda = motoraJauda

audi = Masinas(55,5,2,130)
print(audi.motoraJauda)