from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import (Features, KeywordsOptions,
    SentimentOptions,
    ConceptsOptions)

apikey = "write_your_apikey_here"
url = "write_the_url_here"

def analyze_text(tweet):
    diccionario_respuesta = {"Analisis_sentimiento":""}
    authenticator = IAMAuthenticator(apikey)
    nlu = NaturalLanguageUnderstandingV1(version="2020-08-01", authenticator=authenticator)
    nlu.set_service_url(url)
    analisis_sentimiento = nlu.analyze(
        text=tweet,
        features=Features(
            sentiment=SentimentOptions(),
            keywords=KeywordsOptions(sentiment=True, emotion=True),
            concepts=ConceptsOptions(),
        ),
    ).get_result()

    etiqueta_tweet = analisis_sentimiento["sentiment"]["document"]["label"]
    diccionario_respuesta["Analisis_sentimiento"] = etiqueta_tweet

    return diccionario_respuesta