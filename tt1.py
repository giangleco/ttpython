#-Để định nghĩa một lớp trừu tượng trong Python, minh cần kế thừa từ lop ABC (Abstract Base Class) và 
# sử dụng decorator @abstractmethod để đánh dấu các phương thức trừu tượng.
from abc import ABC,abstractmethod
class Product():
    def __init__(self,id,name,price,total):
        self.id=id
        self.name=name
        self.price=price
        self.total=total
class Mobile(Product):
    def __init__(self, id, name, price, total,battery,memory):
        super().__init__(id, name, price, total)
        self.battery=battery
        self.memory=memory
class MobileManager(ABC):
    @abstractmethod
    def add_mobile(self,mobile):
        pass
class MobileManagerlmpl(MobileManager):
    def __init__(self):
        self.list_append=[]
    def add_mobile(self, mobile):
        self.list_append.append(mobile)
    def print_mobile(self):
       for mobile in self.list_append:
           print(mobile.id,mobile.name,mobile.price,mobile.total,mobile.battery,mobile.memory)
mobile1=Mobile(2023,"ip11",100,10,1000,1)
mobile2=Mobile(2024,"ip12",200,20,2000,2)
manager=MobileManagerlmpl()
manager.add_mobile(mobile1)
manager.add_mobile(mobile2)
manager.print_mobile()



