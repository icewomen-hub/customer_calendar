class GUIConfig:
    
    app_title = 'Kundenkalender - Login'
    menu_topics = None
    font=('Chicago',12, 'normal')
    btn_font=('Chicago',10, 'bold')
    
    def __init__(self):
        
        # Menu - Punkte für Admin 
        self.menu_topics = {
            '☯': ['Übersicht', 'Beenden'],
            'Kalender': ['Öffnen', 'Speichern', 'Aktuell', 'Suche'],
            'Kunden': ['Öffnen', 'Speichern', 'Neu', 'Suche', 'Bearbeiten'],
            'Kurse': ['Termine', 'Trainer', 'Zeiten'],            
            'Analyse': ['Q1..Q4', 'Suche', 'Auswahl'],
            '???': ['Web', 'CHM', 'Manpage'],
        }
        
        
