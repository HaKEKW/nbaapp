# Generated by Django 4.1.7 on 2023-03-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_shop', '0002_alter_good_description_alter_good_good_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good',
            options={'ordering': ['category']},
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
