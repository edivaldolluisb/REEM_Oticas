# Generated by Django 3.2.8 on 2022-02-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicas', '0007_agendamento_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='encomenda',
            name='entregue',
            field=models.BooleanField(default=False),
        ),
    ]