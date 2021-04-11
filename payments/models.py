from django.db import models
from asgiref.sync import sync_to_async


class Transaction(models.Model):
    txnType = models.CharField(max_length=6, choices=[('C',"credit"),('D',"debit")])
    amount = models.FloatField(default=0)
    status = models.CharField(max_length=20, default='in_progress', choices=[
        ('in_progress',"In Progress"),
        ('success',"Successful"),
        ('failed', "Failed")])

    @sync_to_async
    def updateStatus(self, status):
        self.status = status
        self.save() 

    @sync_to_async
    def savetxn(self):
        self.save()

    def __str__(self):
        return self.txnType +": "+ str(self.amount)
