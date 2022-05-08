from django.shortcuts import redirect, render
from .forms import ImageForm
from .models import Category, Product
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
  categories = Category.objects.all()
  products = Product.objects.all()

  context = {
    'products' : products,
    'categories' : categories
  }

  return render(request, "all_products.html", context)


@login_required(login_url = "user_login")
def image_upload_view(request):
  if (request.method == 'POST'):
    form = ImageForm(request.POST, request.FILES)

    if (form.is_valid()):
      form.save()
      img_obj = form.instance
      context = {
        'form' : form,
        'img_obj' : img_obj
      }

      return redirect('index')
  
  else:
    form = ImageForm()
  
  context = {
    'form' : form
  }
  
  return render(request, "add_product.html", context)


def product_detail(request, pk):
  product = Product.objects.get(pk = pk)
  
  context = {
    "product" : product
  }
  
  return render(request, "product_detail.html", context)


def category_detail(request, pk):
  category = Category.objects.get(pk = pk)
  products = Product.objects.filter(category = category)
  categories = Category.objects.all()


  context = {
    'products' : products,
    'category' : category,
    'categories' : categories
  }
  return render(request, 'category.html', context)


def search_product(request):
  if (request.method == "POST"):
    searched = request.POST['searched']
    products = Product.objects.filter(product_name__contains = searched)
    
    context = {
      "searched" : searched,
      "products" : products
    }
    
    return render(request, "search_product.html", context)
  
  else:
    pass


def select_product(request, pk):
  product = Product.objects.get(pk = pk)
  form = ImageForm(instance = product)
  
  if (request.method == "POST"):
    form = ImageForm(request.POST, instance = product)
    
    if (form.is_valid()):
      new_form = form.save(commit = False)
      new_form.choose = True
      new_form.save()
      form.save()
      return redirect("index")

  context = {
    'form' : form
  }
  
  return render(request, "selected.html", context)


def selected_product(request):
  products = Product.objects.all()
  context = {
    'products' : products
  }

  return render(request, "selected.html", context)