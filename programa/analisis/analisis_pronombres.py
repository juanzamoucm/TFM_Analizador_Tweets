import spacy
# from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_hagstag, limpieza_emojis, limpieza_menciones, limpieza_enlaces
import re

nlp = spacy.load("es_core_news_lg")

tweet = "Nos dicen que vayamos a verlos que nos han echado de menos"

def info_pron(tweet):
    # tweet_sin_procesar = limpieza_emojis(tweet)
    # tweet_sin_procesar = limpieza_menciones(tweet_sin_procesar)
    # tweet_sin_procesar = limpieza_hagstag(tweet_sin_procesar)
    # tweet = limpieza_enlaces(tweet_sin_procesar)
    tweet = nlp(tweet)
    diccionario_respuesta = {"Numero_pronombres":"","Pronombres_masc":"","Pronombres_fem":"", "Pronombres_sing":"","Pronombres_plu":"","Pronombres_personales":"","Pronombres_relativos":"","Pronombres_indefinidos":"","Pronombres_demostrativos":"","Pronombres_interrogativos":"","Pronombres_numerales":"","Pronombres_posesivos":""}

    numero_prons = 0
    pron_masc = 0
    pron_fem = 0
    pron_sing = 0
    pron_plu = 0
    pron_pers = 0
    pron_pos = 0
    pron_int = 0
    pron_dem= 0
    pron_ind = 0
    pron_rel = 0
    pron_num = 0
    lista_posibles_encliticos = ["lo","la","los","las","me","te","se","nos","os","le","les"]
    lista_posesivos = ["mio","mia","mios","mias","mío","mía","míos","mías","tuyo","tuyos","tuya","tuyas","suyo","suyos","suya","suyas","nuestro","nuestros","nuestra","nuestras","vuestro","vuestros","vuestra","vuestras"]
    # lista_posibles_encliticos_solos = ["lo","la","los","las","me","te","se","nos","melo","mela","melos","melas","telo","tela","telos","telas","selo","sela","selos","selas","noslo","nosla","noslos","noslas"]
    palabras_rescatadas = []

    for token in tweet:
        # print(token.text)
        if token.pos_ == "PRON" or token.pos_ == "NUM" or token.text in lista_posesivos:
            palabras_rescatadas.append(token.text)
            if token.text in lista_posesivos:
                if token.pos_ == "DET":
                    pass
                else:
                    pron_pos+=1
                    if token.text.endswith("s"):
                        pron_plu+=1
                    else:
                        pron_sing+=1
                    if token.text.endswith("o") or token.text.endswith("os"):
                        pron_masc+=1
                    if token.text.endswith("a") or token.text.endswith("as"):
                        pron_fem+=1
            try:
                if token.morph.get("Gender")[0] == "Masc":
                    pron_masc+=1
                if token.morph.get("Gender")[0] == "Fem":
                    pron_fem+=1
            except:
                pass
            try:
                if token.morph.get("Number")[0] == "Sing":
                    pron_sing+=1
                if token.morph.get("Number")[0] == "Plur":
                    pron_plu+=1
            except:
                pass
            try:
                if token.morph.get("PronType")[0] == "Prs":
                    try:
                        if token.morph.get("Poss")[0] == "Yes":
                            pron_pos+=1
                            numero_prons+=1
                    except:
                        pron_pers+=1
                        numero_prons+=1
                if token.morph.get("PronType")[0] == "Int" or token.morph.get("PronType")[0] == "Rel":
                    # print(tweet.text)
                    if "¿" in tweet.text or "?" in tweet.text:
                        pron_int+=1
                        numero_prons+=1
                    else:
                        pron_rel+=1
                        numero_prons+=1
                if token.morph.get("PronType")[0] == "Dem":
                    pron_dem+=1
                    numero_prons+=1
                if token.morph.get("PronType")[0] == "Ind":
                    pron_ind+=1
                    numero_prons+=1
                if token.morph.get("PronType")[0] == "Neg":
                    pron_ind+=1
                    numero_prons+=1
                if token.morph.get("PronType")[0] == "Tot":
                    pron_ind+=1
                    numero_prons+=1
            except:
                pass
            try:
                if token.pos_ == "NUM":
                    if token.dep_ == "nsubj":
                        pron_num+=1
                        numero_prons+=1
            except:
                pass
        try:
            if token.pos_ == "VERB":
                verbo = token.text
                for i in lista_posibles_encliticos:
                    if verbo.endswith(i) and not verbo.endswith("mos"):
                        pron_pers+=1
                        numero_prons+=1
                        verbo = re.sub(i,"",verbo)
                        for i in lista_posibles_encliticos:
                            if verbo.endswith(i):
                                pron_pers+=1
                                numero_prons+=1
                # stemmer_artificial = r'(a|á|e|é|i|í)r\S+|(a|á|e|é|i|í)d\S+|nd\S+'
                # objeto_busqueda = re.search(stemmer_artificial, verbo)
                # fin_verbo = objeto_busqueda.group()
                # if fin_verbo != None:
                #     for i in lista_posibles_encliticos:
                #         if i in fin_verbo:
                #             if verbo.endswith("mos"):
                #                 pass
                #             else:
                #                 pron_pers+=1
                #                 numero_prons+=1
                #     else:
                #         pass
        except:
            pass

        

    diccionario_respuesta["Numero_pronombres"] = numero_prons
    diccionario_respuesta["Pronombres_masc"] = pron_masc
    diccionario_respuesta["Pronombres_fem"] = pron_fem
    diccionario_respuesta["Pronombres_sing"] = pron_sing
    diccionario_respuesta["Pronombres_plu"] = pron_plu
    diccionario_respuesta["Pronombres_personales"] = pron_pers
    diccionario_respuesta["Pronombres_relativos"] = pron_rel
    diccionario_respuesta["Pronombres_indefinidos"] = pron_ind
    diccionario_respuesta["Pronombres_demostrativos"] = pron_dem
    diccionario_respuesta["Pronombres_interrogativos"] = pron_int
    diccionario_respuesta["Pronombres_numerales"] = pron_num
    diccionario_respuesta["Pronombres_posesivos"] = pron_pos

    return diccionario_respuesta



info_pron(tweet)