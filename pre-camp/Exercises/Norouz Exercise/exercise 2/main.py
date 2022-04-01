from Site import Site
from Account import Account


user1 = Account("moien_karimi", "Llllll4555555", "09115480301", "moein@gmail.com")
user2 = Site("url type")
print(user2.register(user1))
print(user2.registered_users)
# the first argumant must be password. username or email can be second or third
print(user2.login(Account.log_in("Llllll4555555", "moein@gmail.com")))
print(user2.active_users)
print(user2.logout(user1))
print(user2.active_users)