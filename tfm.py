import csv
from programa.analisis.analisis_dependencias_sintacticas import info_sintactica
from programa.preprocesamiento.preprocesamiento_limpieza import *
from programa.analisis.analisis_verbal import info_verbal
from programa.analisis.analisis_pronombres import info_pron
from programa.analisis.analisis_determinantes import info_det
from programa.analisis.analisis_nombres import info_nombres
from programa.analisis.analisis_preposiciones import info_preposiciones
from programa.analisis.analisis_adjetivos import info_adj
from programa.analisis.analisis_emoticonos import extract_emojis
from programa.analisis.analisis_hagstags import numero_hagstags
from programa.analisis.analisis_longitud_media_palabras import longitud_media_palabras
from programa.analisis.analisis_correccion_ortografica import palabras_correctas_e_incorrectas
from programa.analisis.analisis_palabras_acentuadas import detectar_acentos
from programa.analisis.analisis_signos_puntuacion import detect_signos_puntuacion
# from programa.analisis.sentiment_analysis import analyze_text
import language_tool_python
import pandas as pd
from datetime import datetime



tool = language_tool_python.LanguageToolPublicAPI('es')

path = 'reporting/tweets_testing.csv'

# Esta función recibe el path del archivo csv y lo abre
def ejecutar_programa(path):
    with open(path,newline='', encoding = "utf-8") as file:
        reader = csv.reader(file)
        lista_tweets = []
        for row in reader:
            if row != []:
                lista_tweets.append(row)
            else:
                # print("no se añade")
                pass
    
    lista_tweets.pop(0)

    with open("tweets_analizados/analisis_finalizado.csv",'w', newline='') as documento:
        tweets_analizados = 0
        tiempo_analisis_inicio = datetime.now()
        df_con_analisis = pd.DataFrame(columns = ['userid','id_tweet','screen_name','created_at','texto_tweet','Numero_pasados', 'Numero_presentes', 'Numero_futuros', 'Numero_condicionales','Numero_Infinitivos', 'Numero_Gerundios', 'Verbos_indicativo', 'Verbos_subjuntivo', 'Numero_determinantes', 'Determinantes_masc', 'Determinantes_fem', 'Determinantes_sing', 'Determinantes_plu', 'Determinantes_articulos', 'Determinantes_numerales', 'Determinantes_exclamativos', 'Determinantes_indefinidos', 'Determinantes_demostrativos', 'Determinantes_posesivos', 'Numero_nombres_propios', 'Numero_nombres_comunes', 'Numero_nombres', 'Nombres_singular', 'Nombres_plural', 'Nombres_masculino', 'Nombres_femenino', 'Genero_no_detectado', 'Numero_no_detectado', 'Numero_preposiciones', 'Numero_pronombres', 'Pronombres_masc', 'Pronombres_fem', 'Pronombres_sing', 'Pronombres_plu', 'Pronombres_personales', 'Pronombres_relativos', 'Pronombres_indefinidos', 'Pronombres_demostrativos', 'Pronombres_interrogativos', 'Pronombres_numerales', 'Pronombres_posesivos', 'Analisis_sentimiento', 'Numero_emojis', 'Numero_hagstags', 'Numero_webs', 'Longitud_media_palabras', 'Moda_palabras_tweet', 'Mediana_palabras_tweet', 'Numero_errores', 'Numero_tipos_de_error', 'Numero_tildes', 'Numero_signos_puntuacion','Numero_adjetivos','Adjetivos_masc','Adjetivos_fem', 'Adjetivos_sing','Adjetivos_plu','Adjetivos_comparativos','Adjetivos_numerales','Adjetivos_calificativos','Media_palabras_por_constituyente','Numero_constituyentes'])
        for tweet in lista_tweets:
            inicio_tiempo = datetime.now()
            userid = tweet[0]
            id_tweet = tweet[1]
            id_tweet = f"_{id_tweet}"
            screen_name = tweet[2]
            created_at = tweet[3]
            texto_tweet = tweet[4]
            
            info_tweet = {"userid":userid,"id_tweet":id_tweet,"screen_name":screen_name,"created_at":created_at,"texto_tweet":texto_tweet}
            
            resultado = ejecutar_analisis(info_tweet["texto_tweet"])
            info_tweet.update(resultado)
            df_con_analisis = df_con_analisis.append(info_tweet, ignore_index=True)
            # print(df_con_analisis.head())
            tweets_analizados +=1
            fin_analisis = datetime.now()
            tiempo_analisis = fin_analisis - inicio_tiempo
            print(f"""tweet analizado\n
            numero de tweets analizados: {tweets_analizados}\n
            tiempo_análisis_tweet: {tiempo_analisis}""")
        # df_con_analisis = df_con_analisis.set_index("id_tweet")
        df_con_analisis.drop_duplicates(subset="id_tweet")
        df_con_analisis = df_con_analisis.set_index("id_tweet")
        # df_con_analisis.sort_values(["userid"], axis=0, ascending=True,  inplace=True)
        fin_analisis_total = datetime.now()
        tiempo_analisis_total = fin_analisis_total - tiempo_analisis_inicio
        print(f"Todos los tweets han sido analizados en {tiempo_analisis_total}.")
        df_con_analisis.to_csv("tweets_analizados/analisis_finalizado.csv")
        print("""El resultado de tu análisis está en la carpeta tweets_analizados en un archivo llamado "analisis_finalizado.csv" """)

def ejecutar_analisis(tweet):
    diccionario_analisis = {}
    analisis_verbal = info_verbal(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_verbal}
    analisis_determinantes = info_det(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_determinantes}
    analisis_nombres = info_nombres(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_nombres}
    analisis_preposiciones = info_preposiciones(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_preposiciones}
    analisis_pronombres = info_pron(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_pronombres}
    analisis_adjetivos = info_adj(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_adjetivos}
    # sentiment_analysis = analyze_text(tweet)
    # diccionario_analisis = {**diccionario_analisis,**sentiment_analysis}
    analisis_emojis = extract_emojis(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_emojis}
    analisis_hagstag = numero_hagstags(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_hagstag}
    analisis_longitud = longitud_media_palabras(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_longitud}
    analisis_ortografico = palabras_correctas_e_incorrectas(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_ortografico}
    analisis_acentos = detectar_acentos(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_acentos}
    analisis_puntuacion = detect_signos_puntuacion(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_puntuacion}
    analisis_dependencia_sintactica = info_sintactica(tweet)
    diccionario_analisis = {**diccionario_analisis,**analisis_dependencia_sintactica}
    # print(diccionario_analisis.keys())
    return diccionario_analisis

def main():
    path = input("Introduce el path de donde se encuentras los tweets: ")
    ejecutar_programa(path)

if __name__ == "__main__":
    main()


