# Generated by Django 2.2 on 2019-04-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20190415_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.CharField(default='Anonymos', max_length=200),
        ),
    ]