import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_HTML_PATH = BASE_DIR + '/static/index.html'
STATIC_URL = "https://rawgit.com/kinmanz/staticDump/master/static"


AppGitHubKeys = {
    'client_id': 'e367ac8d3b8fea3451b4',
    'client_secret': '451bd4a6a6127b76acb947696e0a43e448fe7d83'
}


rx = re.compile(r'{% static (?P<path>\S+) %}')
with open(INDEX_HTML_PATH, 'r') as f:
    MainPageString = f.read()
    MainPageString = rx.sub(STATIC_URL + '\g<path>', MainPageString)

print(MainPageString)
