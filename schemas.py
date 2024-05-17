from pydantic import BaseModel
from enum import Enum

class Brand(str, Enum):
    NITRO = 'Nitro'
    SALOMAN = 'Saloman'
    BURTON = 'Burton'

class Snowboard(BaseModel):
    id: int
    length: int
    color: str
    has_bindings: bool
    brand: Brand
    
    
        

    
    
