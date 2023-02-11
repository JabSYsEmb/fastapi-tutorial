"""Module providing REST API as backend"""
import json

from enum import Enum
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

origins = [
  "http://localhost:3000",
]

app = FastAPI()

# CORS enabled for some URL
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

class Item(BaseModel):
  item_id: int
  item_name: str
  description: str or None = None
  price: float
  tax: float or None = None

class MLModel(BaseModel):
  model_name: str
  message: str or None = None
  def model_name_swapcase(self):
    self.model_name = self.model_name.swapcase()

# predefined paths using Enum
class ModelName(str, Enum):
  ALEXNET = "alexnet"
  RESNET = "resnet"
  LENET = "lenet"

fake_items_db = [
    {"item_id": 1, "item_name": "Banana", "price": 14.3},
    {"item_id": 2, "item_name": "Apple", "price": 18.3},
    {"item_id": 3, "item_name": "Orange", "price": 11.3},
]

# /api/v1/items
@app.get("/api/v1/items/")
async def get_first_nth_items(start: int = 0, length: int = 10):
  return fake_items_db[ start: start+length ]

@app.post("/api/v1/items/")
async def post_new_item(new_item: Item):
  item = new_item.dict()
  if new_item.tax:
      total_cost = new_item.tax + new_item.price
      item.update({"total_price" : total_cost})
  return item

@app.get("/api/v1/items/{item_id}")
async def get_item_by_id(item_id: int):
  return fake_items_db[item_id]

@app.put("/api/v1/items/{item_id}")
async def get_item_by_id(item_id: int, new_item: Item):
    return  {"item_id" : item_id, **new_item.dict()}

# api/v1/models

@app.get("/api/v1/models/{model_name}")
async def get_model_by_name(model_name: ModelName) :
  if model_name is ModelName.ALEXNET:
    return {
      "model_name": model_name,
      "message": "has 20k parameters to be tuned"
    }
  if model_name.value == ModelName.RESNET.value:
    return {
      "model_name": model_name,
      "message": "has 22k parameters to be tuned"
    }
  return {
    "model_name": model_name,
    "message" : "has 2k parameters to be tuned"
  }

@app.post("/api/v1/models")
async def post_new_model(model: MLModel):
  model.model_name_swapcase()
  return model

# api/v1/files/path.json
@app.get("/api/v1/files/{path_to_json_file:path}")
async def get_json_file_by_path(path_to_json_file: str):
  content_path = Path.cwd().resolve().joinpath(path_to_json_file)
  return {
    "file": path_to_json_file,
    "content" : json.loads(content_path.read_text(encoding="utf-8"))
  }
