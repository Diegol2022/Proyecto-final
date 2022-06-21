from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from recipe.models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe/recipe_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe/recipe_detail.html"
    fields = ['name', 'description']


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    success_url = reverse_lazy('recipe:recipe-list')
    fields = ['name', 'description']


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    success_url = reverse_lazy('recipe:recipe-list')
    fields = ['name', 'description']


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe:recipe-list')
