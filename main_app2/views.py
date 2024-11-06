from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


# Display data on our pages
# loops
# if statements
# Templating engine language

# filters
# Images
# static files
# Database