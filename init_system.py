from models.System import System
from models.User import Customer
from models.Category import *
system = System()

for i in range(10):
  email = f"email{i+1}@email.com"
  firstname = f"firtname{i+1}"
  lastname = f"lastname{i+1}"
  password = f"passowrd{i+1}"
  system.add_customer(
    Customer(email=email,firstname=firstname,lastname=lastname,password=password)
  )
  
  ############# Game
for i in range(5):
      name = f"cateTest{i+1}"
      product=[f"PP{i+1}",f"PP{i+2}",f"PP{i+3}",f"PP{i+4}"]
      system.add_category(Category(name=name,products=product))
      
  
  