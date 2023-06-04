from django import forms
from lib_app.models import Book, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "name",
            "author",
            "image",
            "author_image",
            "price",
            "book_pages",
            "book_rental_by_dy",
            "book_rental_period",
            "book_computed_rental",
            "status",
            "category",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "author_image": forms.FileInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "book_pages": forms.NumberInput(attrs={"class": "form-control"}),
            "book_rental_by_dy": forms.NumberInput(
                attrs={"class": "form-control", "id": "rental_price"}
            ),
            "book_rental_period": forms.NumberInput(
                attrs={"class": "form-control", "id": "rental_period"}
            ),
            "book_computed_rental": forms.NumberInput(
                attrs={"class": "form-control", "id": "rental_total"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }
