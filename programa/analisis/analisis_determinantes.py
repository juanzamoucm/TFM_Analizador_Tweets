import spacy
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_hagstag, limpieza_emojis, limpieza_enlaces, limpieza_menciones

nlp = spacy.load("es_core_news_lg")

def info_det(tweet):
    tweet_sin_procesar = limpieza_emojis(tweet)
    tweet_sin_procesar = limpieza_menciones(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_hagstag(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_enlaces(tweet_sin_procesar)
    tweet_limpio = nlp(tweet_sin_procesar)

    diccionario_respuesta = {"Numero_determinantes":"","Determinantes_masc":"","Determinantes_fem":"", "Determinantes_sing":"","Determinantes_plu":"","Determinantes_articulos":"","Determinantes_numerales":"","Determinantes_exclamativos":"","Determinantes_indefinidos":"","Determinantes_demostrativos":""}

    numero_dets = 0
    det_masc = 0
    det_fem = 0
    det_sing = 0
    det_plu = 0
    det_pos = 0
    det_art = 0
    det_exc = 0
    det_dem = 0
    det_ind = 0
    det_num = 0
    lista_articulos_indefinidos =["un", "una", "unos", "unas"]
    #-------- classifying nouns by type
    for token in tweet_limpio:
        # print(token.text, token.pos_)
        if token.pos_ == "DET" or token.pos_=="NUM":
            try:
                if token.morph.get("Gender")[0] == "Masc":
                    det_masc+=1
                if token.morph.get("Gender")[0] == "Fem":
                    det_fem+=1
                if token.morph.get("Gender") != []:
                    numero_dets+=1
            except:
                pass
            try:
                if token.morph.get("Number")[0] == "Sing":
                    det_sing+=1
                if token.morph.get("Number")[0] == "Plur":
                    det_plu+=1
            except:
                pass
            try:
                # print(token.morph.get("PronType"))
                if token.morph.get("PronType")[0] == "Prs":
                    if token.morph.get("Poss")[0] == "Yes":
                        det_pos+=1
                if token.morph.get("PronType")[0] == "Art":
                    if token.text in lista_articulos_indefinidos:
                        det_ind+=1
                    else:
                        det_art+=1
                if token.morph.get("PronType")[0] == "Exc":
                    det_exc+=1
                if token.morph.get("PronType")[0] == "Dem":
                    det_dem+=1
                if token.morph.get("PronType")[0] == "Ind":
                    det_ind+=1
            except:
                pass
            try:
                if token.morph.get("NumType") != []:
                    det_num+=1
                    numero_dets+=1
            except:
                pass
        try:
            if token.text == "del" or token.text == "Del" or token.text == "DEL" or token.text == "al" or token.text == "Al" or token.text == "AL":
                numero_dets+=1
                det_masc+=1
                det_sing+=1
                det_art+=1
        except:
            pass

    diccionario_respuesta["Numero_determinantes"] = numero_dets
    diccionario_respuesta["Determinantes_masc"] = det_masc
    diccionario_respuesta["Determinantes_fem"] = det_fem
    diccionario_respuesta["Determinantes_sing"] = det_sing
    diccionario_respuesta["Determinantes_plu"] = det_plu
    diccionario_respuesta["Determinantes_posesivos"] = det_pos
    diccionario_respuesta["Determinantes_articulos"] = det_art
    diccionario_respuesta["Determinantes_exclamativos"] = det_exc
    diccionario_respuesta["Determinantes_indefinidos"] = det_ind
    diccionario_respuesta["Determinantes_numerales"] = det_num
    diccionario_respuesta["Determinantes_demostrativos"] = det_dem

    return diccionario_respuesta

# info_det(tweet)