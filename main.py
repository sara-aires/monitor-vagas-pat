import requests
from bs4 import BeautifulSoup
import re
import os

URL = "https://www.caraguatatuba.sp.gov.br/pmc/vagas-no-pat/"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_telegram(mensagem):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Erro: TELEGRAM_TOKEN ou CHAT_ID não definidos.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }

    try:
        r = requests.post(url, data=payload, timeout=30)
        print("Telegram status:", r.status_code)
        print(r.text)
    except Exception as e:
        print("Erro ao enviar mensagem:", e)

def verificar_vagas():
    try:
        response = requests.get(URL, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print("Erro ao acessar o site:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Idealmente você pode restringir para uma div específica se souber a classe
    texto = soup.get_text(separator=" ")

    # Regex robusta para TI (TI, T.I, T I, T.I.)
    encontrou_ti = re.search(r"\bT\.?\s?I\.?\b", texto, re.IGNORECASE)
    encontrou_info = re.search(r"\binformática\b", texto, re.IGNORECASE)

    palavras_encontradas = []

    if encontrou_ti:
        palavras_encontradas.append("TI")

    if encontrou_info:
        palavras_encontradas.append("Informática")

    if palavras_encontradas:
        mensagem = (
            "🚨 VAGA DETECTADA!\n\n"
            "Palavras encontradas:\n"
            + "\n".join(palavras_encontradas)
            + f"\n\nLink: {URL}"
        )
        enviar_telegram(mensagem)
    else:
        print("Nenhuma vaga relevante encontrada.")

if __name__ == "__main__":
    verificar_vagas()
