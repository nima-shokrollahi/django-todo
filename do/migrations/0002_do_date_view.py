# Generated by Django 3.2.7 on 2021-10-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('do', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='do',
            name='date_view',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
