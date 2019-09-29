from django.urls import path
from .views import BookListView, BookDetailView

# app_name = "books"

urlpatterns = [
    path('books/', BookListView.as_view(), name='get_post_book'),
    path('books/<int:pk>', BookDetailView.as_view(), name='get_put_delete_book'),
]