import pandas as pd

archivo_csv = "tweets_analizados/analisis_finalizado.csv"

def agrupar_por_usuario(archivo_csv):
    df = pd.read_csv(archivo_csv)
    # print(df.head())
    df = df.sort_values(["userid"])
    tweets_usuario = df.groupby(by = (["userid"])).agg({
        "Numero_pasados":"mean",
        "Numero_presentes":"mean",
        "Numero_futuros":"mean",
        # "Numero_condcicionales":"mean",
        "Numero_Infinitivos":"mean",
        "Numero_Gerundios":"mean",
        "Verbos_indicativo":"mean",
        "Verbos_subjuntivo":"mean",
        "Numero_determinantes":"mean",
        "Determinantes_masc":"mean",
        "Determinantes_fem":"mean",
        "Determinantes_sing":"mean",
        "Determinantes_plu":"mean",
        "Determinantes_articulos":"mean",
        "Determinantes_numerales":"mean",
        "Determinantes_exclamativos":"mean",
        "Determinantes_indefinidos":"mean",
        "Determinantes_demostrativos":"mean",
        "Determinantes_posesivos":"mean",
        "Numero_nombres_propios":"mean",
        "Numero_nombres_comunes":"mean",
        "Numero_nombres":"mean",
        "Nombres_singular":"mean",
        "Nombres_plural":"mean",
        "Nombres_masculino":"mean",
        "Nombres_femenino":"mean",
        "Genero_no_detectado":"mean",
        "Numero_no_detectado":"mean",
        "Numero_preposiciones":"mean",
        "Numero_pronombres":"mean",
        "Pronombres_masc":"mean",
        "Pronombres_fem":"mean",
        "Pronombres_sing":"mean",
        "Pronombres_plu":"mean",
        "Pronombres_personales":"mean",
        "Pronombres_relativos":"mean",
        "Pronombres_indefinidos":"mean",
        "Pronombres_demostrativos":"mean",
        "Pronombres_interrogativos":"mean",
        "Pronombres_numerales":"mean",
        "Pronombres_posesivos":"mean",
        "Numero_emojis":"mean",
        "Numero_hagstags":"mean",
        "Numero_webs":"mean",
        "Longitud_media_palabras":"mean",
        "Moda_palabras_tweet":"mean",
        "Mediana_palabras_tweet":"mean",
        "Numero_errores":"mean",
        "Numero_tipos_de_error":"mean",
        "Numero_tildes":"mean",
        "Numero_signos_puntuacion":"mean",
        "Numero_adjetivos":"mean",
        "Adjetivos_masc":"mean",
        "Adjetivos_fem":"mean",
        "Adjetivos_sing":"mean",
        "Adjetivos_plu":"mean",
        "Adjetivos_comparativos":"mean",
        "Adjetivos_numerales":"mean",
        "Adjetivos_calificativos":"mean",
        "Media_palabras_por_sintagma":"mean",
        "Numero_sintagmas":"mean"
    })
    tweets_usuario.to_csv('tprueba_1.csv')
    # print(tweets_usuario.head())
    # df_final = pd.DataFrame()
    # for i in tweets_usuario:
    #     hacer_media(i)
    # hacer_media(tweets_usuario.first())
    # tweets_usuario.first().to_csv('tprueba_1.csv')
    # for i in  tweets_usuario.iloc[:, 6:]:
    #     print(i)
    # lista_usuarios = columna.values
    # print(lista_usuarios)




# def hacer_media(df):
#     media_Numero_pasados = sum(df["Numero_pasados"])/len(df["Numero_pasados"])
#     nueva_fila = {'userid':,'Numero_pasados':media_Numero_pasados, 'Numero_presentes', 'Numero_futuros', 'Numero_Infinitivos', 'Numero_Gerundios', 'Verbos_indicativo', 'Verbos_subjuntivo', 'Numero_determinantes', 'Determinantes_masc', 'Determinantes_fem', 'Determinantes_sing', 'Determinantes_plu', 'Determinantes_articulos', 'Determinantes_numerales', 'Determinantes_exclamativos', 'Determinantes_indefinidos', 'Determinantes_demostrativos', 'Determinantes_posesivos', 'Numero_nombres_propios', 'Numero_nombres_comunes', 'Numero_nombres', 'Nombres_singular', 'Nombres_plural', 'Nombres_masculino', 'Nombres_femenino', 'Genero_no_detectado', 'Numero_no_detectado', 'Numero_preposiciones', 'Numero_pronombres', 'Pronombres_masc', 'Pronombres_fem', 'Pronombres_sing', 'Pronombres_plu', 'Pronombres_personales', 'Pronombres_relativos', 'Pronombres_indefinidos', 'Pronombres_demostrativos', 'Pronombres_interrogativos', 'Pronombres_numerales', 'Pronombres_posesivos', 'Analisis_sentimiento', 'Numero_emojis', 'Numero_hagstags', 'Numero_webs', 'Longitud_media_palabras', 'Moda_palabras_tweet', 'Mediana_palabras_tweet', 'Numero_errores', 'Numero_tipos_de_error', 'Numero_tildes', 'Numero_signos_puntuacion','Numero_adjetivos','Adjetivos_masc','Adjetivos_fem', 'Adjetivos_sing','Adjetivos_plu','Adjetivos_comparativos','Adjetivos_numerales','Adjetivos_calificativos','Media_palabras_por_sintagma','Numero_sintagmas'}
#     return media_Numero_pasados


agrupar_por_usuario(archivo_csv)