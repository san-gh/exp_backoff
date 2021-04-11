# Generated by Django 3.2 on 2021-04-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txnType', models.CharField(choices=[('C', 'credit'), ('D', 'debit')], max_length=6)),
                ('amount', models.FloatField(default=0)),
                ('status', models.CharField(choices=[('in_progress', 'In Progress'), ('success', 'Successful'), ('failed', 'Failed')], default='in_progress', max_length=20)),
            ],
        ),
    ]
