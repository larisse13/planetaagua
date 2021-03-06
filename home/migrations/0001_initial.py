# Generated by Django 2.0.1 on 2018-01-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Título')),
                ('description', models.TextField(max_length=500, verbose_name='Descrição')),
                ('image', models.ImageField(upload_to='home/slide', verbose_name='Imagem')),
            ],
            options={
                'verbose_name_plural': 'Slides',
                'verbose_name': 'Slide',
                'ordering': ['title'],
            },
        ),
    ]
