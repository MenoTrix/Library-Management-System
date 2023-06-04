from django.urls import path
from lib_app.views import showBooks, showIndex, update_books, delete_books

urlpatterns = [
    path("", showIndex, name="index"),
    path("books", showBooks, name="books"),
    path("update/<int:id>", update_books, name="update"),
    path("delete/<int:id>", delete_books, name="delete"),
]
