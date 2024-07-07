import os
import tempfile
from fastapi import FastAPI, File, UploadFile
import torch
from moviepy.editor import VideoFileClip
from backend.scripts.model import Model
import firebase_admin
from firebase_admin import credentials, firestore
import uuid


app = FastAPI()
model = Model()
cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
class Video():
    video_id: str
    video: UploadFile = File(...)

@app.post("/getquiz")
async def get_quiz(video: UploadFile = File(...)):
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save the uploaded video to the temporary directory
        temp_video_path = os.path.join(temp_dir, video.filename)
        temp_audio_path = os.path.join(temp_dir, "extracted_audio.wav")
        with open(temp_video_path, "wb") as buffer:
            buffer.write(await video.read())
        
        q, a = model.eval(video_file=temp_video_path, audio_file=temp_audio_path)
    # Return the results
    result = postprocessing(q, a)
    return result

@app.get("/quizme")
async def get_quiz(video_id):
    doc_ref = db.collection('videos').document(video_id)
    doc = doc_ref.get()
    return doc.to_dict()

@app.post("/savequiz")
async def save_quiz(video_id, quiz):
    doc_ref = db.collection('videos').document(video_id)
    doc_ref.set(quiz)



def postprocessing(q, a):
    for line in q.splitlines():
        if line.startswith("Question:"):
            question = line.split(":")[1].strip()
        elif line.startswith("A)"):
            A = line.split(")")[1].strip()
        elif line.startswith("B)"):
            B = line.split(")")[1].strip()
        elif line.startswith("C)"):
            C = line.split(")")[1].strip()
        elif line.startswith("D)"):
            D = line. split(")")[1].strip()
    return {
        "question":  question,
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "answer": a
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)