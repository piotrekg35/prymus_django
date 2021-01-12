from django.shortcuts import render
from cos.models import Book

# Create your views here.
def index(request):
    return render (request,"index1.html")
def books_list(request):
    context ={"books": Book.objects.all()}
    return render (request, "lista.html",context)
def book_details(request, book_id):
    context={"book": Book.objects.get(id=book_id)}
    return render (request, "book_details.html",context)