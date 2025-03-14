class GUIConfig:
    app_title = "Kundenkalender"
    menu_topics = None

    def __init__(self):
        
        self.menu_topics = {
            "Datei": ["Öffnen", "Speichern", "Neu"],
            "Kalender": ["Aktuell", "Suche"],
            "Kunden": ["Neu", "Suche", "Bearbeiten"],
            "Analyse": ["Q1..Q4", "Suche", "Auswahl"],
            "???": ["Web", "CHM", "Manpage"],
        }
