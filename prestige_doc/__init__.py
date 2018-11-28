from prestige_doc import parser
import urllib.request

if __name__ == "__main__":
    url = 'https://raw.githubusercontent.com/avahe-kellenberger/prestige_irc/master/prestige_irc/connection.py'
    text = urllib.request.urlopen(url).read().decode('utf-8')

    class_names = parser.find_class_names(text)

    for class_name in class_names:
        doc = parser.find_class_doc(text, class_name)
        if doc:
            print(f'class {class_name}: \n\n{doc}\n\n')
        else:
            print(f'No documentation for class \'{class_name}\'')
