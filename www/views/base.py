import json
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import FormView
from django.shortcuts import (render, redirect)


class ViewMixins(object):

    def redirect(self, to, permanent=False):
        return redirect(to, permanent)

    def view(self, view, model=None, content_type="text/html"):
        return render(self.request, view, model, content_type=content_type)

    def json(self, data, **kwargs):
        ''' exactly the same as render, but modified for JSON output '''

        view = json.dumps(data)

        httpresponse_kwargs = {
            'content_type': 'application/json',
            'status': kwargs.pop('status', None),
        }

        if 'context_instance' in kwargs:
            context_instance = kwargs.pop('context_instance')
            if kwargs.get('current_app', None):
                raise ValueError('If you provide a context_instance you must '
                                 'set its current_app before calling render()')
        else:
            current_app = kwargs.pop('current_app', None)
            context_instance = RequestContext(self.request, current_app=current_app)

        kwargs['context_instance'] = context_instance

        return HttpResponse(view, **httpresponse_kwargs)


class BaseView(View, ViewMixins):
    pass


class BaseFormView(FormView, ViewMixins):
    pass