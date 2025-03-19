class GUIConfig:
    
    app_title = 'Kundenkalender - Login'
    menu_topics = None
    font=('Chicago',12, 'normal')
    btn_font=('Chicago',10, 'bold')
    
    design_by_role = {
        'guest': ['blue', 'white'], 
        'admin': ['orange', 'black'], 
        'member': ['lightgray', 'black'], 
        'staff': ['green', 'black']
        
    }
    
    
    def __init__(self, is_admin=True):
        
        # Menu - Punkte für Admin 
        self.menu_topics = {
            '☯': ['Übersicht', 'Beenden'],
            'Kalender': ['Öffnen', 'Speichern', 'Aktuell', 'Suche'],
            'Kunden': ['Öffnen', 'Speichern', 'Neu', 'Suche', 'Bearbeiten'],
            'Kurse': ['Termine', 'Trainer', 'Zeiten'],            
            'Analyse': ['Q1..Q4', 'Suche', 'Auswahl'],
            '???': ['Web', 'CHM', 'Manpage'],
        }

        if not is_admin:
            self.menu_topics["Mitglied"] = {
                "Meine Bucungen": ["gebucht", "storniert"],
                "Buchungen bearbeiten": ["Dokumente hinzufügen", "Kommentar hinzufügen", "ändern"],
                "Buchung stornieren": ["Buchung stornieren"],
                "Stammdaten verwalten": ["Namensänderung", "Wohnortänderung"],
                "Vertragdaten": ["Laufzeit", "Beitragsshöhe"]
            }
        
