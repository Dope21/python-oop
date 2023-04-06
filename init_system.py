from models.System import System
from models.User import Customer
from models.Category import *
######## HEAD
from models.Cart import Cart

=======
from models.Product import *
######## 49addc50e050ffc847d6bf70f344e3d06d071c47
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
<<<<<<< HEAD
      product=[f"PP{i+1}",f"PP{i+2}",f"PP{i+3}",f"PP{i+4}"]
      system.add_category(Category(name=name,products=product))


  ############# Ten



=======
      
      system.add_category(Category(name=name,
      products=[Keyboard(f"001","K2 SSR",3200,"A mechanical keyboard with RGB backlight","sefaf.png","23-03-2023","v4","wireless","blue switches","backlight"),
      Keyboard(f"002","K2 SSR",3200,"A mechanical keyboard with RGB backlight","sefaf.png","23-03-2023","v4","wireless","blue switches","pinklight"),
      Keyboard(f"003","K2 SSR",3200,"A mechanical keyboard with RGB backlight","sefaf.png","23-03-2023","v5","wireless","red switches","bluelight"),
      Keyboard(f"004","K3 SSR",3200,"A mechanical keyboard with RGB backlight","sefaf.png","23-03-2023","v2","wireless","red switches","redlight")]))
######## 49addc50e050ffc847d6bf70f344e3d06d071c47
      
  
  
