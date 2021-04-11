from django.http import HttpResponse
from asgiref.sync import sync_to_async
import asyncio
from asyncio import sleep


@sync_to_async
def crunching_stuff():
    sleep(5)
    print("Woke up after 5 seconds!")

async def index(request):
    asyncio.create_task(crunching_stuff())
    return HttpResponse("Hello, async Django!")



