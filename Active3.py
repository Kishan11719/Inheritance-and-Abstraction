from abc import ABC, abstractmethod
# create a base class 
class Animal(ABC):

     # abstract method
         # should be implemented by all sub-classes
         def move(self):
                 pass
         
# sub classes
class Human(Animal):

         def move(self):
                 print("I can crawl")

class snake(Animal) 

       def move(self):
               print("I can bark")

class Lion(Animal):

          def move(self):
                  print("I can roar")               