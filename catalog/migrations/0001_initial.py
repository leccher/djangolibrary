# Generated by Django 4.0.3 on 2022-05-02 14:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, help_text='The eventual middle name', max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('summary', models.TextField(blank=True, help_text='Some anecdotes about the author', max_length=1000)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, default=None, null=True, verbose_name='Died')),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, help_text='Eventual subtitle of the book', max_length=200, null=True)),
                ('coauthors', models.CharField(blank=True, help_text='Other authors', max_length=200, null=True)),
                ('summary', models.TextField(blank=True, help_text='Enter a brief description of the book', max_length=2000)),
                ('isbn', models.CharField(blank=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN')),
                ('ean', models.CharField(blank=True, help_text='13 Character <a href="https://www.ean-search.org">EAN number</a>', max_length=13, verbose_name='EAN')),
                ('pages', models.SmallIntegerField(default=0)),
                ('vendor_url', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre (e.g. Science Fiction)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Loaner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number should be in number format: '+999999999'. Admitted from 9 to 15 ciphers.", regex='^\\d{9,15}$')], verbose_name='Numero di telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book Publisher (e.g. Mondadori)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book series (e.g. Oscar absolute)', max_length=200)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Saga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author')),
                ('genres', models.ManyToManyField(help_text='Select genres for this saga', to='catalog.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('loan_date', models.DateField(blank=True, null=True)),
                ('back_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='a', help_text='Book availability', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.book')),
                ('loaner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.loaner')),
            ],
            options={
                'ordering': ['loan_date'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(blank=True, help_text='Select a genre for this book', null=True, to='catalog.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='saga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.saga'),
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.series'),
        ),
    ]
