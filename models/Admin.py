from dataclasses import dataclass,field
from User import User


@dataclass
class Admin(User):
        phone : str = field(default="10",metadata={"max_length":10})
