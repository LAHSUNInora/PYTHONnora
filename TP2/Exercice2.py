class Chien:
  def __init__(self,nom,age,race):
    self.nom=nom
    self.age=age
    self.race=race
  def aboyer(self):
    print("woof!!")
Chien1 = Chien("koki",14,"cccc")
Chien1.aboyer()