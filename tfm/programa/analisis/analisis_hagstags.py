import re

def numero_hagstags(tweet):
    diccionario_respuesta = {"Numero_hagstags":"", "Numero_webs":""}
    #------ regex para encontrar hagstags
    patron_hagstag = r"\B(\#[a-zA-Z]+\b)(?!;)"
    #------ regex para encontrar webs
    patron_webs = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
    #------ preprocesado con eliminacion
    numero_hagstag = len(re.findall(patron_hagstag, tweet))
    numero_webs = len(re.findall(patron_webs, tweet))
    diccionario_respuesta["Numero_hagstags"]= numero_hagstag
    diccionario_respuesta["Numero_webs"]= numero_webs

    return diccionario_respuesta