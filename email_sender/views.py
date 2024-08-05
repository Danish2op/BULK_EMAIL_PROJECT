
import pandas as pd
import time
import random
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmailTemplateForm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_bulk_emails(request):
    if request.method == 'POST':
        form = EmailTemplateForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['email_subject']
            body = form.cleaned_data['email_body']
            excel_file = request.FILES['excel_file']
            min_time_interval = form.cleaned_data['min_time_interval']
            max_time_interval = form.cleaned_data['max_time_interval']
            email_id = form.cleaned_data['email_id']
            app_password = form.cleaned_data['app_password']
            
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                email_body = body
                email_body = email_body.replace('VAR1', str(row['VAR1']))
                email_body = email_body.replace('VAR2', str(row['VAR2']))
                email_body = email_body.replace('VAR3', str(row['VAR3']))
                email_body = email_body.replace('VAR4', str(row['VAR4']))
                email_body = email_body.replace('VAR5', str(row['VAR5']))
                email_body = email_body.replace('VAR6', str(row['VAR6']))
                email_body = email_body.replace('VAR7', str(row['VAR7']))
                email_body = email_body.replace('VAR8', str(row['VAR8']))
                email_body = email_body.replace('VAR9', str(row['VAR9']))
                email_body = email_body.replace('VAR10', str(row['VAR10']))
                email_body = email_body.replace('VAR11', str(row['VAR11']))
                email_body = email_body.replace('VAR12', str(row['VAR12']))
                msg = MIMEMultipart()
                msg['From'] = email_id
                msg['To'] = row['VAR2']
                msg['Subject'] = subject
                msg.attach(MIMEText(email_body, 'plain'))
                
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email_id, app_password)
                text = msg.as_string()
                server.sendmail(email_id, row['VAR2'], text)
                server.quit()
                
                time.sleep(random.randint(min_time_interval, max_time_interval))  # sleep for a random time between min and max interval
            
            return HttpResponse("Emails sent successfully")
    else:
        form = EmailTemplateForm()
    return render(request, 'email_sender/email_form.html', {'form': form})



from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_email(subject, body, to_email):
    from_email = 'your_email@gmail.com'
    password = 'your_app_password'
    
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with utf-8 encoding
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error: {e}")