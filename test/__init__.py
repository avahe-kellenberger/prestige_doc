import urllib.request

from prestige_doc.module import Module

if __name__ == "__main__":
    url = 'https://raw.githubusercontent.com/avahe-kellenberger/prestige_irc/master/prestige_irc/connection.py'
    text = urllib.request.urlopen(url).read().decode('utf-8')

    test_module = Module(text)
    for c in test_module.classes:
        print(f'class {c.name}: \n{c.doc}\n')
