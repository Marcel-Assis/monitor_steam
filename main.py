import requests
import sqlite3
from auth import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

# --- CONFIGURAÇÕES (Preencha com seus dados) ---
TOKEN_TELEGRAM = TELEGRAM_BOT_TOKEN
CHAT_ID = TELEGRAM_CHAT_ID

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Erro ao enviar para o Telegram: {e}")

def iniciar_db():
    conn = sqlite3.connect('promocoes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogos (
            id TEXT PRIMARY KEY,
            nome TEXT,
            link TEXT
        )
    ''')
    conn.commit()
    return conn

def buscar_jogos_gratis():
    conn = iniciar_db()
    cursor = conn.cursor()
    novos_encontrados = 0
    
    url = "https://www.cheapshark.com/api/1.0/deals?onSale=1&upperPrice=0"
    
    try:
        print("🔍 Verificando promoções na API...")
        response = requests.get(url)
        jogos = response.json()
        
        for jogo in jogos:
            # Filtro rigoroso: Preço de venda deve ser 0
            if float(jogo['salePrice']) == 0 and jogo['steamAppID']:
                id_steam = jogo['steamAppID']
                nome = jogo['title']
                link = f"https://store.steampowered.com/app/{id_steam}"
                
                cursor.execute("SELECT id FROM jogos WHERE id = ?", (id_steam,))
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO jogos VALUES (?, ?, ?)", (id_steam, nome, link))
                    mensagem = f"<b>🎮 JOGO GRÁTIS ENCONTRADO!</b>\n\n" \
                               f"🕹 <b>Nome:</b> {nome}\n" \
                               f"🔗 <b>Link:</b> <a href='{link}'>Resgatar</a>"
                    enviar_telegram(mensagem)
                    novos_encontrados += 1
        
        conn.commit()

        # --- NOVA LÓGICA DE AVISO ---
        if novos_encontrados == 0:
            print("Nenhuma novidade.")
            enviar_telegram("🔎 <b>Status do Monitor:</b> Busca concluída. Nenhuma nova promoção de R$ 0,00 encontrada no momento.")
        else:
            print(f"Sucesso! {novos_encontrados} novos jogos enviados.")
            
    except Exception as e:
        erro_msg = f"⚠️ <b>Erro no Monitor:</b> {e}"
        enviar_telegram(erro_msg)
        print(erro_msg)
    finally:
        conn.close()

if __name__ == "__main__":
    buscar_jogos_gratis()