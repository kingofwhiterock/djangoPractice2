from django.shortcuts import render


# Create your views here.
def signup_view(request):
    context = {'data1': 100}
    return render(request, 'signup.html', context)
