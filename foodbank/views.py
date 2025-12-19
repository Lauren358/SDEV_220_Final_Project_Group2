from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Inventory
from .forms import DonoForm

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

def donation(request):
    if request.method == "POST":
        form = DonoForm(request.POST)
        if form.is_valid():
            dono = form.save(commit=False)
            dono.save()
            return redirect('pantry_list')
    else:
        form = DonoForm()
        return render(request, 'foodbank/donation.html', {'form':form})
