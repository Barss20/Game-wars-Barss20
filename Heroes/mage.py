from Heroes.hero import Hero


class Mage(Hero):

    def heal(self, hero):
        if hero is self:
            print('Cannot heal myself!')
            return
        elif hero.health >= 100:
            print(f'{hero.name} has maximum health points already')
            return
        elif hero.health < 100 and hero.money >= (100 - hero.health):
            heal_points = (100 - hero.health)
            hero.health += heal_points
            hero.power = hero.health * 0.1
            hero.money -= heal_points
            self.money += heal_points


if __name__ == '__main__':
    mage = Mage(name='Mage', health=100, rank=1, power=10, defence=20)
    print(mage)