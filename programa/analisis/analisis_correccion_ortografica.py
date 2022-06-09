import language_tool_python
from programa.preprocesamiento.preprocesamiento_limpieza import limpieza_hagstag, limpieza_emojis, limpieza_menciones, limpieza_enlaces

tool = language_tool_python.LanguageToolPublicAPI('es')
# tweet = "hola valentine está muy pesado"

def palabras_correctas_e_incorrectas(tweet):
    diccionario_respuesta = {"Numero_errores":"", "Numero_tipos_de_error":""}
    #------ regex para eliminar hagstags, urls y signos de puntuación que puedan causar errores en el corrector ortográfico
    tweet_sin_procesar = limpieza_emojis(tweet)
    tweet_sin_procesar = limpieza_menciones(tweet_sin_procesar)
    tweet_sin_procesar = limpieza_hagstag(tweet_sin_procesar)
    tweet_limpio = limpieza_enlaces(tweet_sin_procesar)
    #------ Eliminación de posible ruido 
    try:
        matches = tool.check(tweet_limpio)
        tool.close()
        tipos_de_error = {}
        for i in matches:
            tipo_error = i.ruleId
            if tipo_error not in tipos_de_error:
                tipos_de_error[tipo_error] = 0

        for i in matches:
            tipo_error = i.ruleId
            if tipo_error in tipos_de_error:
                tipos_de_error[tipo_error]+=1  
    

        tool.close() # Se cierra la llamada al terminar
        diccionario_respuesta["Numero_errores"] = len(matches)
        diccionario_respuesta["Numero_tipos_de_error"] = len(tipos_de_error)
    except:
        #Si el programa falla debido al numero de errores se pondrá como numero de errores 
        #la longitud del tweet y como tipos de errores 1
        diccionario_respuesta["Numero_errores"] = len(tweet_limpio)
        diccionario_respuesta["Numero_tipos_de_error"] = 1

    return diccionario_respuesta

# palabras_correctas_e_incorrectas(tweet)