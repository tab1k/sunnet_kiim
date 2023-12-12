from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request):
        return render(request, 'main/index.html')


class AboutView(View):

    def get(self, request):
        return render(request, 'main/about.html')


class ContactView(View):

    def get(self, request):
        return render(request, 'main/contacts.html')


