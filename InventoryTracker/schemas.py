from pydantic import BaseModel


# Base schema shared by all product models
class ProductBase(BaseModel):
    name: str
    quantity: int


# Schema for creating a new product
class ProductCreate(ProductBase):
    pass


# Schema for sending product data back to client
class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True