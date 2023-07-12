from django.shortcuts import render

# Create your views here.

''' The view declaration to invoke the request to render the template url '''
def list(request):
    return render(request, 'todofrontend/list.html')
