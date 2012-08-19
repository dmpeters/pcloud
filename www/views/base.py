import json
from django.views.generic import View
from django.views.generic.edit import FormView
from django.shortcuts import (render, redirect)


class ViewMixins(object):

    def view(self, view, model=None, content_type="text/html"):
        return render(self.request, view, model, content_type=content_type)

    def redirect(self, to, permanent=False):
        return redirect(to, permanent)


class BaseView(View, ViewMixins):
    pass


class BaseFormView(FormView, ViewMixins):
    pass
