import requests
from bs4 import BeautifulSoup
import re
import unicodedata

URL = "https://www.saosebastiao.sp.gov.br/pat/index.asp?idlink=1"

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def verificar():
    response = requests.get(URL, timeout=30)
    soup = BeautifulSoup(response.text, "html.parser")

    texto = remover_acentos(soup.get_text(separator=" ").lower())

    padrao = r"\bajudante\s+de\s+armador\s+de\s+ferro\b"

    if re.search(padrao, texto):
        return ["Ajudante de Armador de Ferro"]

    return []