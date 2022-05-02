from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('sagas/', views.SagaListView.as_view(), name='sagas'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('languages/', views.LanguageListView.as_view(), name='languages'),
    path('loaners/', views.LoanerListView.as_view(), name='loaners'),
    path('publishers/', views.PublisherListView.as_view(), name='publishers'),
    path('serieses/', views.SeriesListView.as_view(), name='serieses'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('loaner/<int:pk>', views.LoanerDetailView.as_view(), name='loaner-detail'),
    path('saga/<int:pk>', views.SagaDetailView.as_view(), name='saga-detail'),
    path('publisher/<int:pk>', views.PublisherDetailView.as_view(), name='publisher-detail'),
    path('series/<int:pk>', views.SeriesDetailView.as_view(), name='series-detail'),
    path('books/loaned', views.LoanedBooksListView.as_view(), name='loaned-books'),

    # Creazione, modifica e cancellazione di un libro
    path('saga/create/', views.SagaCreate.as_view(), name='saga-create'),
    path('saga/<int:pk>/update/', views.SagaUpdate.as_view(), name='saga-update'),
    path('saga/<int:pk>/delete/', views.SagaDelete.as_view(), name='saga-delete'),

    # Creazione, modifica e cancellazione di un libro
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    
    # Creazione, modifica e cancellazione di una lingua
    path('language/create/', views.LanguageCreate.as_view(), name='language-create'),
    path('language/<int:pk>/update/', views.LanguageUpdate.as_view(), name='language-update'),
    path('language/<int:pk>/delete/', views.LanguageDelete.as_view(), name='language-delete'),

    # Creazione, modifica e cancellazione di un genere
    path('genre/create/', views.GenreCreate.as_view(), name='genre-create'),
    path('genre/<int:pk>/update/', views.GenreUpdate.as_view(), name='genre-update'),
    path('genre/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre-delete'),

    # Creazione, modifica e cancellazione di un editore
    path('publisher/create/', views.PublisherCreate.as_view(), name='publisher-create'),
    path('publisher/<int:pk>/update/', views.PublisherUpdate.as_view(), name='publisher-update'),
    path('publisher/<int:pk>/delete/', views.PublisherDelete.as_view(), name='publisher-delete'),

    # Creazione, modifica e cancellazione di un editore
    path('series/create/', views.SeriesCreate.as_view(), name='series-create'),
    path('series/<int:pk>/update/', views.SeriesUpdate.as_view(), name='series-update'),
    path('series/<int:pk>/delete/', views.SeriesDelete.as_view(), name='series-delete'),

    # Creazione, modifica e cancellazione di un genere
    path('loaner/create/', views.LoanerCreate.as_view(), name='loaner-create'),
    path('loaner/<int:pk>/update/', views.LoanerUpdate.as_view(), name='loaner-update'),
    path('loaner/<int:pk>/delete/', views.LoanerDelete.as_view(), name='loaner-delete'),

    # Creazione, modifica e cancellazione di un autore
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),

    # Aggiunta di un libro ad una saga
    path('saga/<int:pk>/addbook', views.add_book_to_saga, name='add-book-to-saga'),
    # Aggiunta di un libro ad un autore
    path('author/<int:pk>/addbook', views.add_book_to_author, name='add-book-to-author'),
    # Duplica libro
    path('book/<int:pk>/addbook', views.duplicate_book, name='book-duplicate'),
    # Presta libro
    path('book/<int:pk>/loan/', views.loan_book, name='book-loan'),
    path('book/<int:pk>/loanback/', views.loanback_book, name='book-loanback'),
    # Auto management Model
    # Creazione, modifica e cancellazione di un autore
    #path('<str:model>/<str:action>/', views.generic_view, name='generic-view'),
    #path('<str:model>/create/', views.GenericCreate.as_view(), name='model-create'),
    #path('<str:model>/<int:pk>/update/', views.GenericUpdate.as_view(), name='model-update'),
    #path('<str:model>/<int:pk>/delete/', views.GenericDelete.as_view(), name='model-delete'),

    re_path(r'^(?P<mmodel>\w+)/create/$', views.GenericCreate.as_view(), name='test_view'),
    
]