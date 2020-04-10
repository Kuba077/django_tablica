from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, DeleteView

from tablica.forms import PostForm
from tablica.models import Post


@login_required
def dodaj_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            p = Post(tresc=form.cleaned_data['tresc'])
            p.uzytkownik = request.user
            p.data_dodania = timezone.now()
            p.save()
            messages.success(request, "Dodano post!")
            return redirect(reverse("tablica:post_lista"))
    else:
        form = PostForm()
    kontekst = {
        'form': form
    }
    return render(request, 'tablica/post_dodaj.html', kontekst)


class ListaPostow(ListView):
    model = Post
    context_object_name = "posty"
    template_name = "tablica/index.html"
    ordering = ["-data_dodania"]


class UsunPost(SuccessMessageMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("tablica:post_lista")
    success_message = "Usunięto post!"
