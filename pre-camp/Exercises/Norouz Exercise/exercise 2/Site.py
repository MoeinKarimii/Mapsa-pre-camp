import hashlib
import Account


class Site:
    registered_users = []
    active_users = []
    def __init__(self, url):
        self.url = url
    
    @staticmethod
    def register(username, password, phone_number, email):
        for i in range(len (Site.registered_users)):
            if username in Site.registered_users[i][0]:
                raise Exception("user already registered")
        Site.registered_users.append([username, password, phone_number, email])
        return "register successful"

    @staticmethod        
    def login(acc):
        password = hashlib.sha256(acc["password"].encode('utf-8')).hexdigest()
        if "username" in acc and "password" in acc and "email" in acc:
            counter = None
            for i in range(len(Site.registered_users)):
                if acc["username"] == Site.registered_users[i][0]:
                    counter = i
                    break
            if Site.registered_users[counter][0] in Site.active_users:
                return "user already logged in"
            elif password == Site.registered_users[counter][1] and acc["email"] == Site.registered_users[counter][-1]:
                Site.active_users.append(Site.registered_users[counter][0])
                return "login successful"
            else:
                return "invalid login"
            
        elif "username" in acc and "password" in acc:
            counter = None
            for i in range(len(Site.registered_users)):
                if acc["username"] == Site.registered_users[i][0]:
                    counter = i
                    break   
            if Site.registered_users[counter][0] in Site.active_users:
                return "user already logged in"
            elif password == Site.registered_users[counter][1]:
                Site.active_users.append(Site.registered_users[counter][0])
                return "login successful"
            else:
                return "invalid login"
        elif "password" in acc and "email" in acc:
            counter = None
            for i in range(len(Site.registered_users)):
                if acc["email"] == Site.registered_users[i][-1]:
                    counter = i
                    break
            if Site.registered_users[counter][0] in Site.active_users:
                return "user already logged in"
            elif password == Site.registered_users[counter][1]:
                Site.active_users.append(Site.registered_users[counter][0])
                return "login successful"
            else:
                return "invalid login"
        else:
            return "invalid login"
    
    def logout(username):
        if username in Site.active_users:
            Site.active_users.remove(username)
            return "logout successful"
        else:
            return "user is not logged in"
