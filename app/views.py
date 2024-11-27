from django.shortcuts import render, redirect
from app.models import Dog, Adopter
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from app.forms import AdoptationForm

# Create your views here.
def index(request):
    dogs = Dog.objects.all()[:4]
    image = Dog.objects.all()[0]
    context = {"dogs": dogs, "image":image}
    return render(request, 'app/index.html', context)

def detail_page(request, slug):
    dog = Dog.objects.get(slug=slug)
    user = request.user
    existing_adopter = Adopter.objects.filter(adopted_dogs=dog).exists()
    if existing_adopter:
        already_adopted = True
    else:
        already_adopted = False
    msg = ''
    if request.method == 'POST':
        form = AdoptationForm(request.POST)
        if form.is_valid():
            adopter = form.save(commit=False)
            adopter.user = request.user
            adopter.adopted_dogs = (dog)
            adopter.save()
            return redirect('detail_page', slug=slug)
        else:
            msg='not valid'
    else:        
        form = AdoptationForm()
    context = {"dog":dog,'form':form, 'msg':msg, 'already_adopted':already_adopted}
    return render(request, "app/details.html", context)

def about(request):
    return render(request, 'app/about.html')


def contact(request):
    return render(request, 'app/contact.html')

def gallery(request):
    breed_query = request.GET.get('breed','')
    if breed_query:
        dogs =  Dog.objects.filter(breed__icontains = breed_query)
    else:
        dogs = Dog.objects.all()
    return render(request, 'app/gallery.html',{"dogs":dogs,"breed_query":breed_query})


    

def signupuser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {"form":form}
    return render(request, 'app/registration.html', context)

def loginuser(request):
    msg = ''
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
            
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            msg = "user doesn't exist"
    else:
        form = AuthenticationForm()
        
    context = {"form": form, "msg":msg}
    return render(request, 'app/login.html', context)

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')