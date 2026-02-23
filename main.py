import os
import requests
from sites import caraguatatuba, saosebastiao

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }
    requests.post(url, data=payload)

def main():
    resultados = {}

    caragua = caraguatatuba.verificar()
    sao_seb = saosebastiao.verificar()

    if caragua:
        resultados["Caraguatatuba"] = caragua

    if sao_seb:
        resultados["São Sebastião"] = sao_seb

    if resultados:
        mensagem = "🚨 VAGAS DETECTADAS!\n\n"

        for cidade, vagas in resultados.items():
            mensagem += f"📍 {cidade}:\n"
            for vaga in vagas:
                mensagem += f"- {vaga}\n"
            mensagem += "\n"

        enviar_telegram(mensagem)
    else:
        print("Nenhuma vaga encontrada.")

if __name__ == "__main__":
    main()