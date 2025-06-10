# backend/main.py
import random
from http.client import HTTPException

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



CHAPTER_IMAGES = {
    "0": [
        "park1.jpeg",
        "park2.jpeg",
        "park3.jpeg",
        "park4.jpeg",
        "park5.jpeg"
    ],
    "1": [
        "formal1.jpeg",
        "formal2.jpeg",
        "formal3.jpeg",
        "formal4.jpeg",
        "formal5.jpeg"
    ],
    "2": [
        "painting1.jpeg",
        "painting2.jpeg"
    ],
    "3": [
        "astros1.jpeg",
        "astros2.jpeg",
        "astros3.jpeg"
    ],
    "4": [
        "boots1.jpeg",
        "boots2.jpeg"
    ],
    "5": [
        "rodeo.jpeg",
        "rodeo1.jpeg",
        "rodeo2.jpeg",
        "rodeo3.jpeg"
    ],
}

@app.get("/api/ping")
def ping():
    return {"message": "pong from backend"}

@app.get('/api/chapter')
def chapter_list():
    chapter_list = [
        "A picnic in the park",
        "Amazing Formal!",
        "Painting Away",
        "Astros Game!",
        "Boots & Bowties",
        "Our First Date"

    ]

    return chapter_list
@app.get('/api/chapter/{chapter}')
def chapter(chapter):
    if chapter == '0':
        scrambled_word = "gderness"
        return scrambled_word
    elif chapter == '3':
        scrambled_word = "dhtgoo"
        return scrambled_word
    elif chapter == '2':
        scrambled_word = "frgilrnied"
        return scrambled_word
    elif chapter == '4':
        scrambled_word = "tncodytcona"
        return scrambled_word
    elif chapter == '1':
        scrambled_word = "miscalpid"
        return scrambled_word
    elif chapter == '5':
        scrambled_word = "werta"
        return scrambled_word

    return "help"


@app.post('/api/answer/{answer}/{chapter}')
def validate(answer, chapter):
    correct = False
    if chapter == '0':
        if answer.lower() == "green dress":
            correct = True

    elif chapter == '1':
        if answer.lower() == "dicamplis":
            correct = True

    elif chapter == '2':
        if answer.lower() == "girlfriend":
            correct = True

    elif chapter == '3':
        if answer.lower() == "hotdog":
            correct = True

    elif chapter == '4':
        if answer.lower() == "cotton candy":
            correct = True

    elif chapter == '5':
        if answer.lower() == "water":
            correct = True

    if not correct:
        return {"correct": False}

        # Pick one random filename
    filenames = CHAPTER_IMAGES.get(chapter)
    if not filenames:
        raise HTTPException(404, "No images for this chapter")

    selected = random.choice(filenames)
    # Build the URL that Vercel (or Vite) will serve from public/images/
    return {
        "correct": True,
        "image_url": f"/images/{selected}"
    }
