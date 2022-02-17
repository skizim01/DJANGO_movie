from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from .models import Students, Category, Specialty,Techers




class GenreSpecTech:

    def get_category(self):
        return Category.objects.all()

    def get_spec(self):
        return Specialty.objects.all()

    def get_tech(self):
        return Techers.objects.all()


class StudentsView(GenreSpecTech, ListView):
    """Список фильмов"""
    model = Students
    queryset = Students.objects.all()


#
class FilterMoviesView(GenreSpecTech, ListView):
    """Фильтр фильмов"""

    def get_queryset(self):
        queryset = Students.objects.filter(
            Q(category__in=self.request.GET.getlist("category")) |
            Q(specialty__in=self.request.GET.getlist("specialty"))
        )
        return queryset


class AddStudent(View):

    def post(self, request):
        if request.method == "POST":
            name = request.POST["name"]
            category = Category.objects.get(name=request.POST["category"])
            specialty = Specialty.objects.get(name=request.POST["specialty"])
            expectation = request.POST["expectation"]
            Students.objects.get_or_create(name=name, category=category,
                                           specialty=specialty,  expectation=expectation,
                                           age=12)
            return redirect("/")

