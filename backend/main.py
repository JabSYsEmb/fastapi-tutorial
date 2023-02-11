"""Module providing REST API as backend"""
import json

from enum import Enum
from pathlib import Path

# from fastapi.responses import HTMLResponse
# from fastapi.responses import PlainTextResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
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

# predefined paths using Enum
class ModelName(str, Enum):
  ALEXNET = "alexnet"
  RESNET = "resnet"
  LENET = "lenet"

@app.get("/api/v1/models/{model_name}")
async def model_root(model_name: ModelName) :
  if model_name is ModelName.alexnet:
    return {
        "model_name": model_name, 
        "message": "has 20k parameters to be tuned"
    }
  if model_name.value == ModelName.resnet.value:
    return {
        "model_name": model_name,
        "message": "has 22k parameters to be tuned"
    }
  return {
      "model_name": model_name,
      "message" : "has 2k parameters to be tuned"
  }

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]

@app.get("/api/v1/db/")
async def db_root(start: int = 0, length: int = 10):
  return fake_items_db[ start: start+length ]

@app.get("/api/v1/files/{path_to_json_file:path}")
async def path_root(path_to_json_file: str):
  content_path = Path.cwd().resolve().joinpath(path_to_json_file)
  return {
      "file": path_to_json_file,
      "content" : json.loads(content_path.read_text(encoding="utf-8"))
  }
