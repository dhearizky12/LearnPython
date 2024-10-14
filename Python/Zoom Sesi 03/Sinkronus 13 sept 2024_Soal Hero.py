# Membuat class Hero
class Hero:
    total_heroes = 0  # Atribut kelas untuk menghitung jumlah hero

    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack_power = attack
        self.defense_power = defense
        Hero.total_heroes += 1

    # Method untuk menampilkan nama hero
    def identify(self):
        print(f"Hero name: {self.name}")
    
    # Method untuk menambah poin attack
    def increase_attack(self, amount):
        self.attack_power += amount
        print(f"{self.name}'s attack increased by {amount}. New attack: {self.attack_power}")
    
    # Method untuk mengurangi poin defense
    def decrease_defense(self, amount):
        self.defense_power -= amount
        if self.defense_power < 0:
            self.defense_power = 0
        print(f"{self.name}'s defense decreased by {amount}. New defense: {self.defense_power}")
    
    # Method untuk menampilkan sisa health hero
    def get_health(self):
        print(f"{self.name}'s remaining health: {self.health}")
    
    # Method untuk menyerang hero lain
    def attack_enemy(self, enemy_hero):
        print(f"{self.name} attacks {enemy_hero.name}!")
        damage = self.attack_power - enemy_hero.defense_power
        if damage > 0:
            enemy_hero.health -= damage
            print(f"{enemy_hero.name} takes {damage} damage! Remaining health: {enemy_hero.health}")
        else:
            print(f"{enemy_hero.name} blocks the attack!")
    
    # Class method untuk menampilkan jumlah hero yang sudah dibuat
    @classmethod
    def get_total_heroes(cls):
        print(f"Total heroes created: {cls.total_heroes}")

# Membuat objek hero
hero1 = Hero("Warrior", 100, 20, 10)
hero2 = Hero("Mage", 80, 25, 5)

# Menjalankan semua method
hero1.identify()
hero2.identify()

hero1.increase_attack(5)
hero2.decrease_defense(2)

hero1.get_health()
hero2.get_health()

hero1.attack_enemy(hero2)
hero2.attack_enemy(hero1)

# Menampilkan total hero yang sudah dibuat
Hero.get_total_heroes()
