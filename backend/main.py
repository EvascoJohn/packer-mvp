from fastapi import FastAPI
from dataclasses import dataclass
from database import session
from fastapi.encoders import jsonable_encoder


import model_data
import models
from database import engine


models.Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message":"hello, world"}


@app.get("/bags")
async def get_bags():
    result = jsonable_encoder(session.query(models.Bag).all())
    if result:
        return result


@app.get("/items")
async def get_items():
    pass
    

@app.get("/bag/{bag_id}")
async def get_bag(bag_id):
    result = jsonable_encoder(session.query(models.Bag).get(bag_id))
    if result:
        return result


@app.post("/create_bag/")
async def get_bag(bag_data: model_data.Bag):
    try:
        new_data = models.Bag(name=bag_data.name)
        session.add(new_data)
        session.commit()
        return {"status": "success", "message": "successfully created a bag."}
    except Exception as e:
        return {"status": "fail", "message": "failed to create a bag."}