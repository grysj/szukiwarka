from fastapi import FastAPI
from eng_help.engine_init import Engine
import json
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*"
]

app = FastAPI()
se = Engine()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           
    allow_credentials=True,
    allow_methods=["*"],             
    allow_headers=["*"],              
)
@app.get("/")
def read_root():
    print("Engine initialised")


@app.get("/search")
def read_item(query: str, eng: int, k: int):
    result = json.loads(se.search(query, eng, k))
    return result
