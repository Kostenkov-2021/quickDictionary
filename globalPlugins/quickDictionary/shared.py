#shared.py
import addonHandler
addonHandler.initTranslation()

import re
import api
import ui
import braille
from speech import LangChangeCommand, speak
from textInfos import POSITION_SELECTION
from time import sleep
from tones import beep
from functools import lru_cache, wraps
import config
from .dictionary import Translator


@lru_cache(maxsize=100)
def translateWithCaching(langFrom, langInto, text):
    translator = Translator(langFrom, langInto, text)
    translator.start()
    i=0
    while translator.is_alive():
        sleep(0.1)
        if i == 10:
            beep(500, 100)
            i = 0
        i+=1
    translator.join()
    return translator

def copyToClipboard(object):
    if api.copyToClip(object):
        ui.message(_("Copied to clipboard."))
    else:
        ui.message(_("Copy faildd."))

def getSelectedText():
    obj = api.getFocusObject()
    treeInterceptor = obj.treeInterceptor
    if hasattr(treeInterceptor, 'TextInfo') and not treeInterceptor.passThrough:
        obj = treeInterceptor
    try:
        info = obj.makeTextInfo(POSITION_SELECTION)
    except (RuntimeError, NotImplementedError):
        info = None
    if not info or info.isCollapsed or not clearText(info.text):
        try:
            text = api.getClipData()
        except:
            text = ''
        if not text or not isinstance(text, str) or not clearText(text):
            # Translators: user has pressed the shortcut key for translating selected text, but no text was actually selected and clipboard is clear
            ui.message(_("There is no selected text, the clipboard is also empty, or its content is not text!"))
            return ''
        return clearText(text)
    return clearText(info.text)

def clearText(text):
    text = ''.join([s for s in text.strip() if s.isalpha() or s.isspace()])
    return ' '.join(re.split('\s+', text))

# Below toggle code came from Tyler Spivey's code, with enhancements by Joseph Lee (from Instant Translate add-on)
def finally_(func, final):
    """Calls final after func, even if it fails."""
    def wrap(f):
        @wraps(f)
        def new(*args, **kwargs):
            try:
                func(*args, **kwargs)
            finally:
                final()
        return new
    return wrap(final)

# below function is taken from Instant Translate add-on
def messageWithLangDetection(msg):
    if config.conf['speech']['autoLanguageSwitching']:
        speechSequence=[]
        speechSequence.append(LangChangeCommand(msg['lang']))
        speechSequence.append(msg['text'])
        speak(speechSequence)
        braille.handler.message(msg['text'])
    else:
        ui.message(msg['text'])
