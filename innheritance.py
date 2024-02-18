class User():
    def Sign_in(Self):
        print("logged in")
class Wizward(User):
    def __init__(self,name,qualification):
       self.name=name
       self.qualification=qualification
    def attack (self):
        print(f"hello my name is {self.name} and i have pass {self.qualification}")


class Aundrya(User):
   def __init__(self,name,age):
       self.name=name
       self.age=age
   def attack (self):
        print(f"hello my name is {self.name} and i am {self.age} years old.")
player=Wizward("salon gautam", "slc")

print(player.attack())
