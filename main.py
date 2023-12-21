#Zhenchen Xu POO3 407
import random

def roll_attribute():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)
    list1 = [dice1, dice2, dice3, dice4]
    list1.sort()
    list1.pop(0)
    return list1[0] + list1 [1] + list1 [2]

class NPC():
    def __init__(self):
        self.Force = roll_attribute()
        self.Agility = roll_attribute()
        self.Consitution = roll_attribute()
        self.Intelligence = roll_attribute()
        self.Sagesse = roll_attribute()
        self.Charisme = roll_attribute()
        self.Armour = random.randint(1,12)
        self.Nom = 'Stratogerelasaurus'
        self.Race = 'Blue'
        self.Espece = 'Helicopter'
        self.PDV = random.randint(1,20)
        self.Profession = 'Procastinator'

    def afficher_caracteristiques(self):
        print(str(self.Force))
        print(str(self.Agility))
        print(str(self.Consitution))
        print(str(self.Intelligence))
        print(str(self.Sagesse))
        print(str(self.Charisme))
        print(str(self.Armour))
        print(str(self.Nom))
        print(str(self.Race))
        print(str(self.Espece))
        print(str(self.PDV))
        print(str(self.Profession))

class kobold(NPC):
    def __init__(self):
        super().__init__()
    def attaquer(self, cible):
        pass
    def subir_dommage(self, dommage):
        pass
class Heros(NPC):
    def __init__(self):
        super().__init__()
    def attaquer(self, cible):
        pass
    def subir_dommage(self, dommage):
        pass
