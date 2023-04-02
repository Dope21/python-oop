from dataclasses import dataclass

@dataclass
class Product:
  id : str
  name : str
  price : float
  description : str
  image : str
  qty: int


#############################################################   Keyboard inherite form product #########################################################
@dataclass
class Keyboard(Product):

  version : str
  type : str
  switches : str
  color : str
  
 

############################################################# Mouse ###########################################################
@dataclass
class Mouse(Product):
  connection : str
  color : str


 

########################################################### Switch ########################################
@dataclass
class Switch(Product):
  option : str
  quantity_set : int

  ############### id
  @property
  def id(self) -> str:
    return self.id
  
  @id.setter
  def id(self,id:str):
    self.id

  ################# name
  @property
  def name(self) -> str:
    return self.name
  
  @name.setter
  def name(self,name:str):
    self.name

  ################# price
  @property
  def price(self) -> float:
    return self.price
  
  @price.setter
  def price(self,price:float):
    self.price

  ######################### description
  @property
  def description(self) -> str:
    return self.description
  
  @description.setter
  def description(self,description:str):
    self.description
  ############################## image
  @property
  def image(self) -> str:
    return self.image
  
  @image.setter
  def image(self,image:str):
    self.image

  ###################### qty
  @property
  def qty(self) -> str:
    return self.qty
  
  @qty.setter
  def qty(self,qty:str):
    self.qty

  ###################### connection
  @property
  def option(self) -> str:
    return self.option
  
  @option.setter
  def option(self,option:str):
    self.option
    
  ############################ color
  @property
  def quantity_set(self) -> str:
    return self.quantity_set
  
  @quantity_set.setter
  def quantity_set(self,quantity_set:str):
    self.quantity_set



  