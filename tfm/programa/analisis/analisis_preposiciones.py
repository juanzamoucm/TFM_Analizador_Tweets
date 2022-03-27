import spacy
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza, limpieza_emojis

nlp = spacy.load("es_core_news_lg")

def info_preposiciones(tweet):
    tweet = limpieza_emojis(tweet)
    tweet = limpieza(tweet)
    diccionario_respuesta = {"Numero_preposiciones":""}
    num_prep = 0
    tweet = nlp(tweet)
    for token in tweet:
        if token.pos_ == "ADP":
            num_prep+=1

    diccionario_respuesta["Numero_preposiciones"] = num_prep

    return diccionario_respuesta