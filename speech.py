import whisper
# dictionary use for key:value pair for model //key "name":"bunny"

from config import MODEL_NAME


def load_whisper_model():
    """
    load the whisper model use confg model name
    """
    model = whisper.load_model(MODEL_NAME)
    return model


def transcribe_audio(audio_path):
    """
    transcribe audio file of whisper model
    """
    model = load_whisper_model()
    result = model.transcribe(audio_path,)
    
    return result["text"]




    
    