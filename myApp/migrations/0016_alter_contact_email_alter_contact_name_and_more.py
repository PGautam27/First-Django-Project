# Generated by Django 4.0.4 on 2022-05-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0015_alter_contact_email_alter_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='gautam@gmail.com', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='gautam', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=1234567895, max_length=10, null=True),
        ),
    ]
