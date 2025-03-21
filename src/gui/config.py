class GUIConfig:
    
    app_title = 'Kundenkalender'
    menu_topics = None
    font=('Chicago',12, 'normal')
    btn_font=('Chicago',10, 'bold')
    
    design_by_role = {
        'guest': ['blue', 'white'], 
        'admin': ['orange', 'black'], 
        'member': ['lightgray', 'black'], 
        'staff': ['green', 'black']
        
    }
    
    
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
        
        self.menu_actions = {
            '☯': ['Übersicht', 'Beenden'],
            'Kalender': ['Öffnen', 'Speichern', 'Aktuell', 'Suche'],
            'Kunden': ['Öffnen', 'Speichern', 'Neu', 'Suche', 'Bearbeiten'],
            'Kurse': ['Termine', 'Trainer', 'Zeiten'],            
            'Analyse': ['Q1..Q4', 'Suche', 'Auswahl'],
            '???': ['Web', 'CHM', 'Manpage'],
        }
        
        
