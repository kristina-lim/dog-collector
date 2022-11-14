from django.shortcuts import render

dogs = [
  {'name': 'Chopin', 'breed': 'yorkshire terrier', 'description': 'cute, hairy, little, spoiled demon', 'age': 8},
  {'name': 'Duke', 'breed': 'border collie', 'description': 'energetic furball', 'age': 12},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })