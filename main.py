from sites import caragua

def main():
    print("🔎 Verificando vagas PAT Caraguatatuba...")

    resultado = caragua.verificar()

    if resultado:
        print("✅ Vagas encontradas e enviadas!")
    else:
        print("ℹ️ Nenhuma vaga encontrada.")

if __name__ == "__main__":
    main()
