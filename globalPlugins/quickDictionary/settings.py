#settings.py
import addonHandler
addonHandler.initTranslation()

import gui
import wx
import config
from . import _addonName, _addonSummary
from .languages import langs

TOKEN = 'dict.1.1.20160512T220906Z.4a4ee160a921aa01.a74981e0761f48a1309d4f903e540f1f3288f1a3'


class QuickDictionarySettingsPanel(gui.SettingsPanel):
    # Translators: name of the settings dialog.
    title = _addonSummary

    def __init__(self, parent):
        super(QuickDictionarySettingsPanel, self).__init__(parent)

    def makeSettings(self, sizer):
        # Translators: Help message for a dialog.
        helpLabel = wx.StaticText(self, label=_("Select translation source and target language:"))
        helpLabel.Wrap(self.GetSize()[0])
        sizer.Add(helpLabel)
        fromSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: A setting in addon settings dialog.
        fromLabel = wx.StaticText(self, label=_("Source language:"))
        fromSizer.Add(fromLabel)
        self._fromChoice = wx.Choice(self, choices=[])
        fromSizer.Add(self._fromChoice)
        intoSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: A setting in addon settings dialog.
        intoLabel = wx.StaticText(self, label=_("Target language:"))
        intoSizer.Add(intoLabel)
        self._intoChoice = wx.Choice(self, choices=[])
        intoSizer.Add(self._intoChoice)
        self.widgetMaker(self._fromChoice, sorted(langs.fromList(), key=lambda l: l.name))
        self._fromChoice.Bind(wx.EVT_CHOICE, self.onSelectFrom)
        self.widgetMaker(self._intoChoice, langs.intoList(config.conf[_addonName]['from']))
        sizer.Add(fromSizer)
        sizer.Add(intoSizer)
        langFrom = self._fromChoice.FindString(langs[config.conf[_addonName]['from']].name)
        langTo = self._intoChoice.FindString(langs[config.conf[_addonName]['into']].name)
        self._fromChoice.Select(langFrom)
        self._intoChoice.Select(langTo)
        # Translators: A setting in addon settings dialog.
        self._copyToClipboardChk = wx.CheckBox(self, label=_("Copy translation result to clipboard"))
        self._copyToClipboardChk.SetValue(config.conf[_addonName]['copytoclip'])
        sizer.Add(self._copyToClipboardChk)
        # Translators: A setting in addon settings dialog.
        self._autoSwapChk = wx.CheckBox(self, label=_("Auto-swap languages"))
        self._autoSwapChk.SetValue(config.conf[_addonName]['autoswap'])
        sizer.Add(self._autoSwapChk)

        serverSizer = wx.BoxSizer(wx.VERTICAL)
        # Translators: A setting in addon settings dialog.
        serverLabel = wx.StaticText(self, label=_("Server settings:"))
        serverSizer.Add(serverLabel)
        # Translators: A setting in addon settings dialog.
        self._useMirrorChk = wx.CheckBox(self, label=_("Use mirror server"))
        self._useMirrorChk.SetValue(config.conf[_addonName]['mirror'])
        serverSizer.Add(self._useMirrorChk)
        tokenSizer = wx.BoxSizer(wx.VERTICAL)
        # Translators: A setting in addon settings dialog.
        tokenLabel = wx.StaticText(self, label=_("Dictionary Access Token:"))
        tokenSizer.Add(tokenLabel)
        self._tokenInput = wx.TextCtrl(self, style=wx.TE_LEFT)
        tokenSizer.Add(self._tokenInput)
        url = 'https://yandex.com/dev/dictionary/keys/get/'
        # Translators: A setting in addon settings dialog.
        self._linkHref = wx.adv.HyperlinkCtrl(self, -1, label=_("Register your own access token"), url=url, style=wx.adv.HL_CONTEXTMENU | wx.adv.HL_DEFAULT_STYLE | wx.adv.HL_ALIGN_RIGHT)
        self._linkHref.Update()
        self._tokenInput.SetValue(config.conf[_addonName]['token'])
        tokenSizer.Add(self._linkHref)
        serverSizer.Add(tokenSizer)
        sizer.Add(serverSizer)

    def widgetMaker(self, widget, languages):
        for lang in languages:
            widget.Append(lang.name, lang)

    def onSelectFrom(self, event):
        fromLang = self._fromChoice.GetClientData(self._fromChoice.GetSelection()).code
        self._intoChoice.Clear()
        self.widgetMaker(self._intoChoice, sorted(langs.intoList(fromLang), key=lambda l: l.name))

    def postInit(self):
        self._fromChoice.SetFocus()

    def onSave(self):
        """Update Configuration"""
        fromLang = self._fromChoice.GetClientData(self._fromChoice.GetSelection()).code
        intoLang = self._intoChoice.GetClientData(self._intoChoice.GetSelection()).code
        config.conf[_addonName]['from'] = fromLang
        config.conf[_addonName]['into'] = intoLang
        config.conf[_addonName]['copytoclip'] = self._copyToClipboardChk.GetValue()
        config.conf[_addonName]['autoswap'] = self._autoSwapChk.GetValue()
        config.conf[_addonName]['mirror'] = self._useMirrorChk.GetValue()
        config.conf[_addonName]['token'] = self._tokenInput.GetValue()
