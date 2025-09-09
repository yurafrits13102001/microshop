"""
Create
Read
Update
Delete
"""

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.products.schemas import ProductCreate
from core.models import Product


async def get_products(session: AsyncSession) -> list[Product]:  # get all products
    query = select(Product).order_by(Product.id)
    result: Result = await session.execute(query)
    products = result.scalars().all()
    return list(products)


async def get_product(
    session: AsyncSession, product_id: int
) -> Product | None:  # get one product
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product
