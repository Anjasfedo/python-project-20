import sys
sys.path.append('../../python-project-20')

from helpers import helpers as hh

print(hh.readJson(path="../config.json", value="GMAIL_APP_PASSWORD"))
