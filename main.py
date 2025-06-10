# backend/main.py
import random
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now; lock down to your Vercel domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CHAPTER_IMAGES = {
    "0": ["park1.jpeg", "park2.jpeg", "park3.jpeg", "park4.jpeg", "park5.jpeg"],
    "1": ["formal1.jpeg", "formal2.jpeg", "formal3.jpeg", "formal4.jpeg", "formal5.jpeg"],
    "2": ["painting1.jpeg", "painting2.jpeg"],
    "3": ["astros1.jpeg", "astros2.jpeg", "astros3.jpeg"],
    "4": ["boots1.jpeg", "boots2.jpeg"],
    "5": ["rodeo.jpeg", "rodeo1.jpeg", "rodeo2.jpeg", "rodeo3.jpeg"],
}


@app.get("/api/ping")
def ping():
    return {"message": "pong from backend"}


@app.get("/api/chapter")
def chapter_list():
    return [
        "A picnic in the park",
        "Amazing Formal!",
        "Painting Away",
        "Astros Game!",
        "Boots & Bowties",
        "Our First Date",
    ]


@app.get("/api/chapter/{chapter}")
def chapter(chapter: str):
    mapping = {
        "0": "gderness",
        "3": "dhtgoo",
        "2": "frgilrnied",
        "4": "tncodytcona",
        "1": "miscalpid",
        "5": "werta",
    }
    return mapping.get(chapter, "help")


@app.post("/api/answer/{answer}/{chapter}")
def validate(answer: str, chapter: str):
    # 1) check correctness
    correct = False
    if chapter == "0" and answer.lower() == "green dress":
        correct = True
    elif chapter == "1" and answer.lower() == "dicamplis":
        correct = True
    elif chapter == "2" and answer.lower() == "girlfriend":
        correct = True
    elif chapter == "3" and answer.lower() == "hotdog":
        correct = True
    elif chapter == "4" and answer.lower() == "cotton candy":
        correct = True
    elif chapter == "5" and answer.lower() == "water":
        correct = True

    if not correct:
        return {"correct": False}

    # 2) pick a random image for the correct chapter
    filenames = CHAPTER_IMAGES.get(chapter)
    if not filenames:
        raise HTTPException(status_code=404, detail="No images for this chapter")

    selected = random.choice(filenames)
    # 3) return relative URL (frontend serves /images/… from public/)
    return {"correct": True, "image_url": f"/images/{selected}"}