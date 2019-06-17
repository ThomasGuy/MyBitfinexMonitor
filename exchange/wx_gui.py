"""Bitfinex Wallet GUI"""
import wx
import asyncio
import logging
from wxasync import StartCoroutine

from .BFX import CustomLogger, tickerDict

from wx.lib.newevent import NewEvent
# define custom event
WalletEvent, EVT_WALLET = NewEvent()
# SomeNewEventAsync, EVT_SOME_NEW_EVENT_ASYNC = wx.lib.newevent.NewEvent()

log = CustomLogger('wx_gui')


class WalletFrame(wx.Frame):
    """Ticker GUI"""

    def __init__(self, parent=None):
        super().__init__(parent, title="Bitfinex Wallet")
        self.fSizer = wx.BoxSizer(wx.VERTICAL)
        panel = MyPanel(self)
        self.fSizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(self.fSizer)
        self.Fit()
        self.Show()


class MyPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.frame = parent
        self.Bind(EVT_WALLET, self.vboxHandler, id=wx.ID_ANY)
        self.myEdits = dict()

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)

    def vboxHandler(self, event):
        attr = event.attr
        # tickerDict = event.data
        print(event.attr)
        for key in tickerDict.keys():
            self.myEdits[key] = wx.StaticText(self.panel, style=wx.ALIGN_LEFT | wx.ST_NO_AUTORESIZE)
        self.mainSizer.AddStretchSpacer(1)
        for edit in self.myEdits.values():
            self.mainSizer.Add(edit, 1, wx.EXPAND | wx.ALL)
        self.Layout()
        StartCoroutine(self.update_ticker(), self)

    async def update_ticker(self):
        """asyncronously run forever"""
        while True:
            await asyncio.sleep(5)
            for pair, edit in self.myEdits.items():
                edit.SetLabelMarkup(self.myFormat(f'{pair}_title', f'{pair}'))

    @staticmethod
    def myFormat(title, pair):
        """formatter for TestFrame"""
        try:
            ticker = tickerDict[pair]
        except KeyError as err:
            log.error(f"TickerData KeyError in Gui formatter {err.args}")
        else:
            if ticker.daily_change < 0:
                col = 'red'
            else:
                col = 'green'
            text2 = "{:<20s}$ {:<12.4f}   ask: $ {:<12.2f}   daily: <span foreground='{}'>{:>5.1f}%</span>". \
                    format(title, ticker.last_price, ticker.ask, col, ticker.daily_pcent)
            return text2
        return 'Boo who'
