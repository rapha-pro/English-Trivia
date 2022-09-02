# Generated by Django 3.1.5 on 2022-03-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0003_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description_text',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='topic',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]