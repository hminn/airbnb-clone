# Generated by Django 3.0.4 on 2020-03-31 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='cleanliness',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]