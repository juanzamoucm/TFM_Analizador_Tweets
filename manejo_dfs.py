import pandas as pd

archivo_csv = "tweets_analizados/97000_analizados_bueno.csv"

def agrupar_por_usuario(archivo_csv):
    df = pd.read_csv(archivo_csv)
    # print(df.head())
    tweets_usuario = df.groupby(by = (["userid","screen_name"])).agg({
        "Numero_pasados":"mean",
        "Numero_presentes":"mean",
        "Numero_futuros":"mean",
        "Numero_condicionales":"mean",
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
        "Media_palabras_por_constituyente":"mean",
        "Numero_constituyentes":"mean"
    })

    tweets_usuario = tweets_usuario.round(2)

    tweets_usuario.to_csv('tweets_por_usuario_bueno.csv')

# agrupar_por_usuario(archivo_csv)

# aquí se mete el csv que solamente tiene los datos del sentimiento y la renta para después unirlo al df general. Está en corpus/FullUsuarios_renta_y_sentimiento.csv
def agrupar_por_usuario_dos(archivo_csv):
    df = pd.read_csv(archivo_csv)
    # print(df.head())
    tweets_usuario = df.groupby(by = (["userid"])).agg({
        "Renta_zona_usuario":"mean",
        "sentiment":"mean"
    })

    tweets_usuario = tweets_usuario.round(2)

    tweets_usuario.to_csv('renta_y_sentimiento_por_usuario.csv')


# agrupar_por_usuario_dos("corpus/FullUsuarios_renta_y_sentimiento.csv")

# Unir dos df a partir de una columna X. Aquí se utiliza para unir el df con rentas y sentiment analysis al df con el análisis nuestro
def Unir_DF(df_1,df_2,columna_union,nombre_nuevo):
    df_primero = pd.read_csv(df_1)
    df_segundo = pd.read_csv(df_2)

    df_final = pd.merge(df_primero, df_segundo, on=columna_union)
    df_final = df_final.set_index("userid")
    df_final.to_csv(f"{nombre_nuevo}.csv")

    return df_final

# Unir_DF("tweets_por_usuario_bueno.csv","renta_y_sentimiento_por_usuario.csv","userid","csv_analisis_final_bueno")

# Devolver una columna
def extraer_columna(df, columna):
    columna = df.loc[:,[columna]]
    return columna

# Calcular la media de una columna dada
def calcular_media(archivo_csv, columna):
    df = pd.read_csv(archivo_csv)
    media_columna = df[columna].mean()

    return media_columna

# Dividir a usuarios por renta. Se divide el df en 3 cuantiles: el tercio con renta mas baja, el tercio con renta media y el tercio con renta alta. después se generan dos csv uno con renta baja y otro con renta alta
def division_cuantiles(archivo_csv):
    df = pd.read_csv(archivo_csv)
    bajo = df.Renta_zona_usuario.quantile(1/3)#tercio inferior o renta baja
    alto = df.Renta_zona_usuario.quantile(2/3)#tercio superior o renta alta

    renta_alta = df[ df.Renta_zona_usuario > alto ]
    renta_alta = renta_alta.set_index("userid")
    renta_baja = df[ df.Renta_zona_usuario < bajo ]
    renta_baja = renta_baja.set_index("userid")
    renta_alta.to_csv("renta_alta.csv")
    renta_baja.to_csv("renta_baja.csv")

# division_cuantiles("csv_analisis_final_bueno.csv")

#  Comparacion dataframes. Se reciben dos dfs y se crea un nuevo csv con dos filas. Las filas contienen la media de cada parametro, cada fila mostrará los datos de un tipo de renta. 
def comparar_dfs(archivo_csv_1, archivo_csv_2):
    df_cabecera = pd.read_csv(archivo_csv_1)
    cabecera_sucia = df_cabecera.columns.values.tolist()
    cabecera = [i for i in cabecera_sucia if i != "userid" and i != "screen_name"]
    df_comparador = pd.DataFrame(columns=cabecera)
    diccionario_df1 = {"tipo_renta":"rentas_altas"}
    for i in cabecera:
        media = round(calcular_media(archivo_csv_1,i),2) 
        diccionario_df1[i] = media
    diccionario_df2 = {"tipo_renta":"rentas_bajas"}
    for i in cabecera:
        media = round(calcular_media(archivo_csv_2,i),2) 
        diccionario_df2[i] = media
    df_comparador = df_comparador.append(diccionario_df1, ignore_index=True)
    df_comparador = df_comparador.append(diccionario_df2, ignore_index=True)
    df_comparador.to_csv("medias_parametros.csv")

# comparar_dfs("renta_alta.csv", "renta_baja.csv")

# Esta función limpia el análisis de los tweets de testing para repetirlo
def crear_nuev_df_desde_columnas(archivo_csv):
    df = pd.read_csv(archivo_csv)
    df_nuevo = df.iloc[:,[0,1,2,3,4]]
    df_nuevo = df_nuevo.set_index("id_tweet")
    df_nuevo.to_csv("tweets_testing_limpio.csv")

# crear_nuev_df_desde_columnas(archivo_csv)
