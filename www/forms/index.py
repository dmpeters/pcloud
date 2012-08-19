from django import forms
from pcloud.tasks.actions import get_photos


class ActionForm(forms.Form):
    ig_code = forms.CharField(required=False)
    fb_code = forms.CharField(required=False)

    def submit(self):

        ig_code = self.cleaned_data['ig_code']
        fb_code = self.cleaned_data['fb_code']

        get_photos.delay(instagram=ig_code, facebook=fb_code)