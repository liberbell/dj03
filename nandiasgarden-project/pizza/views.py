from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def order(request):
    return render(request, 'pizza/order.html')
