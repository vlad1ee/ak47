class Soldier:
    def __init__(self,name):
        self.name = name

class Guns:
    def __init__(self, gun):
        self.gun = gun

class Act_of_shooting(Soldier, Guns):
    def __init__(self, name, gun):
        self.gun = gun
        self.bullets = 30
        super().__init__(name)

    def fire(self):
        print('tigi-tigitishh')
        self.bullets -=1
        if self.bullets == 0:
            self.reload()
    
    def reload(self):
        self.bullets = 30


a = Act_of_shooting('Ryan', 'ak-47')
a.fire()
a.fire()
a.fire()
a.reload()
print(a.bullets)