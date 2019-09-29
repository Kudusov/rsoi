from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serialized = BookSerializer(books, many=True)

        return Response(serialized.data)
    
    def post(self, request):
        serialized = BookSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)

        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        serialized = BookSerializer(book)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        book.delete()

        return Response({"message": "Book with id '{}' succesfully deleted".format(pk)}, status=status.HTTP_204_NO_CONTENT)
