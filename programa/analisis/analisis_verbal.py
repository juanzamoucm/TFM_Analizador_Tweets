import spacy
from spacy.tokens import Doc
import numpy
# import re
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_hagstag, limpieza_emojis, limpieza_enlaces, limpieza_menciones

nlp = spacy.load("es_core_news_lg")

#En esta función se realiza un análisis preliminar de verbos compuestos que luego se eliminan para 
#el posterior procesamiento de estos verbos como tokens individuales. 
def filtro_tokens_verbos_compuestos(tweet):
    posiciones = []
    tiempos_compuestos = []
    modos_verbales = []
    auxiliar_pasado = ["he","has","ha","hemos","habéis","han"]
    for posicion, token in enumerate(tweet):
        try:
            if token.dep_ == "aux" and token.lemma_ == "haber":
                posiciones.append(posicion)
                posiciones.append(posicion+1)
                if token.morph.get("Mood") != []:
                    if token.morph.get("Mood")[0] == "Cnd":
                        modos_verbales.append(["Ind"])
                    else:
                        if token.morph.get("Mood") != []:
                            modos_verbales.append(token.morph.get("Mood"))
                if token.lower_ not in auxiliar_pasado and token.morph.get("Tense") != []:
                    tiempos_compuestos.append(token.morph.get("Tense"))
                elif token.lower_ in auxiliar_pasado:
                    tiempos_compuestos.append("Past")
                else:
                    pass
        except:
            pass
    objeto_tweet_lista = tweet.to_array(['LEMMA'])
    objeto_tweet_lista = numpy.delete(objeto_tweet_lista, posiciones, axis=0)
    tweet_limpio = Doc(tweet.vocab, words=[t.text for i, t in enumerate(tweet) if i not in posiciones])
    tweet_limpio.from_array(['LEMMA'], objeto_tweet_lista)
    return tweet_limpio.text, tiempos_compuestos, modos_verbales

#Esta función lleva a cabo el análisis de los tiempos verbales del tweet devolviendo un diccionario con la siguiente estructura
#diccionario_respuesta = {"Numero_pasados":"","Numero_presentes":"","Numero_futuros":"","Numero_Infinitivos":"","Numero_Gerundios":"", "Verbos_indicativo":"","Verbos_subjuntivo":""}

def info_verbal(tweet):
    tweet = limpieza_emojis(tweet)
    tweet = limpieza_enlaces(tweet)
    tweet = limpieza_hagstag(tweet)
    tweet = limpieza_menciones(tweet)
    tweet_previa_limpieza = nlp(tweet)
    objeto_tweet = filtro_tokens_verbos_compuestos(tweet_previa_limpieza)
    tweet_limpio = nlp(objeto_tweet[0])
    diccionario_respuesta = {"Numero_pasados":"","Numero_presentes":"","Numero_futuros":"","Numero_condicionales":"","Numero_Infinitivos":"","Numero_Gerundios":"", "Verbos_indicativo":"","Verbos_subjuntivo":""}
    
    tiempos_verbales = objeto_tweet[1]
    modos_verbales = objeto_tweet[2]
    verbos_rescatados = []
    lista_futuros = ["aré","eré","iré","rás","rá","remos","réis","rán"]
    lista_condicional = ["ía","íás","íá","íamos","íais","rían"]
    lista_seg_pers_plu = ["áis","éis","ís"]
    numero_pasados = 0
    numero_futuros = 0
    numero_presentes = 0
    numero_infinitivos = 0
    numero_gerundios = 0
    numero_condicionales= 0

    numero_indicativos = 0
    numero_subjuntivos = 0
    
    for token in tweet_limpio:
        # print(token.text)
        if token.pos_ == "VERB" or token.pos_ == "AUX":
            for i in lista_seg_pers_plu:
                if token.text.endswith(i):
                    verbos_rescatados.append(token.text)
                    numero_presentes+=1
                    numero_indicativos+=1
                    break
            if token.lemma_.endswith("ar") or token.lemma_.endswith("er") or token.lemma_.endswith("ir"):
            # if token.morph.get("Tense") != []:
                for i in lista_futuros:
                    if token.suffix_ == i:
                        numero_futuros +=1
                        verbos_rescatados.append(token.text)
                        break
                for i in lista_condicional:
                    if token.text == f"{token.lemma_}{i}":
                        numero_condicionales +=1
                        verbos_rescatados.append(token.text)
                        break
                if token.morph.get("Tense") != "Fut" and token.morph.get("Tense") != [] and token.text not in verbos_rescatados:
                    tiempos_verbales.append(token.morph.get("Tense"))
                # print(tiempos_verbales)
                if token.morph.get("Mood") != []:
                    if token.morph.get("Mood")[0] == "Cnd":
                        modos_verbales.append(["Ind"])
                    else:
                        modos_verbales.append(token.morph.get("Mood"))
                # print(modo_predominante)
                if token.morph.get("Tense") == [] and token.morph.get("Mood") == [] and token.morph.get("Person") == []:
                    if token.text.endswith("ar") or token.text.endswith("er") or token.text.endswith("ir"):
                        tiempos_verbales.append("Infinitivo")
                    if token.suffix_=="ndo":
                        tiempos_verbales.append("Gerundio")
    
    for verbo in tiempos_verbales:
        if verbo[0]!= []:
            if verbo[0] == "Past" or verbo[0] == "Imp" or verbo[0] == "Pqp" or verbo == "Past":
                numero_pasados = numero_pasados + 1
                # print(numero_pasados)
            if verbo[0] == "Fut":
                numero_futuros = numero_futuros + 1
                # print(numero_futuros)
            if verbo[0] == "Pres":
                numero_presentes = numero_presentes + 1
                # print(numero_presentes)
            if verbo == "Infinitivo":
                numero_infinitivos = numero_infinitivos + 1
                # print(numero_infinitivos)
            if verbo == "Gerundio":
                numero_gerundios = numero_gerundios + 1
                # print(numero_infinitivos)
        
    diccionario_respuesta["Numero_pasados"] = numero_pasados
    diccionario_respuesta["Numero_presentes"] = numero_presentes
    diccionario_respuesta["Numero_futuros"] = numero_futuros
    diccionario_respuesta["Numero_condicionales"] = numero_condicionales
    diccionario_respuesta["Numero_Infinitivos"] = numero_infinitivos
    diccionario_respuesta["Numero_Gerundios"] = numero_gerundios

    for verbo in modos_verbales:
        if verbo[0] == "Ind":
            numero_indicativos = numero_indicativos + 1
        if verbo[0] == "Sub":
            numero_subjuntivos = numero_subjuntivos + 1
    diccionario_respuesta["Verbos_indicativo"] = numero_indicativos
    diccionario_respuesta["Verbos_subjuntivo"] = numero_subjuntivos

    return diccionario_respuesta

# Limitaciones:
# -El imperativo no se detecta por el modelo 
# -El modelo no es capaz de distinguir entre pretérito perfecto de subjuntivo y aquellas 
# frases en las que se usa el verbo "haber" en presente de subjuntivo. 
# Spacy no reconoce bien la segunda persona del plural del presnte de indicativo

# info_verbal(tweet)