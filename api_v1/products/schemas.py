from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):
    name: str | None
    description: str | None
    price: int | None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
