from django.shortcuts import render, redirect
from .models import Shoe
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Add the following import
from django.http import HttpResponse
from .forms import PurchaseForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def shoes_index(request):
  shoes = Shoe.objects.all()
  return render(request, 'shoes/index.html', { 'shoes': shoes })

def shoes_detail(request, shoe_id):
  shoe = Shoe.objects.get(id=shoe_id)
  purchase_form = PurchaseForm()
  return render(request, 'shoes/detail.html', { 'shoe': shoe, 'purchase_form': purchase_form })

def add_purchase(request, shoe_id):
  # create the ModelForm using the data in request.POST
  form = PurchaseForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_purchase = form.save(commit=False)
    new_purchase.shoe_id = shoe_id
    new_purchase.save()
  return redirect('detail', shoe_id=shoe_id)

class ShoeCreate(CreateView):
  model = Shoe
  fields = '__all__'
  
class ShoeUpdate(UpdateView):
  model = Shoe
  fields = '__all__'
  
class ShoeDelete(DeleteView):
  model = Shoe
  success_url = '/shoes/'