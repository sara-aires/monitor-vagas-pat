from sites import caraguatatuba
import os
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def enviar_telegram(mensagem):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("⚠️ Variáveis do Telegram não configuradas.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensagem
    }

    response = requests.post(url, data=payload)

    print("Telegram status:", response.status_code)
    print(response.text)


def main():
    print("🔎 Verificando vagas PAT Caraguatatuba...")

    vagas_encontradas = caragua.verificar()

    if vagas_encontradas:
        mensagem = (
            "🚨 VAGA DETECTADA!\n\n"
            f"{vagas_encontradas}"
        )
        enviar_telegram(mensagem)
    else:
        print("ℹ️ Nenhuma vaga encontrada.")


if __name__ == "__main__":
    main()
