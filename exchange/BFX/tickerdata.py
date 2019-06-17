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


@dataclass
class Test:
    '''testing update with **kwargs'''
    name: str
    age: int
    gender: str
    date: str = 'tuesday'

    def update(self, **args):
        for sym, data in args.items():
            setattr(self, sym, data)
        setattr(self, 'age', self.age * -1)

    def __getitem__(self, key):
        return getattr(self, key)


jane = {
    'name': 'Jane',
    'age': 5,
    'gender': 'female'
}
sally = {
    'name': 'Sally',
    'age': 25,
    'date': 'wednesday'
}


if __name__ == '__main__':
    student = Test(**jane)
    print()
    print(f"My name is {student.name} and I'm {student.age} years old on {student.date}")
    student.update(**sally)
    print(f"My name is {student.name} and I'm {student.age} years old on {student.date}")
    print(student['name'])
    print(student)
