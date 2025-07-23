from typing import Optional
from pydantic import BaseModel

class ItemBody(BaseModel):
    item_id: Optional[int]
    item_name: str
    item_price: float
    item_description: Optional[str]
    