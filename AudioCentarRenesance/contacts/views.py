from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def contact_page(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfuly. We will reply as fast as possible.')
            return redirect('home_page')

    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)
