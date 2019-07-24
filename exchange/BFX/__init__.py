from BfxApi.bfxapi import Client
from BfxApi.bfxapi import (Order, Trade, OrderBook, Subscription, Wallet,
                           Position, FundingLoan, FundingOffer, FundingCredit)
from BfxApi.bfxapi.websockets.GenericWebsocket import GenericWebsocket
from BfxApi.bfxapi.websockets.BfxWebsocket import BfxWebsocket
from BfxApi.bfxapi.utils.Decimal import Decimal
from BfxApi.bfxapi.utils.CustomLogger import CustomLogger

from .wsbfx import tickerDict, wsbfx

NAME = 'BFX'
