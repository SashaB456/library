# Generated by Django 5.1.6 on 2025-02-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200)),
                ('available', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['author'],
                'indexes': [models.Index(fields=['title', 'isbn'], name='folder_libr_title_6c208c_idx')],
                'unique_together': {('title', 'author')},
            },
        ),
    ]
