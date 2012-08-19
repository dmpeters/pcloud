from django import forms
from pcloud.tasks.actions import get_photos


class ActionForm(forms.Form):
    ig_code = forms.CharField(required=False)
    fb_code = forms.CharField(required=False)

    def submit(self, receipt):
        ig_code = self.cleaned_data['ig_code']
        fb_code = self.cleaned_data['fb_code']
        get_photos.delay(receipt, instagram=ig_code, facebook=fb_code)
        