# uvicorn backend.api:app --reload
# http://127.0.0.1:8000/docs

from fastapi import FastAPI
from pydantic import BaseModel

from model.concept_extractor import extract_concepts
from model.scene_generator import generate_scene
from model.animation_generator import generate_animation_data

app = FastAPI()

class Topic(BaseModel):
    text: str


@app.post("/generate-animation")

def generate_animation(topic: Topic):

    concepts = extract_concepts(topic.text)

    scenes = generate_scene(concepts)

    animation_data = generate_animation_data(scenes)

    return {
        "concepts": concepts,
        "scenes": scenes,
        "animation": animation_data
    }



from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # sab allow (dev ke liye)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)