import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookTests(TestCase):
    def setUp(self):
        Book.objects.create(title='Война и мир', author='Л. Н. Толстой', publish_year=1969)
    
    def test_book_create(self):
        book_war_and_peace = Book.objects.get(title='Война и мир')
        self.assertEqual(book_war_and_peace.title, 'Война и мир')
    

class BookViewTest(APITestCase):
    client = APIClient()
    url = reverse('get_post_book')

    def setUp(self):
        Book.objects.create(title='Война и мир', author='Л. Н. Толстой', publish_year=1969)
        Book.objects.create(title='Война и мир2', author='Л. Н. Толстой', publish_year=1971)
        Book.objects.create(title='Война и мир3', author='Л. Н. Толстой', publish_year=1973)
    

    def test_get_all_books(self):
        '''
        Запрос на вывод всех книг
        '''
        books = Book.objects.all()
        serialized = BookSerializer(books, many=True)

        response = self.client.get(self.url)
        self.assertEqual(serialized.data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
    

    def test_add_new_book(self):
        '''
        Запрос на добавление новой книги
        '''
        book = {
            'title': 'Война и мир4', 
            'author': 'Л. Н. Толстой',
            'publish_year': 1975
        }

        response = self.client.post(self.url, 
                            data=json.dumps(book),
                            content_type='application/json')
        
        self.assertEqual(response.data, book)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_add_book_negative_publish_year(self):
        '''
        Запрос на добавление новой книги c некорректным годом выпуска
        '''
        book = {
            'title': 'Война и мир4', 
            'author': 'Л. Н. Толстой',
            'publish_year': -1975
        }

        response = self.client.post(self.url, 
                            data=json.dumps(book),
                            content_type='application/json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


