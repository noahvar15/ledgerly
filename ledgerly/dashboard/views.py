from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html', {})

def analytics(request):
    return render(request, 'dashboard/analytics.html', {})