from django.shortcuts import render
from cos.models import Book
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render (request,"index1.html")
def books_list(request):
    context ={"books": Book.objects.all()}
    return render (request, "lista.html",context)
def book_details(request, book_id):
    context={"book": Book.objects.get(id=book_id)}
    return render (request, "book_details.html",context)
def usr_signup(request):
    form = None
    if request.method == "POST":
        # stwórz użytkownika
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # formularz poprawny, można zapisać użytkownika
            form.save()
            # przekierowanie na stronę z podziękowaniem
            return render(request, "registration/signup_complete.html")
    else:
        # pokaż pusty formularze rejestracji
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "registration/signup_form.html", context) 