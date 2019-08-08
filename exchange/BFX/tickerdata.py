from dataclasses import dataclass


@dataclass
class TickerData:
    '''Keep track of ticker data for a PAIR i.e. BTCUSD'''
    chan_id: int
    channel_name: str
    symbol: str
    sub_id: int
    balance: float = 0  # number of coins
    bid: float = -0.01
    bid_size: float = -0.01
    ask: float = -0.01
    ask_size: float = -0.01
    daily_change: float = -0.01
    daily_change_freq: float = -0.01
    last_price: float = -0.01   # latest coin price
    volume: float = -0.01
    high: float = -0.01
    low: float = -0.01
    daily_pcent: float = -0.01
    wallet: float = 0   # value in $ usd

    def update(self, **args):
        """update used to continually update TickerData with
         the latest pair ticker data
        """
        for sym, data in args.items():
            setattr(self, sym, data)
        change = (self.daily_change / self.last_price) * 100
        setattr(self, 'daily_pcent', change)
        setattr(self, 'wallet', self.balance * self.last_price)

    def __getitem__(self, key):
        return getattr(self, key)
