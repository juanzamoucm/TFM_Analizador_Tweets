from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import (Features, KeywordsOptions,
    SentimentOptions,
    ConceptsOptions)

apikey = "1_vgQjpkcqcHvUhX80qxO4sBzpf15L_SvlSSZU56jGs6"
url = "https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/f78256d0-4d9b-4040-8c38-6ec20fcbe7b9"

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