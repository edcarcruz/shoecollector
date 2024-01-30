from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Shoe:
  def __init__(self, name, color, description, material, image):
    self.name = name
    self.color = color
    self.description = description
    self.material = material
    self.image = image

shoes = [
  Shoe('Cortez', 'red', 'Classic Cortez', 'suede','https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/amnnjjrhg2krih3k0tdd/nike-classic-cortez-premium-red-orbit-white-black-release-date.jpg'),
  Shoe('Dunk', 'blue', 'Classic Dunk', 'leather', 'https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/9f5d3ab4-98b4-44fe-9823-3b409603b520/dunk-low-retro-shoes-p6gmkm.png'),
  Shoe('Chuck Taylor', 'black', 'Classic Converse Shoe', 'canvas', 'https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/tgttyejtnd29yz3nbr4p/converse-chuck-taylor-all-star-low-top-unisex-shoes-NLRAok.png'),
  Shoe('Cortez', 'white', 'Classic Cortez', 'suede', 'https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/yi9yjnvjqfx3qkcuu6eb/nike-cortez-all-white.jpg'),
]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def shoes_index(request):
  return render(request, 'shoes/index.html', { 'shoes': shoes })
