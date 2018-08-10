# Generated by Django 2.0.7 on 2018-08-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='alarme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger', models.FloatField(verbose_name='Valor do Trigger')),
                ('tags', models.ManyToManyField(to='tags.tag')),
                ('usuarios', models.ManyToManyField(to='usuarios.usuario')),
            ],
        ),
    ]
