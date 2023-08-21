from django.shortcuts import render, redirect
from django.views import View

class HomeView(View):
    template = 'home.html'
    
    def get(self, request):
        return render(request, self.template, {})