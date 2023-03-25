from dataclasses import dataclass
from User import User
@dataclass
class Admin(User):
        phone : int