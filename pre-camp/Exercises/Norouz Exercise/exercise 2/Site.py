import hashlib
import Account


class Site:
    def __init__(self, url, registered_users = [], active_users = []):
        self.url = url
        self.registered_users = registered_users
        self.active_users = active_users

    def register(self, user):
        username = user.username
        for i in range(len (self.registered_users)):
            if username in self.registered_users[i][0]:
                raise Exception("user already registered")
        self.registered_users.append([username, user.password, user.phone_number, user.email])
        return "register successful"
      
    def login(self, acc):
        password = hashlib.sha256(acc["password"].encode('utf-8')).hexdigest()
        if "username" in acc and "password" in acc and "email" in acc:
            counter = None
            for i in range(len(self.registered_users)):
                if acc["username"] == self.registered_users[i][0]:
                    counter = i
                    break
            if self.registered_users[counter][0] in self.active_users:
                return "user already logged in"
            elif password == self.registered_users[counter][1] and acc["email"] == self.registered_users[counter][-1]:
                self.active_users.append(self.registered_users[counter][0])
                return "login successful"
            else:
                return "invalid login"
            
        elif "username" in acc and "password" in acc:
            counter = None
            for i in range(len(self.registered_users)):
                if acc["username"] == self.registered_users[i][0]:
                    counter = i
                    break   
            if self.registered_users[counter][0] in self.active_users:
                return "user already logged in"
            elif password == self.registered_users[counter][1]:
                self.active_users.append(self.registered_users[counter][0])
                return "login successful"
            else:
                return "invalid login"
        elif "password" in acc and "email" in acc:
            counter = None
            for i in range(len(self.registered_users)):
                if acc["email"] == self.registered_users[i][-1]:
                    counter = i
                    break
            if self.registered_users[counter][0] in self.active_users:
                return "user already logged in"
            elif password == self.registered_users[counter][1]:
                self.active_users.append(self.registered_users[counter][0])
                return "login successful"
            else:
                return "invalid login"
        else:
            return "invalid login"
    
    def logout(self, user):
        if user.username in self.active_users:
            self.active_users.remove(user.username)
            return "logout successful"
        else:
            return "user is not logged in"