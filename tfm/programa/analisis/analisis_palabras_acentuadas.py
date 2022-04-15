from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_excepto_tildes

def detectar_acentos(tweet):
    diccionario_respuesta = {"Numero_tildes":""}
    tweet = limpieza_excepto_tildes(tweet)
    lista_posibilidades = ["á","ó","é","í","ú","Á","Ó","É","Í","Ú"]
    numero_tildes = 0
    for letra in tweet:
        if letra in lista_posibilidades:
            numero_tildes+=1 

    diccionario_respuesta["Numero_tildes"] = numero_tildes
    return diccionario_respuesta        