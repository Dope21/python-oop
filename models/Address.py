from dataclasses import dataclass


@dataclass
class SetAddress:
    pass

@dataclass
class Address:
    firstname : str
    lastname : str
    address : str
    phone : str
    zip_code : str
    set:SetAddress

