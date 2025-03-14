class GUIConfig:
    
    app_title = "Kundenkalender"
    menu_topics = None

    def __init__(self):
        
        # Menu - Punkte für Admin 
        self.menu_topics = {
            "Datei": ["Beenden", "Neu"],
            "Kalender": ["Öffnen", "Speichern", "Aktuell", "Suche"],
            "Kunden": ["Öffnen", "Speichern", "Neu", "Suche", "Bearbeiten"],
            "Analyse": ["Q1..Q4", "Suche", "Auswahl"],
            "Admin": ["Kunden", "Mitarbeiter", "Logs"],
            "???": ["Web", "CHM", "Manpage"],
        }
        
        
