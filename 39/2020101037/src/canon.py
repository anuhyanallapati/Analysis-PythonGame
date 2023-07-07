class Canon:

    def __init__(self, damage, x, y, health, life):
        self.damage = damage
        self.x = x
        self.y = y
        self.health = health
        self.life = life
        print(life)

    def update_health(self, damage):
        self.health = self.health-damage
        if (self.health <= 0):
            self.life = False
