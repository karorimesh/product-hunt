# Generated by Django 3.0.4 on 2020-04-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newproduct', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('pubdate', models.DateTimeField()),
            ],
        ),
    ]
