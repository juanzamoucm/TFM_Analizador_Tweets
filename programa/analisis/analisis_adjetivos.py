import spacy
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_hagstag, limpieza_emojis, limpieza_menciones, limpieza_enlaces

nlp = spacy.load("es_core_news_lg")

def info_adj(tweet):
    tweet_sin_procesar = limpieza_emojis(tweet)
    tweet_sin_procesar = limpieza_menciones(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_hagstag(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_enlaces(tweet_sin_procesar)
    tweet_limpio = nlp(tweet_sin_procesar)
    diccionario_respuesta = {"Numero_adjetivos":"","Adjetivos_masc":"","Adjetivos_fem":"", "Adjetivos_sing":"","Adjetivos_plu":"","Adjetivos_comparativos":"","Adjetivos_numerales":"","Adjetivos_calificativos":""}

    numero_adj = 0
    adj_masc = 0
    adj_fem = 0
    adj_sing = 0
    adj_plu = 0
    adj_num = 0
    adj_cal = 0
    adj_comp = 0

    for token in tweet_limpio:
        if token.pos_ == "ADJ":
            numero_adj+=1
            # print(token)
            try:
                if token.morph.get("Gender")[0] == "Masc":
                    adj_masc+=1
                if token.morph.get("Gender")[0] == "Fem":
                    adj_fem+=1
            except:
                pass
            try:
                if token.morph.get("Number")[0] == "Sing":
                    adj_sing+=1
                if token.morph.get("Number")[0] == "Plur":
                    adj_plu+=1
            except:
                pass
            try:
                if token.morph.get("NumType")[0] == "Ord":
                    adj_num+=1
            except:
                pass
            try:
                if token.morph.get("Degree")[0] == "Cmp":
                    adj_comp+=1
            except:
                adj_cal+=1

    diccionario_respuesta["Numero_adjetivos"] = numero_adj
    diccionario_respuesta["Adjetivos_masc"] = adj_masc
    diccionario_respuesta["Adjetivos_fem"] = adj_fem
    diccionario_respuesta["Adjetivos_sing"] = adj_sing
    diccionario_respuesta["Adjetivos_plu"] = adj_plu
    diccionario_respuesta["Adjetivos_comparativos"] = adj_comp
    diccionario_respuesta["Adjetivos_numerales"] = adj_num
    diccionario_respuesta["Adjetivos_calificativos"] = adj_cal

    return diccionario_respuesta