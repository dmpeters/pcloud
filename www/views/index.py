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
        form.submit()
        return self.view('receipt.json',
                         {"status": "true", "token": "12335"},
                         content_type="application/json")
