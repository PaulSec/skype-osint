"""
Quick OSINT util to retrieve Skype info based on email address/Skype ID
"""
import requests
import re
import base64

from spidermonkey import Runtime
from bs4 import BeautifulSoup


class SkypeOSINTAPI(object):

    """SkypeOSINTAPI Main Handler"""

    def __init__(self, verbose=False):
        self.verbose = verbose

    def display_message(self, s):
        if self.verbose:
            print('[verbose] %s' % s)

    def email_to_skype_id(self, email):
        url = "http://www.skresolver.com/email-to-skype.php"
        self.display_message("Trying to retrieve Skype id for mail address: %s" % email)
        return self.process(url, email)

    def skype_id_to_lan_ip(self, skype_id):
        url = "http://www.skresolver.com/skype-to-lan.php"
        self.display_message("Trying to retrieve LAN IP for skype id %s" % skype_id)
        return self.process(url, skype_id)

    def process(self, url, value):
        s = requests.Session()
        req = s.get(url)
        self.display_message("Server answered: %s status code" % req.status_code)

        pattern = r'S=\'([a-zA-Z0-9\=]+)\''
        cookie_sucuri = base64.b64decode(re.findall(pattern, req.content)[0])
        cookie_sucuri = cookie_sucuri.replace('document.cookie', 'res')
        cookie_sucuri = cookie_sucuri.replace('location.reload();', '')
        # executing the javascript
        rt = Runtime()
        cx = rt.new_context()
        result = cx.execute(cookie_sucuri)
        self.display_message("Sucuri cookie: %s" % result)
        cookie_sucuri = result.split('=')

        cookies = {cookie_sucuri[0]: cookie_sucuri[1]}
        data = {'domainName': value, 'domainResolved': '', 'resolveDomain': ''}
        req = s.post(url, cookies=cookies, data=data)
        self.display_message("Server answered: %s status code" % req.status_code)

        soup = BeautifulSoup(req.content, 'html.parser')
        res = soup.find('input', attrs={'name': 'domainResolved'})['value']
        if res:
            return filter(None, res.split(', '))
        else:
            return None
