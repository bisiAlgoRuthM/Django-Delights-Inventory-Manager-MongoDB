from django.shortcuts import render, redirect
from .forms import IngredientForm, RecipeRequirementForm, MenuItemForm, PurchaseForm
from .models import Purchase, MenuItem, PurchaseItem
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def add_ingredent(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save() #save to database
            return redirect('success_page')
    else:
        form = IngredientForm()
    return render(request, 'add_ingredient.html', {'form' : form})


def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.save() #save to database
            form.save_m2m()
            return redirect('success_page')
    else:
        form = MenuItemForm()
    return render(request, 'add_menu_item.html', {'form':form})

def add_recipe_requirement(request):
    if request.method == 'POST':
        form = RecipeRequirementForm(request.POST)
        if form.is_valid():
            form.save() #save to database
            return redirect('success_page')
    else:
        form = RecipeRequirementForm()
    return render(request, 'add_recipe_requirement.html', {'form':form})

def success_page(request):
    return render(request, 'success_page.html')

def purchase_success(request):
    return render(request, 'purchase_success.html')

def new_purchase(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            menu_item_id = form.cleaned_data['menu_item']
            menu_item = MenuItem.objects.get(pk=menu_item_id)
            quantity = form.cleaned_data['quantity']

            new_purchase = Purchase.objects.create(total_price=0)

            purchase_item = PurchaseItem.objects.create(
                purchase=new_purchase,
                menu_item=menu_item,
                quantity=quantity
            )

            new_purchase.save()

            return redirect('purchase_success')
    else:
        form = PurchaseForm()
    
    return render(request, 'purchase.html', {'form': form})

