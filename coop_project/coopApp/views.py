from django.shortcuts import render

# Create your views here.
def showCoopApp(request):
    return render(request, 'CoopApp/Apptemp.html')
