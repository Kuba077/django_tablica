from django.shortcuts import render
# Create your views here.
from django.utils import timezone
from django.views.generic import ListView

from tablica.forms import PostForm
from tablica.models import Post


def dodaj_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            p = Post(tresc=form.cleaned_data['tresc'])
            p.uzytkownik = request.user
            p.data_dodania = timezone.now()
            p.save()
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
