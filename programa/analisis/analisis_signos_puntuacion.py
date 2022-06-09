import re
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_hagstag, limpieza_emojis, limpieza_menciones, limpieza_enlaces

def detect_signos_puntuacion(tweet):
    diccionario_respuesta = {"Numero_signos_puntuacion":""}
    regex_sign_punt = r",|\.|:|;|-|\"|\(|\)|!|¡|¿|\?|\/|\\|'|{|}|\[|\]"
    tweet_sin_procesar = limpieza_emojis(tweet)
    tweet_sin_procesar = limpieza_menciones(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_hagstag(tweet_sin_procesar)
    tweet = limpieza_enlaces(tweet_sin_procesar)
    numero_sign_punt = len(re.findall(regex_sign_punt, tweet))
    diccionario_respuesta["Numero_signos_puntuacion"] = numero_sign_punt
    return diccionario_respuesta