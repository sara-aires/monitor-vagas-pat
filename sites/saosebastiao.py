import socket
print(socket.gethostbyname("www.saosebastiao.sp.gov.br"))
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
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}
    response = requests.get(URL, headers=headers, timeout=30)

    soup = BeautifulSoup(response.text, "html.parser")

    texto = remover_acentos(soup.get_text(separator=" ").lower())

    padrao = r"\bajudante\s+de\s+armador\s+de\s+ferro\b"

    if re.search(padrao, texto):
        return ["Ajudante de Armador de Ferro"]

    return []
