from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase, PurchaseItem

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields =['name','quantity','unit','price_per_unit']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title','price', 'image']

    ingredients = forms.ModelMultipleChoiceField(
        queryset = Ingredient.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = False
    )


    def save(self, commit=True):
        menu_item = super().save(commit=False)
        if commit:
            menu_item.save()
            self.save_ingredients(menu_item)
        return menu_item

    def save_ingredients(self, menu_item):
        ingredients = self.cleaned_data['ingredients']
        quantity = self.cleaned_data['ingredient_quantities']

        for ingredient in ingredients:
            RecipeRequirement.objects.create(
                menu_item=menu_item,
                ingredient=ingredient,
                quantity=quantity
            )

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ['ingredient', 'quantity', 'menu_item']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['total_price', 'purchase_items']

class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['menu_item', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget = forms.NumberInput(attrs={'min': 0})