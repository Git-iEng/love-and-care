from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
# from .models import Post
# from .forms import PostForm

from .forms import ContactForm

def contact_us(request):
    submitted = False
    name = ""
    email = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            name = contact.name
            email = contact.email
            submitted = True
            form = ContactForm()  # Reset the form
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {
        'form': form,
        'submitted': submitted,
        'name': name,
        'email': email
    })
def home(request):
    return render(request, 'main/index.html')

def navbar(request):
    return render(request, 'main/navbar.html')

def footer(request):
    return render(request, 'main/footer.html')

def about(request):
    return render(request, 'main/about.html')

def event(request):
    return render(request, 'main/event.html')

def project(request):
    return render(request, 'main/project.html')

def team(request):
    return render(request, 'main/team.html')

def contact(request):
    return render(request, 'main/contact.html')
