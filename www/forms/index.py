from django import forms


class ActionForm(forms.Form):
    ig_code = forms.CharField(required=False)
    fb_code = forms.CharField(required=False)

    def submit(self):
        ig_code = self.cleaned_data['ig_code']
        fb_code = self.cleaned_data['fb_code']

        # task it up!
        #print(self.fb_code)
        # send email using the self.cleaned_data dictionary

