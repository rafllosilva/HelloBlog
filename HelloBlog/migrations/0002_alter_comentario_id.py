# Generated by Django 5.0.1 on 2024-02-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelloBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]