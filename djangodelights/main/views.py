from django.shortcuts import render
from .forms import IngredientForm
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

