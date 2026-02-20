## 🚀 SOC-in-a-Box: Honeypot SSH & Real-Time Alerting System

## 🛡️ Descrizione del Progetto
Questo progetto realizza un'infrastruttura **SOC (Security Operations Center)** completa e containerizzata. Il sistema utilizza un Honeypot interattivo (**Cowrie**) per attirare attaccanti in un ambiente isolato, analizza le loro tattiche tramite lo stack **ELK** e invia notifiche critiche in tempo reale tramite un **Bot Telegram** sviluppato in Python.

L'obiettivo è il monitoraggio proattivo delle minacce e l'analisi delle TTP (Tactics, Techniques, and Procedures) degli attaccanti senza mettere a rischio l'infrastruttura reale.

---

## 🏗️ Architettura Tecnica
Il sistema è orchestrato tramite **Docker Compose** e si divide in tre livelli:
1.  **Ingestion (La Trappola)**: Cowrie Honeypot simula un server vulnerabile sulla porta 2222.
2.  **Storage & Analysis (Il Cervello)**: Elasticsearch indicizza i log, Kibana permette la visualizzazione forense.
3.  **Alerting (La Risposta)**: Uno script Python custom monitora i log JSON e comunica con le API di Telegram.

---

## 🛠️ Step di Configurazione

1.  **Preparazione dell'ambiente Docker**

L'intero ecosistema è gestito tramite Docker Desktop e orchestrato con Docker Compose, garantendo isolamento e scalabilità.

**Docker Dashboard**

<img width="1440" height="391" alt="Docker Dashboard" src="https://github.com/user-attachments/assets/e26b672f-31e7-4a51-a1ae-f3bc6bda1721" />

**Docker Compose**

<img width="1277" height="236" alt="Docker Compose" src="https://github.com/user-attachments/assets/7fc66fee-cabf-4ccb-bdb0-8de3e6d24581" />

2.  **Sviluppo del Bot di Alerting**

**Monitoraggio Real-Time di un SOC Honeypot tramite Telegram Bot**
   
<img width="1437" height="823" alt="VS Code in Split View" src="https://github.com/user-attachments/assets/abf0c73d-24cd-4a6f-8c28-110f3f63d14d" />

---

## 🕵️ Casi d'Uso e Simulazioni (Cyber Kill Chain)

### 1. Rilevamento Intrusione (Brute Force)
Ogni tentativo di accesso viene loggato, catturando username e password utilizzati.

<img width="1433" height="801" alt="soc-honeypot-alert-system" src="https://github.com/user-attachments/assets/6fb6b538-06c6-4188-82a2-fd9e86c25690" />

### 2. Malware Staging & Detection
Rilevamento di attività post-compromissione e tentativi di esfiltrazione dati.
* *Azione:*  Tentativo di lettura /etc/shadow e download payload via wget.

* *Analisi:* Monitoraggio real-time per prevenire l'esecuzione di malware e il cracking delle password.

* *IOC:* Estrazione immediata di IP sorgente e URL malevoli per arricchire la Threat Intelligence.

<img width="1439" height="798" alt="malware-staging-and-credential-dumping-alerts" src="https://github.com/user-attachments/assets/b2d79b6d-cb94-4353-b51e-fd1208070b8d" />

### 3. SSH Intrusion Analysis: Hacker vs Honeypot
Tentativi di un Hacker di scalare i privilegi e installare malware, neutralizzati con successo da rigorose misure di hardening e isolamento di rete.

* *Reverse Shell Blocked:* Tentativo nc -e fallito.

* *Data Leak Prevented:* Furto di /etc/passwd intercettato.

* *Malware Injection Failed:* Download di botnet e miner bloccati.

* *Network Isolation:* Accesso DNS/Internet negato all'attaccante.

<img width="1440" height="760" alt="hacker-session-log" src="https://github.com/user-attachments/assets/6cd7019b-6d7a-401d-a567-25b5b0245b34" />

---

## 🚦 Classificazione della Severità (SOC Triage)

Il sistema classifica gli eventi in base al rischio potenziale:

| Severità | Tipo di Attacco | Comandi Esempio | Impatto Potenziale |
| :--- | :--- | :--- | :--- |
| 🟢 **INFO** | Ricognizione | `whoami`, `ls`, `uname` | Basso: Esplorazione dell'ambiente. |
| 🔵 **MEDIUM** | Network Scan | `nmap`, `ping -c 3` | Medio: Tentativo di movimento laterale. |
| 🟡 **HIGH** | Malware Injection | `wget`, `chmod +x` | Alto: Installazione di software malevolo. |
| 🔴 **CRITICAL** | Post-Exploitation | `bash -i` (Reverse Shell) | Critico: Controllo remoto del server. |

---

## 📊 Analisi Forense con Kibana
L'integrazione con lo stack ELK permette di trasformare i log JSON grezzi in una timeline interattiva per l'incident response.
Attraverso la dashboard personalizzata, è possibile visualizzare:
* **Attack Timeline**: Monitoraggio dei picchi di attività e distinzione tra bot e attacchi mirati.
* **Log Correlation**: Aggregazione in tempo reale di IP, credenziali e comandi in un'unica timeline.
* **Operational Visibility**: Analisi dei parametri di connessione e della durata delle sessioni per l'identificazione degli attaccanti.

---

<img width="1440" height="881" alt="Forensic Event View" src="https://github.com/user-attachments/assets/a53aaa14-0797-4bbe-853c-554a001037fb" />

## 💼 Valore per l'Azienda
* **Riduzione del MTTR (Mean Time To Respond)**: Alerting istantaneo che permette interventi immediati.
* **Threat Intelligence Locale**: Raccolta di indicatori di compromissione (IoC) specifici.
* **Automazione della Sicurezza**: Dimostrazione di competenze in Python Automation e Container Security (Docker).

Project SOC © 2026

---

## 🛠️ Come Avviare il Progetto
1. Clona la repository.
2. Configura `TOKEN` e `CHAT_ID` nel file `telegram_alert.py`.
3. Avvia l'infrastruttura:
```bash
docker-compose up -d --build

