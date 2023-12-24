from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def show_result(request):
    if request.method == 'POST':
        # Assuming requestData is passed as a query parameter
        requestData = request.GET.dict()
        print(requestData)
        # Perform your processing on the requestData here

        # For example, create a result dictionary
        result = {'status': 'success', 'message': 'Processing successful', 'data': requestData}

        # Return the result as JSON
        return HttpResponse(result)
    else:
        # Handle other HTTP methods if needed
        result = {'status': 'error', 'message': 'Invalid request method'}
        return HttpResponse(result)
@csrf_exempt
class HomeView(View):
    def get(seft, request):
        return render(request, 'homepage/forms.html')