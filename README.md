# TicketBot (Discord Ticket System)

**Ein moderner, erweiterbarer TicketBot für Discord, inspiriert von TicketTool.**

## Features
- Ticket-Panel mit Button
- Automatische Channel-Erstellung
- Rollenbasierte Berechtigungen
- Ticket-Management (Schließen, Archivieren)
- MongoDB-Datenbank-Anbindung
- (Optional) Docker-Deployment

## Setup

1. Repository klonen
2. `.env` Datei anlegen
3. Abhängigkeiten installieren:
    ```bash
    pip install -r requirements.txt
    ```
4. Bot starten:
    ```bash
    python bot.py
    ```
5. Slash-Command `/panel_erstellen` benutzen!
