from django import forms

class EmailTemplateForm(forms.Form):
    email_subject = forms.CharField(max_length=255)
    email_body = forms.CharField(widget=forms.Textarea)
    excel_file = forms.FileField()
    min_time_interval = forms.IntegerField(label="Minimum Time Interval (seconds)", min_value=0)
    max_time_interval = forms.IntegerField(label="Maximum Time Interval (seconds)", min_value=0)
    email_id = forms.EmailField(label="Your Email ID")
    app_password = forms.CharField(widget=forms.PasswordInput, label="Your App Password")
