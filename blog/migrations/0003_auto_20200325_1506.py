# Generated by Django 3.0.4 on 2020-03-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200325_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(related_name='tags', related_query_name='article', to='blog.Article'),
        ),
    ]