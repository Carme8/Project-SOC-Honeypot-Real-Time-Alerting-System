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

### 2. Malware Staging & Execution
Il sistema rileva comandi critici per il download di payload malevoli (es. `wget`, `curl`).
> **📸 SCREENSHOT CONSIGLIATO**: Comando `wget` nel terminale e relativo alert Telegram.

### 3. Privilege Escalation & Persistence
Monitoraggio di tentativi di acquisizione privilegi root o modifica dei task pianificati (`crontab`).

---

## 🚦 Classificazione della Severità (SOC Triage)

Il sistema classifica gli eventi in base al rischio potenziale:

| Severità | Tipo di Attacco | Comandi Esempio | Impatto Potenziale |
| :--- | :--- | :--- | :--- |
| 🔵 **INFO** | Ricognizione | `whoami`, `ls`, `uname` | Basso: Esplorazione dell'ambiente. |
| 🟡 **MEDIUM** | Network Scan | `nmap`, `ping -c 3` | Medio: Tentativo di movimento laterale. |
| 🟠 **HIGH** | Malware Injection | `wget`, `chmod +x` | Alto: Installazione di software malevolo. |
| 🔴 **CRITICAL** | Post-Exploitation | `bash -i` (Reverse Shell) | Critico: Controllo remoto del server. |

---

## 📊 Analisi Forense con Kibana
Attraverso la dashboard personalizzata, è possibile visualizzare:
* **Top Attack Commands**: I comandi più digitati dagli attaccanti.
* **Authentication Trends**: Rapporto tra login falliti e riusciti.
* **Event Timeline**: Analisi temporale dei picchi di attacco.

> **📸 SCREENSHOT CONSIGLIATO**: Dashboard di Kibana con grafici a torta e serie temporali.

---

## 💼 Valore per l'Azienda
* **Riduzione del MTTR (Mean Time To Respond)**: Alerting istantaneo che permette interventi immediati.
* **Threat Intelligence Locale**: Raccolta di indicatori di compromissione (IoC) specifici.
* **Automazione della Sicurezza**: Dimostrazione di competenze in Python Automation e Container Security (Docker).

---

## 🛠️ Come Avviare il Progetto
1. Clona la repository.
2. Configura `TOKEN` e `CHAT_ID` nel file `telegram_alert.py`.
3. Avvia l'infrastruttura:
```bash
docker-compose up -d --build
