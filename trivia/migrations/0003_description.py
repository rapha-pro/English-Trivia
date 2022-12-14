# Generated by Django 3.1.5 on 2022-03-11 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_auto_20220228_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_text', models.CharField(max_length=30)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.quiz')),
            ],
        ),
    ]
