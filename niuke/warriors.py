import random
import math
class Warriors:
    def __init__(self,name,Kungfu,attkMax,defendMax):
        self.name = name
        self.energyValue = Kungfu
        self.attkMax = attkMax
        self.defendMax = defendMax

    def attack(self):
        return self.attkMax * (random.random() + .5)

    def defend(self):
        return self.defendMax * (random.random() + .5)


class Battles:
    def launchAtack(self, warrior1, warrior2):
        while True:
           if self.fight(warrior1,warrior2) == "Game over":
               print("Game over")
               break
           if self.fight(warrior2, warrior1) == "Game over":
                print("Game over")
                break


    def fight(warriorA,warriorB):
        attkAmount = warriorA.attack()
        defendAmount = warriorB.defend()
        damage2warriorB = math.ceil(attkAmount - defendAmount)
        warriorB.energyValue = math.ceil(warriorB.energyValue - damage2warriorB)
        print("{}进攻，{}防守，伤害值{}，{}战斗值下降为{}".format(
            warriorA.name, warriorB.name, damage2warriorB, warriorB.name, warriorB.energyValue))
        if warriorB.energyValue <= 0:
            return "Game over"

        else:
            return "Continue fight"

blowSnow = Warriors("西门吹雪", 50, 20, 10)
loneCity = Warriors("独孤城",50, 20, 10)
Battles.fight(blowSnow, loneCity)


for i in range(1,10):
    print(i)