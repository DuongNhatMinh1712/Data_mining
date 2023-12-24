from django.shortcuts import render
from django.views import View

# Create your views here.
def show_result(request):
    return "<h1> X </h1>"

class HomeView(View):
    def get(seft, request):
        return render(request, 'homepage/forms.html')