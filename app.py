from fastapi import FastAPI
import  uvicorn
import os
from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine)
from sqlalchemy import types
from databases import Database
from pydantic import BaseModel, Field

#Init App
app =FastAPI(debug = True)
basedir = os.path.abspath(os.path.dirname(__file__))

# Init Database
metadata = MetaData()

class ProductSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: int
    qty: int

product = Table(
    "product",
    metadata,
    Column("id", types.Integer, primary_key=True),
    Column("name", types.Integer),
    Column("price",types.Integer),
    Column("qty", types.Float)
)

url = 'sqlite:///' + os.path.join(basedir, 'fastapi.sqlite')
DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'fastapi.sqlite')
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
#metadata.drop_all(engine)


@app.get("/product/{id}")
async def get_product(id: int):
    query = product.select().where(id == product.c.id)
    return await database.fetch_one(query=query)

@app.get("/product")
async def get_all():
    query = product.select()
    return await database.fetch_all(query=query)

@app.post("/product/{id}")
async def post_product(item: ProductSchema):
    query = product.insert().values(name = item.name, price = item.price, qty = item.qty)
    return await database.execute(query)

@app.put("/product/{id}")
async def update_product (id: int, item: ProductSchema):
    query = (
        product
        .update()
        .where(id == product.c.id)
        .values(price=item.price, name=item.name, qty=item.qty)

    )
    return await database.execute(query=query)

@app.delete("/product/{id}")
async def delete_product(id: int ):
    query = (product.delete().where(id == product.c.id))
    return await database.execute(query)

if __name__ == '__main__':
    #product.create(engine)
    #database.create_all()
    uvicorn.run(app, host='0.0.0.0', debug=True)

    #database.drop_all()

    database.session.commit()