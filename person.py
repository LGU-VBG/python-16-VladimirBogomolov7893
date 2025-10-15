class Person:
    def __init__(self,name,surname):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self,new):
        self._name = new
    
    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self,new):
        self._surname = new

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"
    
    @fullname.setter
    def fullname(self,v):
        name_split = v.split()
        self._name = name_split[0]
        self._surname = name_split[1]    

person = Person('Mike', 'Pondsmith')
person.fullname = 'Troy Baker'
print(person.name)
print(person.surname)

