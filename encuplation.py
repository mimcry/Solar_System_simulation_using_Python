class practice:
    def __init__(self,name,age) :
     self.name=name
     self.age=age
    def run(self):
      print('run')
    def spoke(self):
     print (f"hello my name is {self.name} and i am {self.age} years old")
    




player =practice("Salon gautam",20)     
print(player.spoke())
print((1,2,3,1).count(0))