import ArabicTransliterator
import mishkal.tashkeel.tashkeel as tashkeel

transliterator = ArabicTransliterator.ALA_LC_Transliterator()

def transliterate(text, vocalize=True):
    voc = text
    if vocalize:
        vocalizer=tashkeel.TashkeelClass()
        voc = vocalizer.tashkeel(text)
    return transliterator.do(voc.strip())