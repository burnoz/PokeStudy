class Pokemon:
    def __init__(self, name, hp, is_fainted, sprite, fainted_sprite, x, y):
        self.name = name
        self.hp = hp
        self.is_fainted = is_fainted
        self.sprite = sprite
        self.fainted_sprite = fainted_sprite
        self.x = x
        self.y = y

    def lose_health(self):
        self.hp -= 1
        if self.hp <= 0:
            self.hp = 0
            self.is_fainted = True
            print(f"{self.name} has fainted!")
            self.sprite = self.fainted_sprite
        else:
            print(f"{self.name} has {self.hp} health remaining.")
