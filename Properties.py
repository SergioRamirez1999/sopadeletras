import json

class Properties(object):
    __instance = None
    words = []
    colors = {}
    wordsToShow = {}
    fontFamily = ''
    fontSize = 0
    uppercase = False
    orientation = ''
    help = False
    typeHelp = ''
    lookAndFeel = ''
    office = ''

    def __new__(cls):
        if Properties.__instance is None:
            Properties.__instance = object.__new__(cls)
        return Properties.__instance

    def _load_properties(self):
        try:
            with open('configuration/properties.json') as json_file:
                data = json.load(json_file)
                properties = data['properties']
                self.words = properties['words']
                self.colors = properties['colors']
                self.wordsToShow = properties['wordsToShow']
                self.fontFamily = properties['fontFamily']
                self.fontSize = properties['fontSize']
                self.uppercase = properties['uppercase']
                self.orientation = properties['orientation']
                self.help = properties['help']
                self.typeHelp = properties['typeHelp']
                self.lookAndFeel = properties['lookAndFeel']
                self.office = properties['office']
                self.linesColor = (0,0,0)
                self.backgroundColor = (255,255,255)
                self.fontColor = (0,0,0)
                self.COLOR_RED = (255,0,0)
                self.COLOR_GREEN = (0,255,0)
                self.COLOR_BLUE = (0,0,255)
                self.COLOR_BLACK = (0,0,0)
                self.COLOR_WHITE = (255,255,255)
        except:
            print('El archivo de propiedades no se encuentra el el directorio fuente')
