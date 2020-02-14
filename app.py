from fastapi import FastAPI
import  uvicorn
import os
from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine)
from databases import Database


#Init App
app =FastAPI(debug = True)
basedir = os.path.abspath(os.path.dirname(__file__))

# Init Database
metadata = MetaData()

notes = Table(
    "Product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Integer),
    Column("price",Integer),
    Column("qty", Integer),
)

url = 'sqlite:///' + os.path.join(basedir, 'fastapi.sqlite')
DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'fastapi.sqlite')
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
metadata.drop_all(engine)


# route
@app.get("/api/v2/hello")
def get_hello():
    return {"hello": "world"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/product/{id}")
def get_item(id: int):
    return {"item_id": id}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port = '8080')
    #database.drop_all()
    database.create_all()
    database.session.commit()