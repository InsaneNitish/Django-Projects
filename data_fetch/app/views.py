from django.shortcuts import render,redirect
from app.models import *
# Create your views here.
def home(request):
    books=Book.objects.all()
    return render(request,"homepage.html",{"books" : books})

def addBook(request):
    if(request.method=='POST'):
        book_name=request.POST['book_name']
        author_name=request.POST['author_name']
        book_desc=request.POST['book_desc']
        book_cover=request.POST['book_cover']

        book=Book(book_name=book_name,author_name=author_name,book_desc=book_desc,book_cover=book_cover)
        book.save()
        return redirect('homepage')
    return render(request,'addBook.html')

def deleteBook(request):
    return




    