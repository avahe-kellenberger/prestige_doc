from prestige_doc import parser
import urllib.request

if __name__ == "__main__":
    url = 'https://raw.githubusercontent.com/avahe-kellenberger/prestige_irc/master/prestige_irc/connection.py'
    text = urllib.request.urlopen(url).read().decode('utf-8')

    classes = parser.find_classes(text)
    for class_name in classes.keys():
        print(classes.get(class_name))
        print('\n\n')
