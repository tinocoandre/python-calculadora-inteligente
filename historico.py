import json

def salvar_historico(historico):
    with open("historico.json", "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)

def carregar_historico():
    try:
        with open("historico.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
        
    except FileNotFoundError:
        return []