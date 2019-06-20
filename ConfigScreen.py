import PySimpleGUI as sg
import json
from Formatter import words_formatter

raw_properties = '''
{
  "properties": {
    "words": [["perro","noun"],["jugar", "verb"],["presidente","noun"],["hermoso","adjective"]],
    "colors": {
      "noun": [255,0,0],
      "verb": [0,255,0],
      "adjective": [73,255,219]
    },
    "wordsToShow": {
      "noun": 4,
      "verb": 2,
      "adjective": 1
    },
    "fontFamily": "comicsans",
    "fontSize": 40,
    "uppercase": false,
    "orientation": "vertical",
    "help": true,
    "typeHelp": "definiciones",
    "lookAndFeel": "verano",
    "office": "chiefoffice"
  }
}
'''

dict_properties = json.loads(raw_properties)


def save_properties(properties):
    try:
        with open('configuration/properties.json', 'w') as json_file:
            json.dump(properties, json_file)
    except:
        print('Error al guardar las propiedades')

def color_to_rgb(color):
    if color == 'rojo':
        return [255,0,0]
    elif color == 'verde':
        return [0,255,0]
    elif color == 'azul':
        return [0,0,255]
    elif color == 'violeta':
        return [255,2,169]
    elif color == 'rosado':
        return [255,112,247]
    elif color == 'naranja':
        return [255,111,43]

def show_config_screen():
    layout = [[sg.Frame(layout=[
        [sg.Combo(['comicsans', 'monospace'], size=(20, 3), key='cmb-fontfamily'), sg.InputCombo(['30', '40', '50'], size=(20, 3), key='cmb-fontsize'), sg.InputCombo(['vertical', 'horizontal'], size=(20, 3), key='cmb-orientation')]],
        title='General',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Fuente - Tamanio - Orientacion')],
        [sg.Frame(layout=[
    	[sg.InputCombo(['1','2','3','4','5','6','7'], size=(20, 3), key='cmb-q-noun'), sg.InputCombo(['1','2','3','4','5','6','7'], size=(20, 3), key='cmb-q-verb'), sg.InputCombo(['1','2','3','4','5','6','7'], size=(20, 3), key='cmb-q-adjective')]], title='Cantidad Palabras',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Sustantivos - Verbos - Adjetivos')],
    	[sg.Frame(layout=[[sg.InputCombo(['verde','azul','rojo','violeta','naranja','rosado'], size=(20, 3), key='cmb-c-noun'), sg.InputCombo(['verde','azul','rojo','violeta','naranja','rosado'], size=(20, 3), key='cmb-c-verb'), sg.InputCombo(['verde','azul','rojo','violeta','naranja','rosado'], size=(20, 3), key='cmb-c-adjective')]], title='Colores',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Sustantivos - Verbos - Adjetivos')],
        [sg.Frame(layout=[[sg.InputCombo(['oficina1', 'oficina2', 'oficina3'], size=(20, 3), key='cmb-r-office'), sg.InputCombo(['tema1','tema2','tema3'], size=(20, 3), key='cmb-r-theme')]], title='Raspberry',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Sustantivos - Verbos - Adjetivos')],
        [sg.Frame(layout=[
        [sg.Multiline(default_text='lindo feo bailar presidente',size=(45,5), key='mline-words')],
        [sg.Checkbox('Ayuda', key='select-help', change_submits=True, enable_events=True), sg.Checkbox('Mayusculas', key='select-uppercase')], [sg.Radio('Mostrar palabras', "radio-help", default=True, disabled=True, key='radio-show-words'), sg.Radio('Mostrar Definicion', "radio-help", disabled=True, key='radio-show-definitions')]], title='Palabras',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Oficina - Tema')],
        [sg.Submit('Guardar'), sg.Button('Default Settings', button_color=('white', 'green'))]]

    window = sg.Window('Configuracion', layout, auto_size_text=True, default_element_size=(40, 1))

    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        if event is 'Default Settings':
            save_properties(dict_properties)
            break
        if event is 'select-help':
            flag = values['select-help']
            if(flag):
                window.Element('radio-show-words').Update(disabled=False)
                window.Element('radio-show-definitions').Update(disabled=False)
            else:
                window.Element('radio-show-words').Update(disabled=True)
                window.Element('radio-show-definitions').Update(disabled=True)
        if event is 'Guardar':
            if(values['select-uppercase']):
                words = list(map(lambda x: x[0].upper(), words_formatter(values['mline-words'].split())))
            else:
                words = list(map(lambda x: x[0].lower(), words_formatter(values['mline-words'].split())))

            dict_properties['properties']['words'] = words_formatter(words)
            dict_properties['properties']['fontFamily'] = values['cmb-fontfamily']
            dict_properties['properties']['fontSize'] = int(values['cmb-fontsize'])
            dict_properties['properties']['orientation'] = values['cmb-orientation']
            dict_properties['properties']['wordsToShow']['noun'] = values['cmb-q-noun']
            dict_properties['properties']['wordsToShow']['verb'] = values['cmb-q-verb']
            dict_properties['properties']['wordsToShow']['adjective'] = values['cmb-q-adjective']
            dict_properties['properties']['colors']['noun'] = color_to_rgb(values['cmb-c-noun'])
            dict_properties['properties']['colors']['verb'] = color_to_rgb(values['cmb-c-verb'])
            dict_properties['properties']['colors']['adjective'] = color_to_rgb(values['cmb-c-adjective'])
            dict_properties['properties']['office'] = values['cmb-r-office']
            dict_properties['properties']['lookAndFeel'] = values['cmb-r-theme']
            if(values['select-help']):
                dict_properties['properties']['help'] = True
                if(values['radio-show-definitions']):
                    dict_properties['properties']['typeHelp'] = 'definitions'
                else:
                    dict_properties['properties']['typeHelp'] = 'words'
            else:
                dict_properties['properties']['help'] = False
            if(values['select-uppercase']):
                dict_properties['properties']['uppercase'] = True
            else:
                dict_properties['properties']['uppercase'] = False

            save_properties(dict_properties)
            break
    window.Close()
