import re
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_excepto_tildes

def detect_signos_puntuacion(tweet):
    diccionario_respuesta = {"Numero_signos_puntuacion":""}
    regex_sign_punt = r",|\.|:|;|-|\"|\(|\)|!|¡|¿|\?|\/|\\|'|{|}|\[|\]"
    tweet = limpieza_excepto_tildes(tweet)
    # patron_hagstag = r"\B(\#[a-zA-Z]+\b)(?!;)"
    # patron_webs = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
    # tweet = re.sub(patron_hagstag, '', tweet)
    # tweet = re.sub(patron_webs, '', tweet)
    numero_sign_punt = len(re.findall(regex_sign_punt, tweet))
    diccionario_respuesta["Numero_signos_puntuacion"] = numero_sign_punt
    return diccionario_respuesta