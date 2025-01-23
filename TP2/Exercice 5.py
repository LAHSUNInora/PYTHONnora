class Animal():
    def faire_du_bruit(self):
        pass
class Chien(Animal):
    def faire_du_bruit(self):
        print("woof")
class Chat(Animal):
    def faire_du_bruit(self):
        print("miou")

Chien1 = Chien()
Chat1 = Chat()

Chat1.faire_du_bruit()
Chien1.faire_du_bruit()



