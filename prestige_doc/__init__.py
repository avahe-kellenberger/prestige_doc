from prestige_doc import parser
import urllib.request

if __name__ == "__main__":
    url = 'https://raw.githubusercontent.com/avahe-kellenberger/prestige_irc/master/prestige_irc/connection.py'
    text = urllib.request.urlopen(url).read().decode('utf-8')

    class_docs = parser.map_class_docs(text)
    print(class_docs)
