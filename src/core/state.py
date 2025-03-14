import datetime

class State:
    
    login_time = False
    user_name = False
    user_role = False
    
    def __init__(self):
        pass
    
    
    
    def destroy(self):
        self.login_time = False
        self.user_name = False
        self.user_role = False