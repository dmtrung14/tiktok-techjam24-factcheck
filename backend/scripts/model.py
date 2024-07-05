from moviepy.editor import VideoFileClip
import torch
from transformers import pipeline
from backend.config import Config

class Model:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.whisper  = pipeline("automatic-speech-recognition",
                        "openai/whisper-large-v2",
                        device=self.device)
        self.pipe = pipeline("text-generation", model="Qwen/Qwen2-1.5B-Instruct", device=self.device, max_new_tokens=1000)
        self.base_messages = Config.Model.base_messages

    def extract_audio(self, video_file, audio_file):
        video = VideoFileClip(video_file)
        video.audio.write_audiofile(audio_file, codec='pcm_s16le')

    def transcribe_audio(self, audio_file):
        return self.whisper(audio_file)
    
    def quiz(self, text):
        messages = self.base_messages.copy()
        messages.append({"role": "user", "content": f"Generate one multiple choice question with 4 options A,B,C,D for the following prompt: {text['text']}\nDO NOT GIVE AN ANSWER"})
        response = self.pipe(messages)
        question = response[0]['generated_text'][-1]['content']
        messages.append({"role": "assistant", "content": question})
        messages.append({"role": "user", "content": "So what is the right answer to your quiz. Answer with a single character."})
        response = self.pipe(messages)
        result = response[0]['generated_text'][-1]['content']
        return question, result
    
    def eval(self, video_file = '../test/asset/download.mp4', audio_file = '../test/asset/extracted_audio.wav'):
        # video_file = "/content/download.mp4"
        # audio_file = "/content/extracted_audio.wav"
        self.extract_audio(video_file, audio_file)
        transcription = self.transcribe_audio(audio_file)
        your_quiz =self.quiz(transcription)

        return {
            "quiz": your_quiz
        }

if __name__ == "__main__":
    model = Model()
    model.eval()

