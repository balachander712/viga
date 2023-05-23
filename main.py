from fastapi import FastAPI
from routes import audio_elements

app = FastAPI()

# Include the route definitions from audio_elements.py
app.include_router(audio_elements.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)