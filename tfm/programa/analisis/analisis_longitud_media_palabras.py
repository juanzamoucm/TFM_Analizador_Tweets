from statistics import mean, median, mode
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza, limpieza_emojis



def longitud_media_palabras(tweet):
    diccionario_respuesta = {"Longitud_media_palabras":"", "Moda_palabras_tweet":"", "Mediana_palabras_tweet":""}
    #------regex de limpieza
    tweet = limpieza_emojis(tweet)
    tweet = limpieza(tweet)
    #------regex de limpieza
    lista_palabras = tweet.split()
    lista_longitudes = []
    for palabra in lista_palabras:
        longitud_palabra = len(palabra)
        lista_longitudes.append(longitud_palabra)
    

    diccionario_respuesta["Longitud_media_palabras"] = median(lista_longitudes)
    diccionario_respuesta["Moda_palabras_tweet"] = mode(lista_longitudes)
    diccionario_respuesta["Mediana_palabras_tweet"] = mean(lista_longitudes)
    return diccionario_respuesta
