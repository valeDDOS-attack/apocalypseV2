# apocalypseV2
apocalypse version 2 it's seriously tool destroy website
# APOCALYPSE2V

**APOCALYPSE2V** è uno strumento avanzato di **stress test e load testing** per server HTTP/HTTPS, progettato per testare la resistenza e la capacità di risposta delle infrastrutture web in modo etico e responsabile.  
Include un'interfaccia grafica (GUI) user-friendly e un motore di test ad alte prestazioni.

---

## 🚀 Caratteristiche principali

- **Test ad alta concorrenza:** fino a migliaia di richieste concorrenti grazie ad asyncio e aiohttp.
- **Supporto HTTP/HTTPS** con gestione personalizzata dei certificati SSL.
- **Gestione payload avanzata:** specifica dimensione e tipo di dati inviati.
- **DNS load balancing** e refresh dinamico.
- **Statistiche in tempo reale** su throughput, errori, latenza.
- **Report dettagliato** a fine test.
- **Interfaccia grafica** (Tkinter) facile da usare.
- **Configurazione personalizzabile** (metodo HTTP, headers, keep-alive, ecc).

---
LEGGI ATTENTAMENTE :
OBBLIGATORIO METTERE COME IP NEL TOOL non questo: 192.168.x.x ma questo http/https://192.168.x.x CONN L'IP CHE VI SERVE
## 🛠️ Come è fatto (Architettura)

**1. Interfaccia Grafica (happyddos.py):**
- Realizzata in Python con Tkinter.
- Permette di inserire target, durata, concorrenza e payload.
- Avvia/ferma test e mostra log reali e simulati su più console.

**2. Motore di stress test (stress_core.py):**
- Utilizza asyncio e aiohttp per la massima concorrenza e velocità.
- Risolve dinamicamente il DNS, gestisce payload configurabili, headers, metodi HTTP.
- Colleziona dati statistici e presenta un report finale dettagliato.

---

## 📦 Installazione

> **Prerequisiti:**  
> - Python 3.8+  
> - pip (Python package manager)

**Installa le dipendenze:**
```bash
pip install aiohttp certifi dnspython numpy pillow
```

**Clona il repository:**
```bash
LEGGI ATTENTAMENTE :
OBBLIGATORIO METTERE COME IP NEL TOOL non questo: 192.168.x.x ma questo http/https://192.168.x.x CONN L'IP CHE VI SERVE
git clone https://github.com/valeDDOS-attack/apocalypseV2.git
cd apocalypseV2
pip install aiohttp certifi dnspython numpy pillow
python/python3 happyddos.py
```

---



- Si apre una finestra dove puoi inserire:
  - **Target URL/IP** (es. https://example.com)
  - **Durata** del test (in secondi)
  - **Concorrenza** (numero massimo di richieste in parallelo)
  - **Payload size** (OBBLIGATORIO 10kb)

- Premi “START” per avviare il test, “STOP” per fermarlo.

- I log vengono mostrati in tempo reale nelle console integrate.

- Al termine, puoi consultare i risultati completi nel terminale o nella GUI.

---

### 2. Avvio da terminale (per utenti avanzati)

```bash
python stress_core.py https://example.com -d 60 -c 2000 --payload-size 10kb --log-level INFO
```

**Opzioni principali:**
- `target` — URL o IP del server da testare.
- `-d` / `--duration` — Durata del test (secondi).
- `-c` / `--concurrency` — Numero di richieste concorrenti.
- `--payload-size` — Dimensione del payload (es. 1MB, 500KB).
- `--method` — Metodo HTTP (GET, POST, HEAD, OPTIONS).
- `--keepalive` — Mantieni connessioni attive.
- `--headers` — Headers HTTP custom (in JSON).
- `--no-ssl-verify` — Disabilita verifica certificato SSL.
- `--log-level` — Livello log (DEBUG, INFO, WARNING, ERROR).

**Esempio avanzato:**
```bash
python stress_core.py https://example.com/api/test -d 90 -c 3000 --method POST --payload-size 10kb --headers '{"Authorization":"Bearer TOKEN"}'
```

---

## 📊 Output e Monitoraggio

- Durante il test:
  - Visualizzi in tempo reale richieste al secondo, percentuale di successo, errori, latenza media.
- Al termine:
  - Ricevi un report dettagliato con breakdown codici HTTP, errori, tempi di risposta (min, max, media, P90/P95/P99).
