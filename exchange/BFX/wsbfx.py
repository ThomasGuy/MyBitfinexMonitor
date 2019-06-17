"""Open bitfinex websockets with authorisation get my wallet and show balance"""
import asyncio
import wx

from . import CustomLogger
from .tickerdata import TickerData

log = CustomLogger('wallet_bfx', 'INFO')


pairs = ['LTC', 'NEO', 'XRP', 'IOT', 'ETH', 'EOS', 'BCH', 'NEO', 'OMG']
# dictionary of subscribed objects
# used to access tickDict:-  subscribed = { chan_id: 'BTC'}
mySubscribed = {}
# tickerDicy:- keys = coin, values = TickerData dataclass
tickerDict = {}
base_currency = 'USD'
myWallet = dict()
tickerDataFields = ['bid', 'bid_size', 'ask', 'ask_size', 'daily_change',
                    'daily_change_freq', 'last_price', 'volume', 'high', 'low']


def wsbfx(bfx, frame, WalletEvent, *args, **kwargs):

    @bfx.ws.on('wallet_snapshot')
    async def log_snapshot(wallets):
        for wallet in wallets:
            if wallet.type == 'exchange' and wallet.currency not in ['SPK', 'USD']:  # No small balances
                myWallet[wallet.currency] = wallet.balance
                sym = 't' + wallet.currency + base_currency
                await bfx.ws.subscribe('ticker', sym)
            elif wallet.type == 'exchange' and wallet.currency == 'USD':
                myWallet[wallet.currency] = wallet.balance
        log.info(f"myWallet:- {repr(myWallet)}")

    @bfx.ws.on('wallet_update')
    async def log_update(wallet):
        # if wallet.currency not in myWallet.keys():
        #     myWallet[wallet.currency] = wallet.balance
        #     sym = 't' + wallet.currency + base_currency
        #     await bfx.ws.subscribe('ticker', sym)
        # log.info("Wallet updates: {}".format(wallet))
        pass

    @bfx.ws.on('subscribed')
    def show_channel(sub):
        coin = sub.symbol[1:4]
        mySubscribed[sub.chan_id] = coin
        log.info(f"{coin} is subscribed  - id:- {sub.chan_id}")
        tickerDict[coin] = TickerData(symbol=sub.symbol, channel_name=sub.channel_name,
                                      chan_id=sub.chan_id, sub_id=sub.sub_id,
                                      balance=myWallet[coin])
        log.info(f"tickerDict: {tickerDict[coin]}")
        # bfx.ws._emit('on_update_tickerData', (coin))
        # if len(tickerDict) == len(myWallet) - 1:
        #     evt = WalletEvent(attr='Hello')
        #     wx.PostEvent(frame, evt)

    @bfx.ws.on('unsubscribed')
    async def log_unsubscribe(sub):
        log.info(f"unsubscribed: {sub}")
        del(tickerDict[sub.symbol[1:4]])

    @bfx.ws.on('error')
    async def log_error(msg):
        log.error("Error: {}".format(msg), exc_info=True)

    @bfx.ws.on('balance_update')
    async def log_balance(data):
        # log.info('Balance update: {}'.format(data))
        pass

    @bfx.ws.on('ticker_update')
    async def log_ticker(tkdata):
        symbol, tkupdate = tkdata
        data = dict(zip(tickerDataFields, tkupdate))
        tickerDict[symbol].update(**data)
        # log.info(f"MyWallet: {symbol} - ${tickerDict[symbol].wallet:2f}")

    # My event added to 'bfxapi.ws.GenericWebsocket.py'
    # @bfx.ws.on('on_update_tickerData')
    # async def log_tickerDict(sym):
    #     try:
    #         # tickerDict[sym].balance = myWallet[sym]
    #         log.info(f"tickerDict: {tickerDict[sym]}")
    #     except KeyError:
    #         log.error('Bollocks')
    #     else:
    #         if len(tickerDict) == len(myWallet) - 1:
    #             evt = WalletEvent(attr='Hello')
    #             wx.PostEvent(frame, evt)
