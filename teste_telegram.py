import requests

TOKEN = "8307965646:AAHr97JLA3ddMsbj5GruyCC9bGALtaE_2Ds"
CHAT_ID = "6869059801"

def testar():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": "Teste de conexão!"}
    
    try:
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Resposta do Telegram: {response.text}")
        
        if response.status_code == 200:
            print("✅ Sucesso! Verifique seu Telegram.")
        else:
            print("❌ Erro! Verifique se o Token e o Chat ID estão corretos.")
            
    except Exception as e:
        print(f"Erro de rede: {e}")

testar()