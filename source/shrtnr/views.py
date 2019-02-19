from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views import View

from .forms import SubmitURLForm
from .models import PnplURL



# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        url_form = SubmitURLForm()
        content = {
            'title': "Pnpl URL Shrtnr",
            'form': url_form
        }
        return render(request, 'shrtnr/home.html', content)

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        content = {
            'title': "Pnpl Shrtnr",
            'form': form
        }
        template = 'shrtnr/home.html'
        if form.is_valid():
            submited_url = form.cleaned_data.get('url')
            if not 'http' in submited_url:
                pn_url = 'http://' + submited_url
            else:
                pn_url = submited_url
            obj, created = PnplURL.objects.get_or_create(url=pn_url)
            content = {
                'object': obj,
                'created': created,
            }   
            if created:
                template = 'shrtnr/success.html'
            else:
                template = 'shrtnr/already-exists.html'
        return render(request, template, content)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shrtnr/about.html')

class PnplCBV(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(PnplURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)