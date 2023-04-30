from models.System import System
from models.User import Customer
from models.CodeDiscount import *
from models.Category import *
from models.Product import *
from models.Cart import *

system = System()

for i in range(10):
    email = f"email{i+1}@email.com"
    firstname = f"firtname{i+1}"
    lastname = f"lastname{i+1}"
    password = f"password{i+1}"
    system.create_customer(email, password, firstname, lastname)
# mockup for create order
# p1 = Keyboard(
#     "KB001",
#     "Corsair K70 RGB MK.2",
#     159.99,
#     "Mechanical Gaming Keyboard",
#     "https://example.com/keyboard.jpg",
#     10,
#     "MK.2",
#     "Mechanical",
#     "Cherry MX Speed",
#     "Black",
# )
# p2 = Keyboard(
#     "kb002",
#     "Wireless Office Keyboard",
#     49.99,
#     "A wireless keyboard with a slim design and quiet keys, suitable for office use.",
#     "https://example.com/images/wireless-office-kb.jpg",
#     25,
#     "V1",
#     "Membrane",
#     "N/A",
#     "White",
# )
# p3 = Keyboard(
#     "kb003",
#     "Backlit Mechanical Keyboard",
#     89.99,
#     "A wireless keyboard with a slim design and quiet keys, suitable for office use.A backlit mechanical keyboard with customizable lighting effects and hot-swappable switches.",
#     "https://example.com/images/backlit-mechanical-kb.jpg",
#     5,
#     "V3",
#     "Mechanical",
#     "Gateron Brown",
#     "Silver",
# )
# p4 = Keyboard(
#     "kb004",
#     "Wireless Mechanical Keyboard",
#     99.99,
#     "A wireless mechanical keyboard with a tenkeyless layout and RGB lighting.",
#     "https://example.com/images/wireless-mechanical-kb.jpg",
#     15,
#     "V2",
#     "Mechanical",
#     "Kailh Box White",
#     "Black",
# )
# p5 = Keyboard(
#     "kb005",
#     "RGB Gaming Keyboard",
#     69.99,
#     "An RGB gaming keyboard with a compact layout and detachable USB cable.",
#     "https://example.com/images/rgb-gaming-kb.jpg",
#     20,
#     "V1",
#     "Mechanical",
#     "Outemu Blue",
#     "White",
# )
# keyboard_cate = Category(name="keybaord", products=[p1, p2, p3, p4, p5])
# system.add_category(keyboard_cate)

# # add code discount
# code = CodeDiscount(code="9arm", discount=0.8, expire_date="yy-mm-dd")
# system.add_code_discount(code)

# for i in range(5):
#     name = f"cateTest{i+1}"
#     product = [f"PP{i+1}", f"PP{i+2}", f"PP{i+3}", f"PP{i+4}"]
#     system.add_category(Category(name=name, products=product))

#     system.add_category(
#         Category(
#             name=name,
#             products=[
#                 Keyboard(
#                     f"001",
#                     "K2 SSR",
#                     3200,
#                     "A mechanical keyboard with RGB backlight",
#                     "sefaf.png",
#                     "23-03-2023",
#                     "v4",
#                     "wireless",
#                     "blue switches",
#                     "backlight",
#                 ),
#                 Keyboard(
#                     f"002",
#                     "K2 SSR",
#                     3200,
#                     "A mechanical keyboard with RGB backlight",
#                     "sefaf.png",
#                     "23-03-2023",
#                     "v4",
#                     "wireless",
#                     "blue switches",
#                     "pinklight",
#                 ),
#                 Keyboard(
#                     f"003",
#                     "K2 SSR",
#                     3200,
#                     "A mechanical keyboard with RGB backlight",
#                     "sefaf.png",
#                     "23-03-2023",
#                     "v5",
#                     "wireless",
#                     "red switches",
#                     "bluelight",
#                 ),
#                 Keyboard(
#                     f"004",
#                     "K3 SSR",
#                     3200,
#                     "A mechanical keyboard with RGB backlight",
#                     "sefaf.png",
#                     "23-03-2023",
#                     "v2",
#                     "wireless",
#                     "red switches",
#                     "redlight",
#                 ),
#             ],
#         )
#     )


# # A dictionary to store the discount codes and their discount amount and expiration date
# DISCOUNT_CODES = [
#     CodeDiscount(code="CODE1", expire_date=date(2022, 1, 1), discount=0.1),
#     CodeDiscount(code="CODE2", expire_date=date(2023, 6, 30), discount=0.2),
#     CodeDiscount(code="CODE3", expire_date=date(2024, 2, 2), discount=0.3),
#     CodeDiscount(code="CODE3", expire_date=date(2025, 12, 31), discount=0.4),
# ]

# for i in range(len(DISCOUNT_CODES)):
#     system.add_code_discount(DISCOUNT_CODES[i])
