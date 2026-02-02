from Hero import Hero


print("\n== SUMMON PARTY HERO ==")
alucard  = Hero("Alucard", 120,"warior")
eudora  = Hero("Eudora",  80,",mage")
angela = Hero("Angela", 90,"healer")


print("\n== MUNCUL GOBLIN ==")
goblin = Hero("Goblin",60 ,"Monster", "normal")

print("\n== PARTY MELAWAN GOBLIN ==")
alucard.attack(goblin, 20)
eudora.attack(goblin, 30)
eudora.attack(goblin, 40)
goblin.attack(eudora,20)

print("\n== MUNCUL RAJA IBLIS ==")
boss = Hero("Raja Iblis", 200,"Bos", "bos")

print("\n== PARTY MELAWAN RAJA IBLIS ==")
alucard.attack(boss, 40)
eudora.attack(boss, 50)
alucard.attack(boss, 30)

print("\n== RAJA IBLIS BALAS MENYERANG ==")
boss.attack(alucard, 25)

print("\n== HEALER MENOLONG ==")
angela.heal()
