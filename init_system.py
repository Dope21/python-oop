from models.System import System
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

# product mockup
keyboard = system.create_category("keyboard")
keycap = system.create_category("keycap")
switch = system.create_category("switch")
mouse = system.create_category("mouse")

keyboard.create_product(
    kind="keyboard",
    name="Corsair K70 RGB MK.2",
    price=159.99,
    description="Mechanical Gaming Keyboard",
    image="https://example.com/keyboard.jpg",
    qty=10,
    version="MK.2",
    type="Mechanical",
    switches="Cherry MX Speed",
    color="Black",
)
keyboard.create_product(
    kind="keyboard",
    name="Wireless Office Keyboard",
    price=49.99,
    description="A wireless keyboard with a slim design and quiet keys, suitable for office use.",
    image="https://example.com/images/wireless-office-kb.jpg",
    qty=25,
    version="V1",
    type="Membrane",
    switches="N/A",
    color="White",
)
keyboard.create_product(
    kind="keyboard",
    name="Backlit Mechanical Keyboard",
    price=89.99,
    description="A wireless keyboard with a slim design and quiet keys, suitable for office use.A backlit mechanical keyboard with customizable lighting effects and hot-swappable switches.",
    image="https://example.com/images/backlit-mechanical-kb.jpg",
    qty=5,
    version="V3",
    type="Mechanical",
    switches="Gateron Brown",
    color="Silver",
)
keyboard.create_product(
    kind="keyboard",
    name="Wireless Mechanical Keyboard",
    price=99.99,
    description="A wireless mechanical keyboard with a tenkeyless layout and RGB lighting.",
    image="https://example.com/images/wireless-mechanical-kb.jpg",
    qty=15,
    version="V2",
    type="Mechanical",
    switches="Kailh Box White",
    color="Black",
)
keyboard.create_product(
    kind="keyboard",
    name="RGB Gaming Keyboard",
    price=69.99,
    description="An RGB gaming keyboard with a compact layout and detachable USB cable.",
    image="https://example.com/images/rgb-gaming-kb.jpg",
    qty=20,
    version="V1",
    type="Mechanical",
    switches="Outemu Blue",
    color="White",
)
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
