from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from lib_app.models import Book, Category
from lib_app.forms import BookForm, CategoryForm

# Create your views here.


def showIndex(request):
    if request.method == "POST":
        new_book = BookForm(request.POST, request.FILES)

        if new_book.is_valid():
            new_book.save()
            return redirect("index")
        new_category = CategoryForm(request.POST)
        if new_category.is_valid():
            new_category.save()
            return redirect("index")

    booksForm = BookForm()
    category_form = CategoryForm()
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        "lib_app/pages/index.html",
        context={
            "books": books,
            "categories": categories,
            "form": booksForm,
            "category_form": category_form,
            "book_number": Book.objects.filter(active=True).count(),
            "available_books": Book.objects.filter(status="available").count(),
            "rented_books": Book.objects.filter(status="rented").count(),
            "sold_books": Book.objects.filter(status="sold").count(),
        },
    )


def showBooks(request):
    book_name = None
    search_book = Book.objects.all()
    if "search_name" in request.GET:
        book_name = request.GET["search_name"]
        print("=>>>>>>>>>>>>>>>>", book_name)
        if book_name:
            search_book = search_book.filter(name__icontains=book_name)

    category_form = CategoryForm()

    categories = Category.objects.all()

    return render(
        request,
        "lib_app/pages/books.html",
        context={
            "books": search_book,
            "categories": categories,
            "category_form": category_form,
        },
    )


def update_books(request, id):
    book_id = Book.objects.get(id=id)
    # Post Request it will Post the data after it's retrieved in Get  so the Else will run first then If

    if request.method == "POST":
        form_for_book = BookForm(request.POST, request.FILES, instance=book_id)
        if form_for_book.is_valid():
            form_for_book.save()
        return redirect("/")
    else:
        # Get Request it will retrieve the post and it will happen when i press on تعديل
        form_for_book = BookForm(instance=book_id)
        return render(
            request, "lib_app/pages/update.html", context={"form": form_for_book}
        )


def delete_books(request, id):
    get_book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        get_book.delete()
        return redirect("/")
    return render(request, "lib_app/pages/delete.html")
