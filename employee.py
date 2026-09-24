
class Employee:
    def __init__(self,name,salary,id):
        self.name = name   # public variable
        self._salary = salary    # protected  variable
        self.__id = id      
         # private variable
    def show_salary(self):
        return self._salary
    def show_id(self):
        return self.__id
# manager--------------------------

class Manager(Employee):              
    def __init__(self,name,salary,id):
       super().__init__(name,salary,id)
       
    def calculate_bonus(self):
        return self._salary+(self._salary*10/100)
    def show_info(self):
        return f" Name : {self.name} and id : {self.show_id()}"
    def __generate_report(self):
         return f" manager : {self.name} id : {self.show_id()} salary : {self._salary} with bonus {self.calculate_bonus()} "
    def show_report(self):
       return self.__generate_report()
# developer--------------------

class Developer(Employee):           # inhertance
    def __init__(self,name,salary,id):
       super().__init__(name,salary,id)
       
    def calculate_bonus(self):         # overriding
        return self._salary+(self._salary*10/100)
    def show_info(self):
        return f" Name : {self.name} and id : {self.show_id()}"
    def __generate_report(self):
         return f" Developer : {self.name}  id : {self.show_id()} salary : {self._salary} with bonus {self.calculate_bonus()} "
    def show_report(self):
       return  self.__generate_report()
class Designer(Employee):          # inheritance
    def __init__(self,name,salary,id):
       super().__init__(name,salary,id)
       
    def calculate_bonus(self):     # overriding
        return self._salary+(self._salary*10/100)
    def show_info(self):
        return f" Name : {self.name} and id : {self.show_id()}"
    def __generate_report(self):
         return f" Designer: {self.name} of id : {self.show_id()} salary : {self._salary} with bonus {self.calculate_bonus()} "
    def show_report(self):
        return self.__generate_report()
# m = Manager("ali",10000,1)
# print(m.show_id())
# print(m.show_salary())
# print(m.show_report())
# d = Developer("ahmad",20000,2)
# print(d.show_id())
# print(d.show_salary())
# print(d.show_report())
# b = Designer("amjad",30000,3)
# print(b.show_id())
# print(b.show_salary())
# print(b.show_report())
empl = [Manager("ali",10000,"123"),Developer("ahmad",20000,"456"),Designer("amjad",30000,"789")] # ploymorphism 
for i in empl:
    print(i.show_info())
    print(i.calculate_bonus())
    print(i.show_report())






   

    

