import spacy
from statistics import mean
import string
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_hagstag, limpieza_emojis, limpieza_menciones, limpieza_enlaces

nlp = spacy.load("es_core_news_lg")

def info_sintactica(tweet):
    tweet_sin_procesar = limpieza_emojis(tweet)
    tweet_sin_procesar = limpieza_menciones(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_hagstag(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_enlaces(tweet_sin_procesar)
    tweet_limpio = nlp(tweet_sin_procesar)
    diccionario_respuesta = {"Media_palabras_por_constituyente":"","Numero_constituyentes":""}

    numero_constituyentes = 0
    longitud_media_constituyentes = 0
    constituyentes = []

    #Extracción de  constituyentes
    for palabra in tweet_limpio:
        constituyentes.append([t for t in palabra.subtree])

    #Eliminación de constituyentes únicos
    lista_borrado = []
    for constituyente in constituyentes:
        if len(constituyente) <= 1:
            lista_borrado.append(constituyente)
    constituyentes_tweet = [x for x in constituyentes if x not in lista_borrado]
    numero_constituyentes = len(constituyentes_tweet)

    longitud_media_constituyentes = []

    lista_borrado_2 = []
    constituyentes_tweets_no_signos = []
    for i in constituyentes_tweet:
        for eliminador in i:
            if eliminador.text in string.punctuation:
                lista_borrado_2.append(eliminador)
    for i in constituyentes_tweet:
        constituyente_limpio = [x for x in i if x not in lista_borrado_2]
        constituyentes_tweets_no_signos.append(constituyente_limpio)

    for i in constituyentes_tweets_no_signos:
        longitud_media_constituyentes.append(len(i))

    try:
        diccionario_respuesta["Media_palabras_por_constituyente"] = mean(longitud_media_constituyentes)
    except: 
        diccionario_respuesta["Media_palabras_por_constituyente"] = 1
    diccionario_respuesta["Numero_constituyentes"] = numero_constituyentes

    return diccionario_respuesta

# info_sintactica(tweet)

#ATENCION
#Es importante alcarar que no se están analizando constituyentes en el sentido de la sintaxis tradicional
#Sino relaciones de dependencia semántica de las palabras entre sí. Es decir árboles de sintaxis generativa