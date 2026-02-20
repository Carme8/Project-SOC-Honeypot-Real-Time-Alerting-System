import time
import json
import requests
import os


TOKEN = "7869469356:AAGIVu8Nw-nzThRZ5R2tFpYEnh0veTRSUok"
CHAT_ID = "7508713112" 

# Percorsi file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "logs", "cowrie.json")

def send_telegram_message(message):
    """Invia il messaggio formattato a Telegram."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": message, 
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"✅ Notifica inviata: {message[:40].replace(chr(10), ' ')}...")
        else:
            print(f"❌ Errore API Telegram: {response.status_code}")
    except Exception as e:
        print(f"❌ Errore connessione: {e}")

def monitor_logs():
    print(f"🚀 Sentinel SOC Alerting System Attivo...")
    print(f"📂 Monitoraggio file: {LOG_PATH}")
    
    ultimo_messaggio_inviato = ""

    if not os.path.exists(LOG_PATH):
        print(f"⚠️ ATTENZIONE: Il file {LOG_PATH} non esiste. In attesa...")
        while not os.path.exists(LOG_PATH):
            time.sleep(5)

    with open(LOG_PATH, "r") as f:
        
        f.read() 
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            
            try:
                data = json.loads(line)
                event_id = data.get("eventid")
                src_ip = data.get("src_ip", "N/A")
                
                msg = ""

                # 1. Caso: Login Riuscito
                if event_id == "cowrie.login.success":
                    username = data.get("username", "unknown")
                    password = data.get("password", "unknown")
                    msg = (f"⚠️ *ACCESSO HONEYPOT*\n"
                           f"👤 User: `{username}`\n"
                           f"🔑 Pwd: `{password}`\n"
                           f"🌐 IP: `{src_ip}`")

                # 2. Caso: Login Fallito (Brute Force)
                elif event_id == "cowrie.login.failed":
                    username = data.get("username", "unknown")
                    password = data.get("password", "unknown")
                    msg = (f"🚫 *LOGIN FALLITO*\n"
                           f"👤 User: `{username}`\n"
                           f"🔑 Pwd: `{password}`\n"
                           f"🌐 IP: `{src_ip}`")

                # 3. Caso: Comando Eseguito
                elif event_id == "cowrie.command.input":
                    comando = data.get("input", "")
                    # Ignoriamo comandi vuoti o di sistema ripetitivi se necessario
                    if comando:
                        msg = (f"⌨️ *COMANDO ESEGUITO*\n"
                               f"💻 Cmd: `{comando}`\n"
                               f"🌐 IP: `{src_ip}`")

                
                if msg and msg != ultimo_messaggio_inviato:
                    send_telegram_message(msg)
                    ultimo_messaggio_inviato = msg
                
            except Exception as e:
                # Silenzioso per righe JSON parziali o corrotte
                continue

if __name__ == "__main__":
    try:
        monitor_logs()
    except KeyboardInterrupt:
        print("\n🛑 Sistema di Alerting interrotto dall'utente.")