import os
from socketio import socketio_manage
from status.status_socketio import StatusNamespace
from www.forms.index import ActionForm
from .base import BaseFormView
from pcloud.ioc import container



class IndexView(BaseFormView):
    form_class = ActionForm

    def get(self, request):
        return self.view('index.html')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            return super(IndexView, self).post(request, *args, **kwargs)
        else:
            return self.redirect('/')

    def form_valid(self, form):
        reciept = os.urandom(16).encode('hex') 
        form.submit(reciept)
        return self.json({"ok": True, "token": reciept})