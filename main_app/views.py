from django.shortcuts import render

dogs = [
  {'name': 'Chopin', 'breed': 'yorkshire terrier', 'description': 'cute, hairy, little, spoiled demon', 'age': 8},
  {'name': 'Duke', 'breed': 'border collie', 'description': 'energetic furball', 'age': 12},
  {'name': 'Lily', 'breed': 'chihuahua dotson', 'description': 'sweet but rowdy', 'age': 2},
  {'name': 'Po', 'breed': 'chihuahua dotson', 'description': 'shy and gentle', 'age': 2},
  {'name': 'Louie', 'breed': 'chihuahua dotson', 'description': 'old man vibes but very playful', 'age': 3},
  {'name': 'Monty', 'breed': 'chihuahua', 'description': 'looks crazy cause he is crazy', 'age': 3},
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