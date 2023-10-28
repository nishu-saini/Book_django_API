# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from .models import Book
# from .serializer import BookSerializer

# # Get all books
# @api_view(['GET'])
# def book_list(req):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)

#     return Response(serializer.data, status=status.HTTP_200_OK)


# # add book
# @api_view(['POST'])
# def add_book(req):
#     serializer = BookSerializer(data = req.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def book(req, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except:
#         return Response({
#             'error': 'Book not found'
#         }, status=status.HTTP_404_NOT_FOUND)

#     if req.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif req.method == "PUT":
#         serializer = BookSerializer(book, data = req.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif req.method == 'DELETE':
#         book.delete()

#         data = {
#             "message": "Book deleted successfully!"
#         }
#         return Response(data, status=status.HTTP_204_NO_CONTENT)

from rest_framework.views import APIView
from rest_framework.response import Response
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework import status

class BookList(APIView):
    def get(self, req):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateBook(APIView):
    def post(self, req):
        serializer = BookSerializer(data = req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookInfo(APIView):

    def find_book(self, pk):
        try:
            book = Book.objects.get(pk=pk)
            return book
        except:
            return None
    

    def get(self, req, pk):
        book = self.find_book(pk)

        if not book:
            return Response({
                'error': 'Book not found'
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, req, pk):
        book = self.find_book(pk)

        if not book:
            return Response({
                'error': 'Book not found'
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data = req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, req, pk):
        book = self.find_book(pk)

        if not book:
            return Response({
                'error': 'Book not found'
            }, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(
            { "message": "Book deleted successfully!" }, 
            status=status.HTTP_204_NO_CONTENT
        )
