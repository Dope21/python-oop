from models.System import System
from models.User import Customer
from models.Category import Category
from models.Product import Keyboard
from models.CodeDiscount import CodeDiscount

system = System()

for i in range(10):
  email = f"email{i+1}@email.com"
  firstname = f"firtname{i+1}"
  lastname = f"lastname{i+1}"
  password = f"passowrd{i+1}"
  system.add_customer(
    Customer(email=email,firstname=firstname,lastname=lastname,password=password)
  )

# mockup for create order
p1 = Keyboard("KB001","Corsair K70 RGB MK.2",159.99,"Mechanical Gaming Keyboard","https://example.com/keyboard.jpg",10,"MK.2","Mechanical","Cherry MX Speed","Black")
p2 = Keyboard("kb002","Wireless Office Keyboard",49.99,"A wireless keyboard with a slim design and quiet keys, suitable for office use.","https://example.com/images/wireless-office-kb.jpg",25,"V1","Membrane","N/A","White")
p3 = Keyboard("kb003","Backlit Mechanical Keyboard",89.99,"A wireless keyboard with a slim design and quiet keys, suitable for office use.A backlit mechanical keyboard with customizable lighting effects and hot-swappable switches.","https://example.com/images/backlit-mechanical-kb.jpg",5,"V3","Mechanical","Gateron Brown","Silver")
p4 = Keyboard("kb004","Wireless Mechanical Keyboard",99.99,"A wireless mechanical keyboard with a tenkeyless layout and RGB lighting.","https://example.com/images/wireless-mechanical-kb.jpg",15,"V2","Mechanical","Kailh Box White","Black")
p5 = Keyboard("kb005","RGB Gaming Keyboard",69.99,"An RGB gaming keyboard with a compact layout and detachable USB cable.","https://example.com/images/rgb-gaming-kb.jpg",20,"V1","Mechanical","Outemu Blue","White")
keyboard_cate = Category(name="keybaord", products=[p1,p2,p3,p4,p5])
system.add_category(keyboard_cate)

customer = system.get_customer_by_email("email1@email.com")
customer.add_cart_item(p1, 2)
customer.add_cart_item(p2, 1)

# add code discount
code = CodeDiscount(code="9arm",discount=0.8,expire_date="yy-mm-dd")
system.add_code_discount(code)