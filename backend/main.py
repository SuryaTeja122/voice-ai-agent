from fastapi import FastAPI, UploadFile, File
from openai import OpenAI
import shutil
import os

app = FastAPI()




@app.get("/")
def home():
    return {"message": "Voice AI Backend Running"}


@app.post("/voice")
async def voice_agent(file: UploadFile = File(...)):

    # Save uploaded audio
    with open("input.wav", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Speech → Text
    transcript = client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe",
        file=open("input.wav", "rb")
    )

    user_text = transcript.text

    # GPT Response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a hospital assistant helping patients book doctor appointments."},
            {"role": "user", "content": user_text}
        ]
    )

    reply = response.choices[0].message.content

    return {
        "user_said": user_text,
        "ai_reply": reply

    }
