from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect 
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy 
from .models import Inventory
from .forms import DonoForm
from django.contrib.auth.forms import UserCreationForm
from foodbank import models 
from django.views.generic import CreateView
from .forms import TakeForm
from django.http import HttpResponse

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
    
    def take(request):
    if request.method == "POST":
        form = TakeForm(request.POST)
        if form.is_valid():
            take = form.save(commit=False)
            take.save()
            return redirect('pantry_list')
    else:
        form = TakeForm()
        return render(request, 'foodbank/take_donation.html', {'form':form})


def food_taken(self, food_name, food_total):
        if food_total > 0:
            take = Take.objects.create(name=self.request.user, food_name=food_name, food_total=food_total)
            take.save()
            food_total = food_total - food_total
            food_total.save()
            return HttpResponse("Food taken successfully!")
        else:
            return HttpResponse("None available at this time, please try again later.")



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


