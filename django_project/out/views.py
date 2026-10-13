from django.shortcuts import render

# Create your views here.
def out(request):
    return render(request, 'out.html')
