from django.shortcuts import render
from .forms import PizzaForm

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form})
