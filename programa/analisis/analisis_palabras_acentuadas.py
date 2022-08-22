from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_hagstag, limpieza_emojis, limpieza_menciones, limpieza_enlaces

def detectar_acentos(tweet):
    diccionario_respuesta = {"Numero_tildes":""}
    tweet_sin_procesar = limpieza_emojis(tweet)
    tweet_sin_procesar = limpieza_menciones(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_hagstag(tweet_sin_procesar)
    tweet = limpieza_enlaces(tweet_sin_procesar)
    lista_posibilidades = ["á","ó","é","í","ú","Á","Ó","É","Í","Ú"]
    numero_tildes = 0
    for letra in tweet:
        if letra in lista_posibilidades:
            numero_tildes+=1 

    diccionario_respuesta["Numero_tildes"] = numero_tildes
    return diccionario_respuesta        