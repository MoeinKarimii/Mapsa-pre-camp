from Site import Site
from Account import Account


user1 = Account("moien_karimi", "Llllll4555555", "09115480301", "moeinkarimi@gmail.com")
# the first argumant must be password. username or email can be second or third
print((Account.log_in("Llllll4555555", "moeinkarimi@gmail.com")))
print(Site.active_users)
print(user1.log_out())
print(Site.active_users)



