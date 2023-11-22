from django import forms


class CSVImortForm(forms.Form):
    csv_file = forms.FileField()
