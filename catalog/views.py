from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

import datetime
# Decorator for view requiring login
from django.contrib.auth.decorators import login_required

# Class for view requiring login
from django.contrib.auth.mixins import LoginRequiredMixin

# More views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Catalog
from catalog.models import *

# Forms
from catalog.forms import *

DEFAULT_LIST_ITEMS=20
#@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = Loan.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = Loan.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_generes = Genre.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_generes': num_generes,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

#class BookListView(LoginRequiredMixin,generic.ListView):
class BookListView(generic.ListView):
    model = Book
    paginate_by = DEFAULT_LIST_ITEMS
    # your own name for the list as a template variable
    # default modelname_list
    #context_object_name = 'my_book_list'
    # Get 5 books containing the title war
    # defaut all objects available
    #queryset = Book.objects.filter(title__icontains='war')[:5] 
    # Specify your own template name/location
    # default templates/appname/modelname_list.html
    #template_name = 'books/my_arbitrary_template_name_list.html'  

    # sovrascrive get_queryset() per modificare la lista di record restituiti.
    def get_queryset(self):
        # Get 5 books containing the title libro
        #return Book.objects.filter(title__icontains='libro')[:5]
        return Book.objects.order_by('title')

    # per passare altre variabili addizionali di context al template 
    # (es. la lista di libri è passata per default). 
    # Il frammento sotto mostra come aggiungere una variabile "some_data" al 
    # context (sarà quindi disponibile come variabile del template).
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = DEFAULT_LIST_ITEMS
    ordering = ['first_name','last_name']

class LoanerListView(generic.ListView):
    model = Loaner
    paginate_by = DEFAULT_LIST_ITEMS
    ordering = ['name']

class GenreListView(generic.ListView):
    model = Genre
    paginate_by = DEFAULT_LIST_ITEMS
    ordering = ['name']

class LanguageListView(generic.ListView):
    model = Language
    paginate_by = DEFAULT_LIST_ITEMS
    ordering = ['name']

class PublisherListView(generic.ListView):
    model = Publisher
    paginate_by = DEFAULT_LIST_ITEMS
    ordering = ['name']

class SeriesListView(generic.ListView):
    model = Series
    paginate_by = DEFAULT_LIST_ITEMS
    ordering = ['name']

class SagaListView(generic.ListView):
    model = Saga
    paginate_by = DEFAULT_LIST_ITEMS
    ordering = ['title']

class LanguageCreate(LoginRequiredMixin,CreateView):
    model = Language
    fields = '__all__'
    success_url = reverse_lazy('languages')
class LanguageUpdate(LoginRequiredMixin,UpdateView):
    model = Language
    fields = '__all__'
    success_url = reverse_lazy('languages')
class LanguageDelete(LoginRequiredMixin,DeleteView):
    model = Language
    success_url = reverse_lazy('languages')

