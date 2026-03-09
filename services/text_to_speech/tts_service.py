from gtts import gTTS
import io

def text_to_speech(text):

    tts = gTTS(text)

    audio = io.BytesIO()

    tts.write_to_fp(audio)

    return audio.getvalue()