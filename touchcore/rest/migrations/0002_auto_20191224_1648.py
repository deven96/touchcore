# Generated by Django 3.0.1 on 2019-12-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phonenumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
