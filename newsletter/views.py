from django.shortcuts import render
from .forms import SignUpForm, ContactForm


# Create your views here.


def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)

    context = {
        'title': title,
        'form': form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        my_full_name = form.cleaned_data.get('full_name')
        my_email = form.cleaned_data.get('email')

        print(my_full_name)
        print(my_email)

        instance.save()

        context = {
            'title': 'Thank You'
        }

    return render(request, "newsletter/home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        for key, value in form.cleaned_data.items():
            print(key, value)
        # email = form.cleaned_data.get('email')
        # full_name = form.cleaned_data.get('full_name')
        # message = form.cleaned_data.get('message')

    context = {
        'form': form,
    }

    return render(request, 'newsletter/contact.html', context)
