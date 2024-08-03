
from typing import Dict
from googletrans import Translator

def open_text():
    file = open('core/text.txt', 'r', encoding='utf-8')
    text = file.read()
    file.close()
    data = {'data':text}
    return data

def trans(to_lang):
    if to_lang == 'en':
        file = open('core/text.txt', 'r', encoding='utf-8')
        text_ru = file.read()
        file.close()
        translator= Translator()
        translation = translator.translate(text_ru, dest='en')
        text_en = translation.text
        data = {'data':text_en}
        return data
    if to_lang == 'de':
        file = open('core/text.txt', 'r', encoding='utf-8')
        text_ru = file.read()
        file.close()
        translator= Translator()
        translation = translator.translate(text_ru, dest='de')
        text_de = translation.text
        data = {'data':text_de}
        return data
    if to_lang == 'fr':
        file = open('core/text.txt', 'r', encoding='utf-8')
        text_ru = file.read()
        file.close()
        translator= Translator()
        translation = translator.translate(text_ru, dest='fr')
        text_fr = translation.text
        data = {'data':text_fr}
        return data
    
def day_week(day)->str:
    week = {
        'mondey':'green',
        'tuesday':'color',
        'wednesday':'color',
        'thursday':'color',
        'friday':'color',
        'saturday':'color',
        'sunday':'color'
    }
    
    
    data = week[day]
    return data


