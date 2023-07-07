class Huts:
    def __init__(self,x,y,health,life):
        self.x=x
        self.y=y
        self.health=health
        self.life=life
    
    def update_health(self,damage):
        self.health=self.health-damage
        if(self.health<=0):
            self.life=False    