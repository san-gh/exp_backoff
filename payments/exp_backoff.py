import random
import time
from asyncio import sleep
from asgiref.sync import sync_to_async

SLOT_TIME = 2 #seconds
MAX_ATTEMPTS = 4

async def mock_server(attempt):
    if (attempt) > 3:
       return 's'
    return 'f'

class ExpBackoff:
    def __init__(self, slot_time = SLOT_TIME):
        self.__slot_time = slot_time
        self.__attempt = 1

    def get_wait_time(self):
        k = self.__attempt -1 
        k_set = range(0, 2**k)
        print(list(k_set))
        return random.choice(k_set) * self.__slot_time

    def inc_attempt(self):
        self.__attempt += 1

    def get_attempt(self):
        return self.__attempt


async def transmit_with_backoff(db_obj, backoff, max_attempts=MAX_ATTEMPTS, gatewayserver=mock_server):
    print(max_attempts)
    while backoff.get_attempt() <= max_attempts:
        wait_time = backoff.get_wait_time()
        print("\n Attempt {} at transmitting in {} secs".format(backoff.get_attempt(), wait_time))
        await sleep(wait_time)
        reply = await gatewayserver(backoff.get_attempt())

        if (reply=="s"):
            print("msg successfully transmitted") 
            await db_obj.updateStatus('success')
            return
        else:
            print("msg transmission failed")
            backoff.inc_attempt()
            
    
    print("msg transmission failed, No more retries")
    await db_obj.updateStatus('failed')



