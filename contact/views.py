from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def EmailView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            messages.success(request, 'E-postanız başarıyla bize ulaşmıştır')
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})        