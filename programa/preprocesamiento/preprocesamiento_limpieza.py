import re

def limpieza (tweet):
    # patron_hagstag = r"\B(\#[a-zA-Z]+\b)(?!;)"
    patron_hagstag = r"\B#\w*[a-zA-Z]+\w*"
    patron_webs = r"(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?\S"
    patron_signos_puntuacion = r"([.,\\/#!$%\\^&\\*;:{}=\\-_`~()])"
    patron_espacios =r"\s{2,}"
    #Aquí se eliminan los hagstags, signos de puntuacion y los enlaces
    tweet = re.sub(patron_hagstag, '', tweet)
    tweet = re.sub(patron_webs, '', tweet)
    tweet = re.sub(patron_signos_puntuacion, ' ', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet


def limpieza_excepto_tildes (tweet):
    patron_hagstag = r"\B#\w*[a-zA-Z]+\w*"
    patron_webs = r"(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?\S"
    patron_espacios =r"\s{2,}"
    tweet = re.sub(patron_espacios, ' ', tweet)
    #Aquí se eliminan los hagstags y los enlaces
    tweet = re.sub(patron_hagstag, '', tweet)
    tweet = re.sub(patron_webs, '', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet

def limpieza_signos_puntuacion (tweet):
    patron_caracteres_a_eliminar = r"([.,\\/#!$%\\^&\\*;:{}=\\-_`~()])"
    patron_espacios =r"\s{2,}"
    #Aquí se eliminan los hagstags y los enlaces
    tweet = re.sub(patron_caracteres_a_eliminar, ' ', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet

def limpieza_emojis(tweet):
    regex_emojis = r'([\U00010000-\U0010ffff]|\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])'
    patron_espacios =r"\s{2,}"
    tweet = re.sub(regex_emojis, '', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet

def limpieza_hagstag(tweet):
    patron_hagstag = r"\B#\w*[a-zA-Z]+\w*"
    patron_espacios =r"\s{2,}"
    tweet = re.sub(patron_hagstag, '', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet

def limpieza_enlaces (tweet):
    patron_webs = r"(https?:\/\/)([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?\S"
    patron_espacios =r"\s{2,}"
    #Aquí se eliminan los hagstags y los enlaces
    tweet = re.sub(patron_webs, '', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet

def limpieza_menciones (tweet):
    patron_menciones = r"@\s?\S+"
    patron_espacios =r"\s{2,}"
    #Aquí se eliminan los hagstags y los enlaces
    tweet = re.sub(patron_menciones, '', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet

    