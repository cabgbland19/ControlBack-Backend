# Generated by Django 4.0.8 on 2022-10-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]