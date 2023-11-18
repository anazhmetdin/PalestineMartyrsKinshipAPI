import ArabicTransliterator
import mishkal.tashkeel.tashkeel as tashkeel
import re

transliterator = ArabicTransliterator.ALA_LC_Transliterator()

def transliterate(text, vocalize=True):
    voc = text
    if vocalize:
        vocalizer=tashkeel.TashkeelClass()
        voc = vocalizer.tashkeel(text)
    return transliterator.do(voc.strip())

def romanize(name):
    validate_characters(name)    
    return transliterate(name).title()

def validate_characters(name):
    pattern = re.compile(
        r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF\U00010E60-\U00010E7F\U0001EE00-\U0001EEFF0-9\s()\[\]{}<>]'
    )

    if not pattern.match(name):
        raise Exception('Name contains invalid characters')