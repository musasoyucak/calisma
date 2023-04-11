class Human:
    
    name="Musa"
    def talk(self,message):
        print(f"{self.name}:{message}")
    def walk(self):
       print(f"{self.name} yürüyor")
    def __init__(self,name):
        self.name=name
        
    def talk(self,sentence):
        print(f"{self,name}{sentence}")
        name="Ali"
        print(f"{self.name}{sentence}")
        self.walk()

human1=Human("zeynep")
human1.name="ayse"
human1.talk("hi")
human1.walk()
print(human1)
