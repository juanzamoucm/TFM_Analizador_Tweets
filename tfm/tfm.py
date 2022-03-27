import csv
from programa.preprocesamiento.preprocesamiento_limpieza import *
from programa.analisis.analisis_verbal import info_verbal
from programa.analisis.analisis_pronombres import info_pron
from programa.analisis.analisis_determinantes import info_det
from programa.analisis.analisis_nombres import info_nombres
from programa.analisis.analisis_preposiciones import info_preposiciones
from programa.analisis.analisis_emoticonos import extract_emojis
from programa.analisis.analisis_hagstags import numero_hagstags
from programa.analisis.analisis_longitud_media_palabras import longitud_media_palabras
from programa.analisis.analisis_correccion_ortografica import palabras_correctas_e_incorrectas
from programa.analisis.analisis_palabras_acentuadas import detectar_acentos
from programa.analisis.analisis_signos_puntuacion import detect_signos_puntuacion
from programa.analisis.sentiment_analysis import analyze_text
import language_tool_python
tool = language_tool_python.LanguageToolPublicAPI('es')

tweet = "Saque de esquina #SegundaRFEF #sportingdegijon #futbol #fotografiadeportiva #foto #fotografia #fotografo #canon #canonespaña #blancoynegro #salamanca #AlexLorrys en Estadio Helmántico https://t.co/wuffBZNJgv"


path = 'corpus/1a_muestra_tweets.csv'

# Esta función recibe el path del archivo csv y lo abre
def ejecutar_programa(path):
    with open(path,newline='') as file:
        reader = csv.reader(file)
        lista_tweets = []
        for row in reader:
            lista_tweets.append(row)
    
    lista_tweets.pop(0)
    # lista_tweets = lista_tweets[96]

    with open("carpeta_analisis/analisis_realizado.csv",'w', newline='') as documento:
        campos = ['autor_tweet','id_tweet','texto_tweet','Numero_pasados', 'Numero_presentes', 'Numero_futuros', 'Numero_Infinitivos', 'Numero_Gerundios', 'Verbos_indicativo', 'Verbos_subjuntivo', 'Numero_determinantes', 'Determinantes_masc', 'Determinantes_fem', 'Determinantes_sing', 'Determinantes_plu', 'Determinantes_articulos', 'Determinantes_numerales', 'Determinantes_exclamativos', 'Determinantes_indefinidos', 'Determinantes_demostrativos', 'Determinantes_posesivos', 'Numero_nombres_propios', 'Numero_nombres_comunes', 'Numero_nombres', 'Nombres_singular', 'Nombres_plural', 'Nombres_masculino', 'Nombres_femenino', 'Genero_no_detectado', 'Numero_no_detectado', 'Numero_preposiciones', 'Numero_pronombres', 'Pronombres_masc', 'Pronombres_fem', 'Pronombres_sing', 'Pronombres_plu', 'Pronombres_personales', 'Pronombres_relativos', 'Pronombres_indefinidos', 'Pronombres_demostrativos', 'Pronombres_interrogativos', 'Pronombres_numerales', 'Pronombres_posesivos', 'Analisis_sentimiento', 'Numero_emojis', 'Numero_hagstags', 'Numero_webs', 'Longitud_media_palabras', 'Moda_palabras_tweet', 'Mediana_palabras_tweet', 'Numero_errores', 'Numero_tipos_de_error', 'Numero_tildes', 'Numero_signos_puntuacion']
        writer = csv.DictWriter(documento, fieldnames=campos)
        writer.writeheader()
        for tweet in lista_tweets:
            autor_tweet = tweet[0]
            id_tweet = tweet[1]
            id_tweet = f"_{id_tweet}"
            texto_tweet = tweet[2]
            info_tweet = {"id_tweet":id_tweet,"autor_tweet":autor_tweet,"texto_tweet":texto_tweet}
            resultado = ejecutar_analisis(info_tweet["texto_tweet"])
            info_tweet = {**info_tweet,**resultado}
            writer.writerow(info_tweet)

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
    # print(diccionario_analisis.keys())
    return diccionario_analisis
 

ejecutar_programa(path)