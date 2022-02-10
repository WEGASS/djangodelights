from django.shortcuts import render, redirect
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.db.models import Sum
from .forms import PurchaseCreateForm
import datetime

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/home.html'
    today = datetime.date.today()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.all()
        context['recipes'] = RecipeRequirement.objects.all()
        context['menu_items'] = MenuItem.objects.all()
        context['today'] = datetime.datetime.today()
        context['today_purchases'] = Purchase.objects.filter(timestamp__gte=self.today)
        return context

#INGREDIENTS
class IngredientView(LoginRequiredMixin, ListView):
    template_name = 'inventory/ingredients.html'
    model = Ingredient


class CreateIngredientView(LoginRequiredMixin, CreateView):
    template_name = 'inventory/ingredient_create_form.html'
    model = Ingredient
    fields = '__all__'


class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    template_name = 'inventory/ingredient_update_form.html'
    model = Ingredient
    fields = '__all__'


class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    template_name = 'inventory/ingredient_delete_form.html'
    model = Ingredient
    success_url = '/ingredients/'

#MENU
class MenuItemView(LoginRequiredMixin, ListView):
    template_name = 'inventory/menu.html'
    model = MenuItem


class CreateMenuItemView(LoginRequiredMixin, CreateView):
    template_name = 'inventory/menu_create_form.html'
    model = MenuItem
    fields = '__all__'


class UpdateMenuItemView(LoginRequiredMixin, UpdateView):
    template_name = 'inventory/menu_update_form.html'
    model = MenuItem
    fields = '__all__'


class DeleteMenuItemView(LoginRequiredMixin, DeleteView):
    template_name = 'inventory/menu_delete_form.html'
    model = MenuItem
    success_url = '/menu/'


#RECIPES
class RecipeView(LoginRequiredMixin, ListView):
    template_name = 'inventory/recipes.html'
    model = RecipeRequirement


class CreateRecipeView(LoginRequiredMixin, CreateView):
    template_name = 'inventory/recipe_create_form.html'
    model = RecipeRequirement
    fields = '__all__'


class UpdateRecipeView(LoginRequiredMixin, UpdateView):
    template_name = 'inventory/recipe_update_form.html'
    model = RecipeRequirement
    fields = '__all__'


class DeleteRecipeView(LoginRequiredMixin, DeleteView):
    template_name = 'inventory/recipe_delete_form.html'
    model = RecipeRequirement
    success_url = '/recipes/'


#PURCHASES
class PurchaseView(LoginRequiredMixin, ListView):
    template_name = 'inventory/purchases.html'
    model = Purchase


class CreatePurchaseView(LoginRequiredMixin, CreateView):
    template_name = 'inventory/purchase_create_form.html'
    model = Purchase
    form_class = PurchaseCreateForm

    def get_menu(self):
        return [m.pk for m in MenuItem.objects.all() if m.available()]

    def get_form_kwargs(self):
        kwargs = super(CreatePurchaseView, self).get_form_kwargs()
        kwargs['menu'] = self.get_menu()
        print(self.get_menu())
        return kwargs

    def form_valid(self, form):
        purchased_item = form.cleaned_data['purchased_item']
        used_ingredients = purchased_item.reciperequirement_set.all()
        for i in used_ingredients:
            i.ingredient.quantity -= i.quantity
            i.ingredient.save()
        return super().form_valid(form)


#REPORTS
class ReportsView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/reports.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchases = Purchase.objects.all()
        context['purchases'] = purchases
        revenue = purchases.aggregate(revenue=Sum('purchased_item__price'))['revenue']
        context['total_revenue'] = revenue
        total_cost = 0
        for purchase in purchases:
            for ingred in purchase.purchased_item.reciperequirement_set.all():
                total_cost += (ingred.ingredient.unit_price * ingred.quantity)
        context['total_cost'] = total_cost
        context["profit"] = revenue - total_cost
        return context


#LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')


# class CreatePurchaseView(LoginRequiredMixin, View):
#
#     def get(self, request, *args, **kwargs):
#         context = {'form':PurchaseCreateForm()}
#         return render(self.request, 'inventory/purchase_create_form.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = PurchaseCreateForm(self.request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#         return redirect('purchases')