class Hero:
    # pertama kali dipanggil (summon)
    # self = dirinya sendiri / internal
    def __init__(self, name, hp, job,hero_type="hero"):
        self.name = name
        self.job = job
        self.hp = hp
        self.max_hp = hp
        self.type=hero_type

        if self.job =="warior":
            self.hp += 40
        print(f"✨ [{job}] Hero {self.name} telah di summon!")

    def is_alive(self):
        return self.hp > 0

    def heal(self):
        if not self.is_alive():
            print(f"woi dah mati si {self.name}  ")
            return
        
        if self.job == "healer":
            heal_amount=30
        elif self.job == "warior":
            heal_amount=20
        else:
            heal_amount=10

        if self.hp > self.max_hp:
         self.hp = self.max_hp

        self.hp += heal_amount

        print(f"🧪 {self.name} meminum potion...")
        print(f"💚 HP {self.name} bertambah +{heal_amount}")

    def take_damage(self, damage):
        # self.hp = self.hp - damage (aslinya)
        self.hp -= damage

        if self.hp < 0:
            self.hp=0

        print(f"💥 {self.name} terkena {damage} damage\n")
        # print(f"💚 Sisa HP: {self.hp}")
        if self.hp == 0:
            print(f"🚫 {self.name} tereliminasi dari arena!")
    
    def attack(self, enemy, damage):
        
        if not self.is_alive():
            print (f"woi {self.name}nya dah mati nggak nyerang")
            return
        if damage <= 0 :
            print(f"woi {self.name}yng bener lah masa nggak ada damage ")
            return
        if self.type == "bos" and self.hp <= self.max_hp /2 :
            print (f"hayo bos {self.name} marah loh ")
            damage *= 2

        if self.job == "mage":
            damage += 15
        print(f"⚔️ {self.name} menyerang {enemy.name}!")
        # panggil method lain dari dalam
        enemy.take_damage(damage)

    # fungsi cek status terkini 
    def __str__(self):
        status = "🟢 HIDUP" 
        if self.hp == 0:
            status = "💀 MATI" 

        return f"[{self.job}] {self.name} | HP: {self.hp} | {status}"
    
   