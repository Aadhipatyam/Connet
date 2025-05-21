## Pydantic Schemas

from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    sku: str
    price: float
    description: Optional[str] = None
    image_url: Optional[str] = None
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    category: CategoryOut

    class Config:
        orm_mode = True
