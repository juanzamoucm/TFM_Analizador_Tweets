import spacy
# from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_hagstag, limpieza_emojis, limpieza_menciones, limpieza_enlaces
import re

nlp = spacy.load("es_core_news_lg")

tweet = """Muere Verónica Forqué: ha sido hallada sin vida en su casa de Madrid
 https://t.co/DEKtYH6sca vía @diarioas

QEPD

La depresión mata

"La actriz, que hace tan solo unos días cumplió 66 años, había participado recientemente
 en 'MasterChef Celebrity' y se tuvo que retirar agotada"""


def limpieza_emojis(tweet):
    regex_emojis = r'([\U00010000-\U0010ffff]|\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])'
    patron_espacios =r"\s{2,}"
    tweet = re.sub(regex_emojis, '', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet

def limpieza_hagstag(tweet):
    patron_hagstag = r"\B#\w*[a-zA-Z]+\w*"
    patron_espacios =r"\s{2,}"
    tweet = re.sub(patron_hagstag, '', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet

def limpieza_enlaces (tweet):
    patron_webs = r"(https?:\/\/)([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?\S"
    patron_espacios =r"\s{2,}"
    #Aquí se eliminan los hagstags y los enlaces
    tweet = re.sub(patron_webs, '', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet

def limpieza_menciones (tweet):
    patron_menciones = r"@\s?\S+"
    patron_espacios =r"\s{2,}"
    #Aquí se eliminan los hagstags y los enlaces
    tweet = re.sub(patron_menciones, '', tweet)
    tweet = re.sub(patron_espacios, ' ', tweet)

    return tweet

    

def info_nombres(tweet):
    tweet_sin_procesar = limpieza_emojis(tweet)
    tweet_sin_procesar = limpieza_menciones(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_hagstag(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_enlaces(tweet_sin_procesar)
    tweet_sin_procesar = tweet_sin_procesar.lower()
    tweet_limpio = nlp(tweet_sin_procesar)
    diccionario_respuesta = {"Numero_nombres_propios":"","Numero_nombres_comunes":"","Numero_nombres":"","Nombres_singular":"","Nombres_plural":"","Nombres_masculino":"", "Nombres_femenino":"", "Genero_no_detectado":"", "Numero_no_detectado":""}
    
    generos = []
    numeros = []

    nombres_propios = 0
    nombres_comunes = 0
    numero_nombres = 0
    genero_no_detectado = 0
    numero_no_detectado = 0
    #-------- classifying nouns by type
    for token in tweet_limpio:
        if token.pos_ == "PROPN":
            numero_nombres+=1
            nombres_propios+=1
            # print(token.morph)
            if token.morph.get("Gender") != []:
                # print(token.morph)
                generos.append(token.morph.get("Gender"))
            else:
                genero_no_detectado+=1
            if token.morph.get("Number") != []:
                numeros.append(token.morph.get("Number"))
            else:
                numero_no_detectado+=1
        if token.pos_ == "NOUN":
            numero_nombres+=1
            nombres_comunes+=1
            # print(token.morph)
            if token.morph.get("Gender") != []:
                # print(token.morph)
                generos.append(token.morph.get("Gender"))
            else:
                genero_no_detectado+=1

            if token.morph.get("Number") != []:
                numeros.append(token.morph.get("Number"))
            else:
                numero_no_detectado+=1
    #-------- classifying nouns by type
    numero_masculinos = 0
    numero_femeninos = 0
    for i in generos:
        if i[0] == "Masc":
            numero_masculinos +=1
        if i[0] == "Fem":
            numero_femeninos +=1
    numero_singulares = 0
    numero_plurales = 0
    for i in numeros:
        if i[0] == "Sing":
            numero_singulares +=1
        if i[0] == "Plur":
            numero_plurales +=1
        
    diccionario_respuesta["Numero_nombres_propios"] = nombres_propios
    diccionario_respuesta["Numero_nombres_comunes"] = nombres_comunes   
    diccionario_respuesta["Numero_nombres"] = numero_nombres
    diccionario_respuesta["Nombres_singular"] = numero_singulares
    diccionario_respuesta["Nombres_plural"] = numero_plurales
    diccionario_respuesta["Nombres_masculino"] = numero_masculinos
    diccionario_respuesta["Nombres_femenino"] = numero_femeninos
    diccionario_respuesta["Genero_no_detectado"] = genero_no_detectado
    diccionario_respuesta["Numero_no_detectado"] = numero_no_detectado

    return diccionario_respuesta



info_nombres(tweet)