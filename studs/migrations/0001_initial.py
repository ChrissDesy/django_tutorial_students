# Generated by Django 2.1.1 on 2019-07-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=8)),
                ('saved_date', models.DateTimeField(verbose_name='date added')),
            ],
        ),
    ]
