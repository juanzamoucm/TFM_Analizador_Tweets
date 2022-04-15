import re

def limpieza (tweet):
    # patron_hagstag = r"\B(\#[a-zA-Z]+\b)(?!;)"
    patron_hagstag = r"#(\w|\d|\s|á|é|ó|í|ú|Á|É|Ó|Í|Ú|ñ|Ñ)+"
    patron_webs = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
    patron_caracteres_a_eliminar = r"([.,\\/#!$%\\^&\\*;:{}=\\-_`~()])"
    patron_espacios =r"\s{2,}"
    #Aquí se eliminan los hagstags, signos de puntuacion y los enlaces
    tweet = re.sub(patron_hagstag, '', tweet)
    tweet = re.sub(patron_webs, '', tweet)
    tweet = re.sub(patron_caracteres_a_eliminar, ' ', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet


def limpieza_excepto_tildes (tweet):
    patron_hagstag = r"#(\w|\d|\s|á|é|ó|í|ú|Á|É|Ó|Í|Ú|ñ|Ñ)+"
    patron_webs = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
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
    regex_emojis = r'[\U00010000-\U0010ffff]'
    patron_espacios =r"\s{2,}"
    tweet = re.sub(regex_emojis, '', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet

def limpieza_hagstag(tweet):
    patron_hagstag = r"#(\w|\d|\s|á|é|ó|í|ú|Á|É|Ó|Í|Ú|ñ|Ñ)+"
    patron_espacios =r"\s{2,}"
    tweet = re.sub(patron_hagstag, '', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet