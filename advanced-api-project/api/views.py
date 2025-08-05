from rest_framework import filters
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from .models import Book #replace with your working model
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django_filters import rest_framework

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Create your views here.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": "You are authenticated!"})
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": "You are authenticated!"})
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": "You are authenticated!"})
