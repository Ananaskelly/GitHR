import os
import re


class __AppGitHubKeys(object):
    @property
    def client_id(self):
        return 'e367ac8d3b8fea3451b4'

    @property
    def client_secret(self):
        return '451bd4a6a6127b76acb947696e0a43e448fe7d83'

AppGitHubKeys = __AppGitHubKeys()


# RAWGIT cofiguration don't forget cdn!!!
STATIC_URL = "https://rawgit.com/kinmanz/staticDump/master/static"

# Used only on start
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_HTML_PATH = BASE_DIR + '/static/index.html'

rx = re.compile(r'{% static (?P<path>\S+) %}')
with open(INDEX_HTML_PATH, 'r') as f:
    MainPageString = f.read()
    MainPageString = rx.sub(STATIC_URL + '\g<path>', MainPageString)

print(MainPageString)
