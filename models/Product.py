from dataclasses import dataclass

@dataclass
class Product:
  id : str
  name : str
  price : float
  description : str
  image : str
  qty: int

class Keyboard(Product):
  version : str
  type : str
  switches : str
  color : str
 
class Keycap(Product):
  version : str
  color : str

class Mouse(Product):
  connection : str
  color : str
 
class Switch(Product):
  option : str
  quantity_set : int



  