# Generated by Django 3.1 on 2021-04-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jini',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MSN', models.CharField(max_length=20, verbose_name='電話番号')),
                ('model', models.CharField(max_length=30, verbose_name='機種')),
                ('subtotal', models.IntegerField(verbose_name='小計')),
                ('call', models.CharField(max_length=10, verbose_name='通話')),
                ('GB', models.IntegerField(verbose_name='ネット')),
                ('hs', models.CharField(max_length=10, verbose_name='半サポ')),
                ('suport', models.CharField(max_length=500, verbose_name='割引')),
            ],
        ),
        migrations.DeleteModel(
            name='Apo',
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]