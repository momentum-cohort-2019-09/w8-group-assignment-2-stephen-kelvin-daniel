# Generated by Django 2.2.6 on 2019-10-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='subject',
            field=models.CharField(max_length=50, null=True, verbose_name='Subject Name'),
        ),
    ]
