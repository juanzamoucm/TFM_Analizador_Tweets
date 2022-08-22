import spacy
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_hagstag, limpieza_emojis, limpieza_menciones, limpieza_enlaces

nlp = spacy.load("es_core_news_lg")

def info_preposiciones(tweet):
    tweet_sin_procesar = limpieza_emojis(tweet)
    tweet_sin_procesar = limpieza_menciones(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_hagstag(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_enlaces(tweet_sin_procesar)
    # tweet_sin_procesar = tweet_sin_procesar.lower()
    tweet_limpio = nlp(tweet_sin_procesar)
    diccionario_respuesta = {"Numero_preposiciones":""}
    num_prep = 0
    tweet = nlp(tweet)
    for token in tweet:
        if token.pos_ == "ADP":
            num_prep+=1

    diccionario_respuesta["Numero_preposiciones"] = num_prep

    return diccionario_respuesta