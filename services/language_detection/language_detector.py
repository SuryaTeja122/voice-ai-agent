from langdetect import detect

def detect_language(text):

    try:
        lang = detect(text)

        if lang == "hi":
            return "hindi"

        if lang == "ta":
            return "tamil"

        return "english"

    except:
        return "english"