class GenreCreate(LoginRequiredMixin,CreateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('genres')
class GenreUpdate(LoginRequiredMixin,UpdateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('genres')
class GenreDelete(LoginRequiredMixin,DeleteView):
    model = Genre
    success_url = reverse_lazy('genres')

class PublisherCreate(LoginRequiredMixin,CreateView):
    model = Publisher
    fields = '__all__'
    success_url = reverse_lazy('publishers')
class PublisherUpdate(LoginRequiredMixin,UpdateView):
    model = Publisher
    fields = '__all__'
    success_url = reverse_lazy('publishers')
class PublisherDelete(LoginRequiredMixin,DeleteView):
    model = Publisher
    success_url = reverse_lazy('publishers')

class SeriesCreate(LoginRequiredMixin,CreateView):
    model = Series
    fields = '__all__'
    success_url = reverse_lazy('serieses')
class SeriesUpdate(LoginRequiredMixin,UpdateView):
    model = Series
    fields = '__all__'
    success_url = reverse_lazy('serieses')
class SeriesDelete(LoginRequiredMixin,DeleteView):
    model = Series
    success_url = reverse_lazy('serieses')

class SagaCreate(LoginRequiredMixin,CreateView):
    model = Saga
    fields = '__all__'
    success_url = reverse_lazy('sagas')
class SagaUpdate(LoginRequiredMixin,UpdateView):
    model = Saga
    fields = '__all__'
    success_url = reverse_lazy('sagas')
class SagaDelete(LoginRequiredMixin,DeleteView):
    model = Saga
    success_url = reverse_lazy('sagas')

class BookCreate(LoginRequiredMixin,CreateView):
    model = Book
    fields = '__all__'
class BookUpdate(LoginRequiredMixin,UpdateView):
    model = Book
    fields = '__all__'
class BookDelete(LoginRequiredMixin,DeleteView):
    model = Book
    success_url = reverse_lazy('books')

class LoanerCreate(LoginRequiredMixin,CreateView):
    model = Loaner
    fields = '__all__'
    success_url = reverse_lazy('loaners')
class LoanerUpdate(LoginRequiredMixin,UpdateView):
    model = Loaner
    fields = '__all__'
    success_url = reverse_lazy('loaners')
class LoanerDelete(LoginRequiredMixin,DeleteView):
    model = Loaner
    success_url = reverse_lazy('loaners')

class AuthorCreate(LoginRequiredMixin,CreateView):
    model = Author
    fields = '__all__'
class AuthorUpdate(LoginRequiredMixin,UpdateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('authors')
class AuthorDelete(LoginRequiredMixin,DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

def generic_view(request,model,action):
    print("model={}".format(model))
    print("action={}".format(action))
    return getattr(o, name)

class GenericCreate(LoginRequiredMixin,CreateView):
    template_name='catalog/generic_form.html'
    def get_form_class(self):
        SOME_FORMS = {
            "saga" : SagaCreate,
            "Cat" : "UpdateCatForm",
            "Frog" : "UpdateFrogForm",
        }
        form_class_name = SOME_FORMS["saga"]
        #form_class_name now takes the values "UpdateDogForm"
        #, "UpdateCatForm" or "UpdateFrogFrom"
        return form_class_name
    
class GenericUpdate(LoginRequiredMixin,UpdateView):
    pass
class GenericDelete(LoginRequiredMixin,DeleteView):
    pass

class BookDetailView(generic.DetailView):
    model = Book
    def book_detail_view(request, primary_key):
        obj = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'object': obj})

class SagaDetailView(generic.DetailView):
    model = Saga
    def saga_detail_view(request, primary_key):
        obj = get_object_or_404(Saga, pk=primary_key)
        return render(request, 'catalog/saga_detail.html', context={'object': obj})

class PublisherDetailView(generic.DetailView):
    model = Publisher
    def publisher_detail_view(request, primary_key):
        obj = get_object_or_404(Publisher, pk=primary_key)
        return render(request, 'catalog/publisher_detail.html', context={'object': obj})

class SeriesDetailView(generic.DetailView):
    model = Series
    def series_detail_view(request, primary_key):
        obj = get_object_or_404(Series, pk=primary_key)
        return render(request, 'catalog/series_detail.html', context={'object': obj})

class AuthorDetailView(generic.DetailView):
    model = Author
    def book_detail_view(request, primary_key):
        obj = get_object_or_404(Author, pk=primary_key)
        return render(request, 'catalog/author_detail.html', context={'object': obj})

class LoanerDetailView(generic.DetailView):
    model = Loaner
    def book_detail_view(request, primary_key):
        obj = get_object_or_404(Loaner, pk=primary_key)
        return render(request, 'catalog/loaner_detail.html', context={'object': obj})

class LoanedBooksListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan."""
    model = Loan
    template_name ='catalog/book_list_loaned.html'
    paginate_by = 10

    def get_queryset(self):
        return Loan.objects.filter(back_date__isnull=True   ).order_by('loan_date')

def add_book_to_saga(request,pk):
    try:
        obj = Saga.objects.get(pk=pk)
    except Saga.DoesNotExist:
        raise Http404("Saga does not exist")
    
    book = Book(saga=obj)
    # Se è una richiesta di tipo POST allora processa i dati della Form
    if request.method == 'POST':

        # Crea un'istanza della form e la popola con i dati della richiesta (binding):
        form = AddBookForm(request.POST)

        # Controlla se la form è valida:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book.title = form.cleaned_data['title']
            book.subtitle = form.cleaned_data['title']
            book.summary = form.cleaned_data['summary']
            book.isbn = form.cleaned_data['isbn']
            book.pages = form.cleaned_data['pages']
            book.vendor_url = form.cleaned_data['vendor_url']
            book.coauthors = form.cleaned_data['coauthors']
            book.saga = form.cleaned_data['saga']
            book.language = form.cleaned_data['language']
            book.publisher = form.cleaned_data['publisher']
            book.series = form.cleaned_data['series']
            book.save()

            for obj in form.cleaned_data['genres']:
                book.genres.add(obj)
            
            # reindirizza ad un nuovo URL:
            return HttpResponseRedirect(reverse('sagas'))

    # Se la richiesta è GET o un altro metodo crea il form di default
    else:
        form = AddBookForm(initial={'saga': obj,'author':obj.author,'genres':obj.genres.all()})

    context = {
        'form': form
    }

    return render(request, 'catalog/book_form.html', context)

def add_book_to_author(request,pk):
    try:
        obj = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")
    
    book = Book(author=obj)
    # Se è una richiesta di tipo POST allora processa i dati della Form
    if request.method == 'POST':

        # Crea un'istanza della form e la popola con i dati della richiesta (binding):
        form = AddBookForm(request.POST)

        # Controlla se la form è valida:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book.title = form.cleaned_data['title']
            book.subtitle = form.cleaned_data['title']
            book.summary = form.cleaned_data['summary']
            book.isbn = form.cleaned_data['isbn']
            book.pages = form.cleaned_data['pages']
            book.vendor_url = form.cleaned_data['vendor_url']
            book.coauthors = form.cleaned_data['coauthors']
            book.saga = form.cleaned_data['saga']
            book.language = form.cleaned_data['language']
            book.publisher = form.cleaned_data['publisher']
            book.series = form.cleaned_data['series']
            book.save()

            for obj in form.cleaned_data['genres']:
                book.genres.add(obj)
            
            # reindirizza ad un nuovo URL:
            return HttpResponseRedirect(reverse('sagas'))

    # Se la richiesta è GET o un altro metodo crea il form di default
    else:
        form = AddBookForm(initial={'author': obj})

    context = {
        'form': form
    }

    return render(request, 'catalog/book_form.html', context)

def duplicate_book(request,pk):
    try:
        obj = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    book_json={
            'title':obj.title,
            'subtitle':obj.subtitle,
            'summary':obj.summary,
            'isbn':obj.isbn,
            'ean':obj.ean,
            'pages':obj.pages,
            'vendor_url':obj.vendor_url,
            'coauthors':obj.coauthors,
            'saga':obj.saga,
            'language':obj.language,
            'publisher':obj.publisher,
            'series':obj.series,
            'author': obj.author,
            'generes': obj.genres
            }
    book = Book(book_json)
    # Se è una richiesta di tipo POST allora processa i dati della Form
    if request.method == 'POST':

        # Crea un'istanza della form e la popola con i dati della richiesta (binding):
        form = AddBookForm(request.POST)

        # Controlla se la form è valida:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book.title = form.cleaned_data['title']
            book.subtitle = form.cleaned_data['title']
            book.summary = form.cleaned_data['summary']
            book.isbn = form.cleaned_data['isbn']
            book.ean = form.cleaned_data['ean']
            book.pages = form.cleaned_data['pages']
            book.vendor_url = form.cleaned_data['vendor_url']
            book.coauthors = form.cleaned_data['coauthors']
            book.author = form.cleaned_data['author']
            book.saga = form.cleaned_data['saga']
            book.language = form.cleaned_data['language']
            book.publisher = form.cleaned_data['publisher']
            book.series = form.cleaned_data['series']
            book.save()

            for obj in form.cleaned_data['genres']:
                book.genres.add(obj)
            
            # reindirizza ad un nuovo URL:
            return HttpResponseRedirect(reverse('sagas'))

    # Se la richiesta è GET o un altro metodo crea il form di default
    else:
        form = AddBookForm(initial=book_json)

    context = {
        'form': form,
        'book':book
    }

    return render(request, 'catalog/book_form.html', context)

def loan_book(request,pk):
    try:
        obj = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    loan = Loan(book=obj)
    # Se è una richiesta di tipo POST allora processa i dati della Form
    if request.method == 'POST':

        # Crea un'istanza della form e la popola con i dati della richiesta (binding):
        form = LoanForm(request.POST)

        # Controlla se la form è valida:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            loan.loaner = form.cleaned_data['loaner']
            loan.loan_date = form.cleaned_data['loan_date']
            loan.save()

            # reindirizza ad un nuovo URL:
            return HttpResponseRedirect(reverse('loaned-books'))

    # Se la richiesta è GET o un altro metodo crea il form di default
    else:
        form = LoanForm(initial={'book':obj,'loan_date':datetime.date.today})

    context = {
        'form': form,
        'loan':loan
    }

    return render(request, 'catalog/loan_form.html', context)

def loanback_book(request,pk):
    try:
        loan = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
        raise Http404("Loan does not exist")
    # Se è una richiesta di tipo POST allora processa i dati della Form
    if request.method == 'POST':

        # Crea un'istanza della form e la popola con i dati della richiesta (binding):
        form = LoanForm(request.POST)

        # Controlla se la form è valida:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            loan.loaner = form.cleaned_data['loaner']
            loan.loan_date = form.cleaned_data['loan_date']
            loan.back_date = form.cleaned_data['back_date']
            loan.save()

            # reindirizza ad un nuovo URL:
            return HttpResponseRedirect(reverse('loaned-books'))

    # Se la richiesta è GET o un altro metodo crea il form di default
    else:
        form = LoanForm(initial={'pk':loan.pk,'book':loan.book,'loan_date':loan.loan_date,'loaner':loan.loaner,'back_date':datetime.date.today})

    context = {
        'form': form,
        'loan':loan
    }

    return render(request, 'catalog/loan_form.html', context)