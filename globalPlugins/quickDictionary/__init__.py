﻿#__init__.py
# A part of NonVisual Desktop Access (NVDA)
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Copyright (C) 2020 Olexandr Gryshchenko <grisov.dev@mailnull.com>

import addonHandler
addonHandler.initTranslation()

import os
_addonDir = os.path.join(os.path.dirname(__file__), "..", "..")
if isinstance(_addonDir, bytes):
    _addonDir = _addonDir.decode("mbcs")
_curAddon = addonHandler.Addon(_addonDir)
_addonName = _curAddon.manifest['name']
_addonSummary = _curAddon.manifest['summary']

import globalPluginHandler
from scriptHandler import script, getLastScriptRepeatCount
import api, ui, config
import gui, wx
from time import sleep
from tones import beep
from threading import Thread
from .dictionary import Translator
from .shared import copyToClipboard, getSelectedText
from .languages import langs
from .settings import QuickDictionarySettingsPanel, TOKEN


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = str(_addonSummary)

    def __init__(self, *args, **kwargs):
        super(GlobalPlugin, self).__init__(*args, **kwargs)
        confspec = {
            "from": "string(default=%s)" % langs.defaultFrom,
            "into": "string(default=%s)" % langs.defaultInto,
            "autoswap": "boolean(default=true)",
            "copytoclip": "boolean(default=true)",
            "token": "string(default=%s)" % TOKEN,
            "mirror": "boolean(default=false)"
        }
        config.conf.spec[_addonName] = confspec
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(QuickDictionarySettingsPanel)

    @property
    def source(self):
        return config.conf[_addonName]['from']

    @source.setter
    def source(self, lang):
        config.conf[_addonName]['from'] = lang

    @property
    def target(self):
        return config.conf[_addonName]['into']

    @target.setter
    def target(self, lang):
        config.conf[_addonName]['into'] = lang

    @property
    def isCopyToClipboard(self):
        return config.conf[_addonName]['copytoclip']

    @property
    def isAutoSwap(self):
        return config.conf[_addonName]['autoswap']

    def terminate(self):
        try:
            gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(QuickDictionarySettingsPanel)
        except IndexError:
            pass

    def showSettings(self):
        wx.CallAfter(gui.mainFrame._popupSettingsDialog, gui.settingsDialogs.NVDASettingsDialog, QuickDictionarySettingsPanel)

    @script(description='%s: %s' % (_addonSummary, _("Announces the translation of the current selected word or phrase, press twice to copy to clipboard")))
    def script_translateAnnounce(self, gesture):
        text = getSelectedText()
        if not text: return
        if getLastScriptRepeatCount() == 0:
            Thread(target=self.translate, args=[text, False, False]).start()
        elif getLastScriptRepeatCount() >= 1:
            Thread(target=self.translate, args=[text, False, True]).start()

    @script(description='%s: %s' % (_addonSummary, _("Displays translation results in a window, press twice to copy to clipboard")))
    def script_translateBox(self, gesture):
        text = getSelectedText()
        if not text: return
        if getLastScriptRepeatCount() == 0:
            Thread(target=self.translate, args=[text, True, False]).start()
        elif getLastScriptRepeatCount() >= 1:
            Thread(target=self.translate, args=[text, False, True]).start()

    @script(description='%s: %s' % (_addonSummary, _("Change the order of the selected languages for translation, press twice to select other languages")))
    def script_swapLanguages(self, gesture):
        if getLastScriptRepeatCount() == 0:
            if langs.isAvailable(self.target, self.source):
                self.source, self.target = self.target, self.source
                ui.message('%s-%s' % (langs[self.source].name, langs[self.target].name))
            else:
                ui.message(_('Swap languages is not available for this pair') + ': %s - %s' % (langs[self.source].name, langs[self.target].name))
        elif getLastScriptRepeatCount() >= 1:
            self.showSettings()

    def translate(self, text, isHtml=False, copyToClip=False):
        pairs = [(self.source, self.target)]
        if self.isAutoSwap:
            pairs.append((self.target, self.source))
        for lFrom, lInto in pairs:
            translator = Translator(lFrom, lInto, text)
            translator.start()
            i=0
            while translator.is_alive():
                sleep(0.1)
                if i == 10:
                    beep(500, 100)
                    i = 0
                i+=1
            translator.join()
            if translator.plaintext:
                break
        else:
            if not translator.plaintext:
                ui.message(_('No results'))
                return
        if isHtml:
            ui.browseableMessage(translator.html, title='%s-%s' % (langs[translator.langFrom].name, langs[translator.langTo].name), isHtml=isHtml)
        else:
            ui.message('%s-%s' % (langs[translator.langFrom].name, langs[translator.langTo].name))
            ui.message(translator.plaintext)
        if copyToClip or self.isCopyToClipboard:
            copyToClipboard(translator.plaintext)

    __gestures = {
        "kb:NVDA+w": "translateAnnounce",
        "kb:NVDA+shift+w": "translateBox",
        "kb:NVDA+control+w": "swapLanguages"
    }
