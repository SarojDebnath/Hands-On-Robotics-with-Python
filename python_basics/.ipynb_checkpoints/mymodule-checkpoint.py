def add(a,b):
    return a+b

class xy:
    def __init__(self,name,country):
        self.name=name
        self.c=country
    def func(self,dest):
        return f'Hi, I am {self.name} from {self.c} and my destination is {dest}'