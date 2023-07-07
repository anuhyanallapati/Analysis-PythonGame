class Barbarian:
    def __init__(self,damage,x,y,health,life,spawn,target):
        self.damage=damage
        self.x=x
        self.y=y
        self.health=health
        self.life=life
        self.spawn=spawn
        self.target=target
    
    def update_health(self,damage):
        self.health=self.health-damage
        if(self.health<=0):
            self.life=False    
            