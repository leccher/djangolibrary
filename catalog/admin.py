from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, Loan, Language

admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)

class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book
    fields = ['title','subtitle','coauthors']
    can_delete = False
    readonly_fields=['title','subtitle','coauthors']
    

# Define a ModelAdmin will change the default admin view
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    # In admin view show the list with declared fields
    list_display = ('first_name', 'last_name', 'middle_name','date_of_birth', 'date_of_death')
    # In admin detail view we can group (to show horizzontaly if enough space) fields
    fields = [('first_name','middle_name'), 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for BookInstance using the decorator
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    # The fields I want in admin list
    list_display = ('book','loaner','loan_date')
    # This show filters on the right of teh view
    list_filter = ('status','loan_date')
    # This organize fields
    fieldsets = (
        (None, {
            'fields': ('book', 'loaner', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'loan_date')
        }),
    )

class LoanInline(admin.TabularInline):
    readonly_fields = ('id','status','loaner','loan_date')
    model = Loan
    can_delete = False
    extra = 0

# Register the Admin classes for Book using the decorator
@admin.register(Book) # same as admin.site.register(Author, AuthorAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','subtitle', 'display_genre')
    inlines = [LoanInline]
