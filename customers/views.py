from django.shortcuts import render

from .forms import CustomerForm

from .models import Customer
# Create your views here.

def customer_create_view(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerForm()  
    context = {
        'form': form
    } 
    return render(request, "customers/customer_create.html", context)