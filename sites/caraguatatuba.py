import requests
from bs4 import BeautifulSoup
import re
import unicodedata

URL = "https://www.caraguatatuba.sp.gov.br/pmc/vagas-no-pat/"

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def verificar():
    response = requests.get(URL, timeout=30)
    soup = BeautifulSoup(response.text, "html.parser")

    texto = remover_acentos(soup.get_text(separator=" ").lower())

    padroes = [
        r"\bti\b",
        r"\binformatica\b"
    ]

    encontrados = []

    for padrao in padroes:
        if re.search(padrao, texto):
            encontrados.append(padrao.replace("\\b", ""))

    return encontrados