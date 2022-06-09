from Items import Sword, Shield
from Heroes import Hero, Mage
from Merchant import Merchant
from arena import Arena

barsik = Hero(name='Barsik', health=100, rank=1, power=9, defence=90)
son = Hero(name='Son', health=100, rank=1, power=4, defence=80)
ben = Hero(name='Ben', health=100, rank=2, power=4, defence=100)
vasya = Mage(name='Vasya', health=100, rank=1, power=10, defence=20)

adidas = Merchant(name='Adidas')

# create swords and shields
gladius = Sword(name='Gladius', price=20, power_bonus=2)
knightSword = Sword(name='Knight Sword', price=30, power_bonus=3)
longSword = Sword(name='Long Sword', price=40, power_bonus=4)
runicSword = Sword(name='Runic Sword', price=50, power_bonus=5)
orcSlayer = Sword(name='Orc Slayer', price=60, power_bonus=6)
woodenShield = Shield(name='Wooden Shield', price=20, defence_bonus=20)
vikingShield = Shield(name='Viking Shield', price=30, defence_bonus=30)
guardianShield = Shield(name='Guardian Shield', price=40, defence_bonus=40)
paladinShield = Shield(name='Paladin Shield', price=50, defence_bonus=50)
aegis = Shield(name='Aegis', price=60, defence_bonus=6)


adidas.goods['swords'].extend((gladius, knightSword, longSword, runicSword, orcSlayer))
adidas.goods['shields'].extend((woodenShield, vikingShield, guardianShield, paladinShield, aegis))


arena1 = Arena(name='Arena 1', prize_fund=200)


print(adidas)


barsik.buy_equipment(adidas, gladius)
barsik.buy_equipment(adidas, woodenShield)
son.buy_equipment(adidas, longSword)
son.buy_equipment(adidas, vikingShield)


barsik.equip(gladius)
barsik.equip(woodenShield)
son.equip(longSword)
son.equip(vikingShield)


print(adidas)

print(barsik)
print(son)
print(arena1)


arena1.tournament(barsik, son)

print(barsik)
print(son)
print(arena1)

vasya.heal(barsik)
vasya.heal(son)

print(barsik)
print(son)
print(vasya)

barsik.sell_equipment(adidas, gladius)
barsik.sell_equipment(adidas, woodenShield)
son.sell_equipment(adidas, longSword)
son.sell_equipment(adidas, vikingShield)
print(barsik)
print(son)
print(adidas)