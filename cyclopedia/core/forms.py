from django import forms


# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = Entry
#         fields = "__all__"

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()