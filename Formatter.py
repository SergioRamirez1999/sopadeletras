from pattern.web import Wiktionary
from pattern.es import lexicon, parse
import json

def search_wiktionary(word):
    wiki = Wiktionary(language='es')
    data = wiki.search(word)
    return data

def search_pattern(word):
    return parse(word)

def exist_lexicon(word):
    if (not(word.lower() in lexicon) and not(word.upper() in lexicon) and not(word.capitalize() in lexicon)):
        return False
    return True

def get_type_wiktionary(data):
    for sect in data.sections:
        sentence = sect.title
        if 'Verbo' in sentence:
            return 'verb'
        elif 'Sustantivo' in sentence:
            return 'noun'
        elif 'Adjetivo' in sentence:
            return 'adjective'


def get_definition_wiktionary(data):
    for sect in data.sections:
        sentence = sect.title
        if 'Etimología' in sentence:
            return sect.content

def get_type_pattern(data):
    if 'NN' in data:
        return 'noun'
    elif 'JJ' in data:
        return 'adjective'
    elif 'VB' in data:
        return 'verb'
    else:
        return 'undefined'

def save_logs(path, data):
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file)
    except:
        print('Error al guardar los logs')

def words_formatter(words):
    formated_words = []
    unknown_words = []
    unknown_words_pattern = []
    for i in range(len(words)):
        word = words[i].lower()
        data = search_wiktionary(word)
        if(data):
            type = get_type_wiktionary(data)
            definition = get_definition_wiktionary(data)
            formated_words.append((words[i], type, definition))
            if(not search_pattern(words[i])):
                unknown_words_pattern.append(words[i])
        else:
            exist = exist_lexicon(words[i])
            if(exist):
                type = get_type_pattern(words[i])
                definition = 'undefined'
                formated_words.append((words[i], type, definition))
            else:
                unknown_words.append(words[i])
    if(len(unknown_words_pattern) > 0):
        data = {'patternErrors':unknown_words_pattern}
        save_logs('logs/patternerror.json', data)
    if(len(unknown_words) > 0):
        data = {'unknownWords':unknown_words}
        save_logs('logs/unknownwords.json', data)
    return formated_words
