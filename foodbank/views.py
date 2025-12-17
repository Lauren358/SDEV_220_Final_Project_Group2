from django.shortcuts import render, get_object_or_404
from .models import Inventory

# Create your views here.

def post_list(request):
    return render(request, 'foodbank/post_list.html', {})

def pantry_list(request):
    all_foods = Inventory.objects.all()
    filter_table = request.GET.get('q')

    if filter_table:
        all_foods = all_foods.filter(models.Q(name__icontains=filter_table)).distinct()

    layout = {
        'food_list': all_foods,
    }
    return render(request, 'foodbank/pantry_list.html', layout)
