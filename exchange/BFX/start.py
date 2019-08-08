import asyncio
import os

# package imports
from . import wsbfx, Client, CustomLogger


log = CustomLogger('start', 'DEBUG')

api_key = os.getenv('BFX_KEY')
api_secret = os.getenv('BFX_SECRET')
loglevel = 'DEBUG'


class AuthError(Exception):
    """
    Thrown whenever there is a problem with the authentication packet
    """
    pass


def main_async():
    try:
        loop = asyncio.events.get_event_loop()
        bfx = Client(API_KEY=api_key, API_SECRET=api_secret)
        tasks = [
            asyncio.ensure_future(bfx.ws.get_task_executable()),
        ]
        loop.run_until_complete(asyncio.wait(tasks))
    except AuthError as err:
        log.error(err)
    except Exception:
        log.error('Exception ', exc_info=True)
    else:
        log.onfo('Bitfinex user is logging in...')
