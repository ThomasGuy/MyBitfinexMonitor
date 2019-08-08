from bfxapi import Client
from bfxapi import (Order, Trade, OrderBook, Subscription, Wallet,
                    Position, FundingLoan, FundingOffer, FundingCredit)

from bfxapi.websockets.generic_websocket import GenericWebsocket

from bfxapi.websockets.bfx_websocket import BfxWebsocket
from bfxapi.utils.decimal import Decimal
from bfxapi.utils.custom_logger import CustomLogger

from .wsbfx import tickerDict, wsbfx

NAME = 'BFX'
