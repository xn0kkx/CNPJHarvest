import requests
import json
import os

def fetch_cnpj_data(cnpj):
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao buscar {cnpj}: {e}")
        return None

def salvar_json(cnpj, data):
    filename = f"{cnpj}_result.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"[OK] Dados salvos em {filename}")

def main():
    if not os.path.exists("cnpjs.txt"):
        print("[ERRO] Arquivo cnpjs.txt não encontrado.")
        return

    with open("cnpjs.txt", "r") as file:
        cnpjs = [linha.strip() for linha in file if linha.strip()]

    for cnpj in cnpjs:
        print(f"[INFO] Buscando dados para CNPJ: {cnpj}")
        data = fetch_cnpj_data(cnpj)
        if data:
            salvar_json(cnpj, data)

if __name__ == "__main__":
    main()
