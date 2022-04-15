import emoji 

def extract_emojis(tweet):
    diccionario_respuesta = {"Numero_emojis":""}
    emojis = [emoticono for emoticono in tweet if emoticono in emoji.UNICODE_EMOJI['es']]
    numero_emojis = len(emojis)
    diccionario_respuesta["Numero_emojis"] = numero_emojis
    return diccionario_respuesta