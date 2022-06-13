import pandas as pd

archivo_csv = "tweets_analizados/analisis_finalizado.csv"

def agrupar_por_usuario(archivo_csv):
    df = pd.read_csv(archivo_csv)
    print(df.head())
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
        "Media_palabras_por_sintagma":"mean",
        "Numero_sintagmas":"mean"
    })

    tweets_usuario = tweets_usuario.round(2)

    tweets_usuario.to_csv('tweets_por_usuario.csv')


agrupar_por_usuario(archivo_csv)
