from django import forms
from .models import Ingredent, MenuItem, RecipeRequirement, Purchase, PurchaseItem

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredent
        fields =['name','quantity','unit','price_per_unit']



class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'image', 'ingredients']

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ['ingredient', 'quantity', 'menu_item']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['created_at', 'total_price', 'menu_items']

class PurchaseItem(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['purchase', 'menu_item', 'quantity']