# Generated by Django 3.2.8 on 2022-02-15 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicas', '0005_auto_20220213_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='morada',
            field=models.CharField(default='Sem morada', max_length=300),
        ),
    ]
