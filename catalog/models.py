from django.db import models
from django.core import validators
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

import uuid # Required for unique book instances

DEFAULT_LANGUAGE_ID=1

# Create your models here.
class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,help_text="The eventual middle name",blank=True,null=True,default=None)
    last_name = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text='Some anecdotes about the author',blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True,default=None)

    class Meta:
        ordering = ['first_name','last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Publisher(models.Model):
    """Model representing a book editor."""
    name = models.CharField(max_length=200, help_text='Enter a book Publisher (e.g. Mondadori)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Series(models.Model):
    """Model representing a book series."""
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, help_text='Enter a book series (e.g. Oscar absolute)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class Saga(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField(Genre, help_text='Select genres for this saga')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('saga-detail', args=[str(self.id)])

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200,null=True,help_text="Eventual subtitle of the book",blank=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True,blank=True)

    saga = models.ForeignKey(Saga, on_delete=models.SET_NULL, null=True,blank=True)
    coauthors = models.CharField(max_length=200,null=True,help_text="Other authors",blank=True)

    summary = models.TextField(max_length=2000, help_text='Enter a brief description of the book',blank=True)
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', blank=True)
    ean = models.CharField('EAN', max_length=13, help_text='13 Character <a href="https://www.ean-search.org">EAN number</a>', blank=True)
    pages = models.SmallIntegerField(blank=False,default=0)
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genres = models.ForeignKey(Genre, help_text='Select a genre for this book',null=True,blank=True,default=None,on_delete=models.SET_NULL)

    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True,default=DEFAULT_LANGUAGE_ID)

    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    vendor_url = models.URLField(blank=True,null=True)
    # Default method used to show as text book instances
    def __str__(self):
        """String for representing the Model object."""
        return '{} - by {}'.format(self.title,self.author)

    # Function usd in admin site when editing an instance for riseing a specific view
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

    # Show first 3 of genre
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    # Used in tabls as head title 
    display_genre.short_description = 'Genre'

class Loaner(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200,blank=True)
    phone_v = validators.RegexValidator(regex=r'^\d{9,15}$', message="Phone number should be in number format: '+999999999'. Admitted from 9 to 15 ciphers.")
    phone = models.CharField(verbose_name="Numero di telefono",validators=[phone_v], max_length=15, blank=True) # validators should be a list
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Loan(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    loaner = models.ForeignKey(Loaner, on_delete=models.SET_NULL, null=True, blank=True)
    loan_date = models.DateField(null=True, blank=True)
    back_date = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['loan_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.book.pk)])