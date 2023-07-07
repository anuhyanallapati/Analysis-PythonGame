from colorama import Back, Fore

class Building:
    def __init__(self, health, x, y, symbol):
        self.health = health
        self.x = x
        self.y = y
        self.dead = 0
        self.max_health = health
        self.symbol = symbol

    def change_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead = 1
            print(
                Back.GREEN
                + "\033[%s;%sH" % (self.y, self.x)
                + " "
            )
        elif self.health <= self.max_health / 2 and self.health > self.max_health / 5:
            print(
                Back.RED
                + Fore.YELLOW
                + "\033[%s;%sH" % (self.y, self.x)
                + self.symbol
            )
        elif self.health <= self.max_health / 5:
            print(
                Back.BLUE
                + Fore.YELLOW
                + "\033[%s;%sH" % (self.y, self.x)
                + self.symbol
            )


class hut(Building):
    symbol = "H"

    def __init__(self, x, y, health):
        super().__init__(health, x, y, self.symbol)


class canon(Building):
    symbol = "C"

    def __init__(self, damage, x, y, health):
        super().__init__(health, x, y, self.symbol)
        self.damage = damage

    def damage_health(self, obj):
        obj.change_health(self.damage)


class Townhall(Building):
    symbol = "HH"

    def __init__(self, x, y, health):
        super().__init__(health, x, y, self.symbol)