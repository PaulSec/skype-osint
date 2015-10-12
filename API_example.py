from SkypeOsintAPI import *

api = SkypeOSINTAPI(True)
res = api.email_to_skype_id('username@gmail.com')

if res:
    print "Username(s) found: {0}".format(res)
    for username in res:
        print api.skype_id_to_lan_ip(username)
