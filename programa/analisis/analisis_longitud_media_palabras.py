from statistics import mean, median, mode
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_emojis



def longitud_media_palabras(tweet):
    diccionario_respuesta = {"Longitud_media_palabras":"", "Moda_palabras_tweet":"", "Mediana_palabras_tweet":""}
    #------regex de limpieza
    tweet = limpieza_emojis(tweet)
    #------regex de limpieza
    lista_palabras = tweet.split()
    lista_longitudes = []
    for palabra in lista_palabras:
        longitud_palabra = len(palabra)
        lista_longitudes.append(longitud_palabra)
    
    try:
        diccionario_respuesta["Longitud_media_palabras"] = mean(lista_longitudes)
        diccionario_respuesta["Moda_palabras_tweet"] = mode(lista_longitudes)
        diccionario_respuesta["Mediana_palabras_tweet"] = median(lista_longitudes)
    except:
        diccionario_respuesta["Longitud_media_palabras"] = 0
        diccionario_respuesta["Moda_palabras_tweet"] = 0
        diccionario_respuesta["Mediana_palabras_tweet"] = 0
    return diccionario_respuesta
