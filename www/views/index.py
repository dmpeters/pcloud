from www.forms.index import ActionForm
from .base import BaseFormView
from pcloud.ioc import container


class IndexView(BaseFormView):
    form_class = ActionForm

    def get(self, request):
        return self.view('index.html')

    def form_valid(self, form):
        form.submit()
        return self.view('index.html')
