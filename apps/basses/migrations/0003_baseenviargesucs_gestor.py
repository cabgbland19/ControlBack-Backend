# Generated by Django 4.0.8 on 2022-10-20 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basses', '0002_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseenviargesucs',
            name='gestor',
            field=models.CharField(default='NINGUNO', max_length=60),
        ),
    ]
