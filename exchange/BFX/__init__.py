from bfxapi import Client
from bfxapi import (Order, Trade, OrderBook, Subscription, Wallet,
                    Position, FundingLoan, FundingOffer, FundingCredit)
from bfxapi.websockets.GenericWebsocket import GenericWebsocket
from bfxapi.websockets.BfxWebsocket import BfxWebsocket
from bfxapi.utils.Decimal import Decimal
from bfxapi.utils.CustomLogger import CustomLogger

from .wsbfx import tickerDict, wsbfx

NAME = 'BFX'
