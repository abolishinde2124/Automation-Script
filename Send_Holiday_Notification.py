import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from email.mime.image import MIMEImage
# Configuration
smtp_server, smtp_port = "smtp.gmail.com", 587  # Use TLS/STARTTLS port
sender_email, sender_password = "abolishinde2124@gmail.com", "eout ypof mczn fxch"
employee_emails = ["aboli.shinde@dtskill.com"]  # Replace with employee emails
holiday_date = (datetime(datetime.now().year, 1, 27) - timedelta(days=1)).strftime("%A, %B %d, %Y") 
img_1 = r"c:\Users\Avi Shinde\Downloads\img2.jpg"
img_2 = r"c:\Users\Avi Shinde\Downloads\logo.png"
img_list = [r"c:\Users\Avi Shinde\Downloads\img2.jpg", r"c:\Users\Avi Shinde\Downloads\logo.png"]
# Email Content
subject = "Don’t Set the Alarm: Holiday Tomorrow"
email_content = f"""
Hello Team,

As we celebrate Republic Day on {holiday_date}, let us take a moment to reflect on the values of freedom, equality, and unity that define our nation. May this special day inspire us all to strive for excellence and contribute to the greater good.

Wishing you a joyful and memorable Republic Day!

Warm regards,
HR Team
"""


html = """
<html>
  <body>
    
    <img src="cid:image1" alt="Embedded Image" />
    <img src="cid:image2" alt="Embedded Image" />
  </body>
</html>
"""
def send_email(recipient):
    message = MIMEMultipart()
    message["From"], message["To"], message["Subject"] = sender_email, recipient, subject
    message.attach(MIMEText(email_content, "plain"))
    message.attach(MIMEText(html, 'html'))
    # img_list = [r"c:\Users\Avi Shinde\Downloads\th.jpeg", r"c:\Users\Avi Shinde\Downloads\th (1).jpeg"]
    for i,img_lt in enumerate (img_list): 
        with open(img_lt, 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-ID', f'<image{i + 1}>')  
            message.attach(img)
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, message.as_string())
            print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {e}")

# Send Test Email
send_email("aboli.shinde@dtskill.com")  # Replace with your email

# Send to All Employees
# for email in employee_emails:
#     send_email(email)

