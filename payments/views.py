import asyncio
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404
import json
from .models import Transaction
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import sync_to_async
from asyncio import sleep
from .exp_backoff import transmit_with_backoff, ExpBackoff

TXN_TYPE ={
        'C' : 'credit',
        'D' : 'debit'
    }

TXN_TYPE_KEY ={
        'credit' :'C',
        'debit' : 'D'
    }
TXN_STATUS = {
    'in_progress':"In Progress",
    'success': "Successful",
    'failed': "Failed"
}

async def index(request):
    return HttpResponse("Hello, world. You're at the payments index.")



def viewTxn(request, txn_id):
    if request.method == 'GET':
        txn = get_object_or_404(Transaction, pk=txn_id)
        response = {
            "id": txn.id,
            "Txn Type" : TXN_TYPE[txn.txnType],
            "Amount ": txn.amount,
            "Status": TXN_STATUS[txn.status]
        }
        return JsonResponse(response)

    raise HttpResponseNotAllowed(['GET'])


async def postTxn(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        txnType,amount = TXN_TYPE_KEY[body["txnType"]], float(body["amount"])
        newTxn = Transaction(txnType=txnType, amount=amount)
        await newTxn.savetxn()
        
        backoff = ExpBackoff()
        asyncio.create_task(transmit_with_backoff(newTxn,backoff))
        
        return HttpResponseRedirect(redirect_to='/payments/{}'.format(newTxn.id))
    raise HttpResponseNotAllowed(['POST'])