# Generated by Django 4.1.5 on 2023-01-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='picture',
            name='tags',
        ),
        migrations.AddField(
            model_name='picture',
            name='tags',
            field=models.ManyToManyField(blank=True, to='app.tag'),
        ),
    ]