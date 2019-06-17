import asyncio
import os
from wxasync import WxAsyncApp
# package imports
from .BFX import wsbfx, Client
from .wx_gui import WalletFrame, WalletEvent


api_key = os.getenv('BFX_KEY')
api_secret = os.getenv('BFX_SECRET')


def main_async():
    loop = asyncio.events.get_event_loop()
    bfx = Client(API_KEY=api_key, API_SECRET=api_secret, loop=loop)
    app = WxAsyncApp(loop=loop)
    frame = WalletFrame()
    frame.Show()
    app.SetTopWindow(frame)
    tasks = [
        asyncio.ensure_future(bfx.ws.get_task_executable()),
        asyncio.ensure_future(app.MainLoop()),
    ]
    wsbfx(bfx, frame, WalletEvent)
    loop.run_until_complete(asyncio.wait(tasks))
