Python Skype OSINT util
=======

This tool allows you to retrieve the Skype ID from an e-mail address but also the LAN IP from the Skype ID. 
More to come in the next few days. Feel free if you also want to contribute


Installation
=======

Install [Spider Monkey](https://github.com/davisp/python-spidermonkey.git), then: 

Clone the repo: 

```
git clone git@github.com:PaulSec/skype-osint.git
```

Then checkout the ```API_example.py``` file: 

```python
from SkypeOsintAPI import *

api = SkypeOSINTAPI(True)
res = api.email_to_skype_id('username@gmail.com')

if res:
    print "Username(s) found: {0}".format(res)
    for username in res:
        print api.skype_id_to_lan_ip(username)
```

Contributing
=======

Feel free if you find any bug or want to add any other feature. Glad if you want to contribute to this project. 
You can also ping me on Twitter [@PaulWebSec](https://twitter.com/PaulWebSec)