from django.views.generic import View
from django.shortcuts import render

class BaseView(View):
    
    def view(self, view, model=None):
        return render(self.request, view, model, content_type="text/html")