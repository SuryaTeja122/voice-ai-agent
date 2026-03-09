import whisper
import tempfile

model = whisper.load_model("base")

def speech_to_text(audio_bytes):

    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(audio_bytes)
        temp_path = temp.name

    result = model.transcribe(temp_path)

    return result["text"]