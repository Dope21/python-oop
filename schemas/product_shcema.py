from pydantic import BaseModel

class  Categoryname(BaseModel):
    catename : str

class Productid(BaseModel):
    pid : str
    
class Proid(BaseModel):
    catename:str
    id:str
    
class Proname(BaseModel):
    catename:str
    name:str

class Probyname(BaseModel):
    name: str

    

    