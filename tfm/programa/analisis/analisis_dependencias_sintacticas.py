import spacy
from statistics import mean
import string
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_emojis, limpieza_hagstag

nlp = spacy.load("es_core_news_lg")

def info_sintactica(tweet):
    tweet_preparado = limpieza_emojis(tweet)
    tweet_listo = limpieza_hagstag(tweet_preparado)
    tweet_limpio = nlp(tweet_listo)
    diccionario_respuesta = {"Media_palabras_por_sintagma":"","Numero_sintagmas":""}

    numero_sintagmas = 0
    longitud_media_sintagmas = 0
    sintagmas = []

    #Extracción de  sintagmas
    for palabra in tweet_limpio:
        sintagmas.append([t for t in palabra.subtree])

    #Eliminación de sintagmas únicos
    lista_borrado = []
    for sintagma in sintagmas:
        if len(sintagma) <= 1:
            lista_borrado.append(sintagma)
    sintagmas_tweet = [x for x in sintagmas if x not in lista_borrado]
    numero_sintagmas = len(sintagmas_tweet)

    longitud_media_sintagmas = []

    lista_borrado_2 = []
    sintagmas_tweets_no_signos = []
    for i in sintagmas_tweet:
        for eliminador in i:
            if eliminador.text in string.punctuation:
                lista_borrado_2.append(eliminador)
    for i in sintagmas_tweet:
        sintagma_limpio = [x for x in i if x not in lista_borrado_2]
        sintagmas_tweets_no_signos.append(sintagma_limpio)

    for i in sintagmas_tweets_no_signos:
        longitud_media_sintagmas.append(len(i))

    try:
        diccionario_respuesta["Media_palabras_por_sintagma"] = mean(longitud_media_sintagmas)
    except: 
        diccionario_respuesta["Media_palabras_por_sintagma"] = 1
    diccionario_respuesta["Numero_sintagmas"] = numero_sintagmas

    return diccionario_respuesta

# info_sintactica(tweet)

#ATENCION
#Es importante alcarar que no se están analizando sintagmas en el sentido de la sintaxis tradicional
#Sino relaciones de dependencia semántica de las palabras entre sí. Es decir árboles de sintaxis generativa