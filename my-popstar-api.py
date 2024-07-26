import fastapi;
from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

# Path Parameters vs Query Param
popStars = {
    1: {
        "name": "Charli XCX",
        "age": 23,
        "recentAlbum": "brat"
    },
    2: {
        "name": "Ariana",      
        "age": 23,
        "recentAlbum": "brat"},
}

class PopStar(BaseModel):
     name: str
     age: int
     recentAlbum: str

class updatePopStar(BaseModel):
     name: Optional[str] = None
     age: Optional[int] = None
     recentAlbum: Optional[str] = None

@app.get("/get-pop-star/{pop_star_id}")
def get_pop_star(pop_star_id: int = Path(..., description="id of pop star you want to view", gt=0)):
       if pop_star_id not in popStars:
          return{"error": "pop Star does not exists"}
       return popStars[pop_star_id]

@app.get("/get-pop-star-by-name/{pop_star_id}")
def get_pop_star( *, pop_star_id: int, name: Optional[str] = None, test: int):
    for pop_star_id in popStars:
         if popStars[pop_star_id]["name"] == name:
            return popStars[pop_star_id]
    return {"data": "Not Found Please Don't Get Sad"}

@app.post("/create-pop-star/{pop_star_id}")
def create_pop_star(pop_star_id: int, newPopStar: PopStar):
     if pop_star_id in popStars:
        return {"error": "pop Star exists"}
     
     popStars[pop_star_id] = newPopStar
     return  popStars[pop_star_id]

@app.put("/update-pop-star/{pop_star_id}")
def update_pop_star(pop_star_id: int,  popStar: updatePopStar):
     if pop_star_id not in popStars:
          return{"error": "pop Star does not exists"}
     
     if popStar.name is not None:
        popStars[pop_star_id]["name"] = popStar.name

     if popStar.age is not None:
        popStars[pop_star_id]["age"] = popStar.age

     if popStar.recentAlbum is not None:
        popStars[pop_star_id]["recentAlbum"] = popStar.recentAlbum

     return  popStars[pop_star_id]

@app.delete("/delete-pop-star/{pop_star_id}")
def delete_pop_star(pop_star_id: int):
     if pop_star_id not in popStars:
          return{"error": "pop Star does not exists"}

     del popStars[pop_star_id]

     return {"error": "pop Star has been un alived"}
