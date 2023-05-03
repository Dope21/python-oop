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

customer = system.get_customer_by_email("email1@email.com")

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

keycap.create_product(
    kind="keycap",
    name="Cherry MX Keycap Set",
    price=29.99,
    description="A set of Cherry MX keycaps with a variety of colors and styles to choose from.",
    image="https://example.com/images/cherry-mx-keycap-set.jpg",
    qty=10,
    version="V2",
    color="Multi",
)

keycap.create_product(
    kind="keycap",
    name="PBT Dye-Sublimated Keycap Set",
    price=49.99,
    description="A set of PBT keycaps with dye-sublimated legends for long-lasting and durable legends.",
    image="https://example.com/images/pbt-dye-sublimated-keycap-set.jpg",
    qty=15,
    version="V1",
    color="Black and White",
)

keycap.create_product(
    kind="keycap",
    name="SA Keycap Set",
    price=69.99,
    description="A set of sculpted SA profile keycaps with a vintage look and feel.",
    image="https://example.com/images/sa-keycap-set.jpg",
    qty=8,
    version="V3",
    color="Beige",
)

keycap.create_product(
    kind="keycap",
    name="Backlit Keycap Set",
    price=39.99,
    description="A set of keycaps with translucent legends and a variety of color options for customizable lighting effects.",
    image="https://example.com/images/backlit-keycap-set.jpg",
    qty=12,
    version="V2",
    color="Multi",
)

keycap.create_product(
    kind="keycap",
    name="Customized Artisan Keycap",
    price=99.99,
    description="A one-of-a-kind artisan keycap with a unique design and hand-crafted by an artisan maker.",
    image="https://example.com/images/customized-artisan-keycap.jpg",
    qty=1,
    version="V1",
    color="Purple",
)

# A dictionary to store the discount codes and their discount amount and expiration date
DISCOUNT_CODES = [
    CodeDiscount(code="CODE1", expire_date=date(2025, 1, 1), discount=0.9),
    CodeDiscount(code="CODE2", expire_date=date(2025, 6, 30), discount=0.8),
    CodeDiscount(code="CODE3", expire_date=date(2020, 2, 2), discount=0.7),
    CodeDiscount(code="CODE3", expire_date=date(2021, 12, 31), discount=0.6),
]

for i in range(len(DISCOUNT_CODES)):
    system.add_code_discount(DISCOUNT_CODES[i])
