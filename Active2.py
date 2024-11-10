class Person( object ):

               # __init__is known as the constructro
               def __init__(self, name, idnumber):
                            self.name = name
                            self.idnumber = idnumber
               def display(self):
                            print(self.name)
                            print(self.idnumber)

# child class
class Employee( Person ):
                def __init__(self, name, idnumber, salary, post):
                                self.salary = salary
                                self.post = post

                                # invoking the __init__of the
                                
                                Person.__init__(self, name, idnumber)

# creation of on an object variable or an instance
a = Employee('Penduin', 20210401, 15000, "Intern")

# calling a function of the class Person using its intance
a.display()