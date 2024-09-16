import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import datetime

# Employee data with birthdays and email addresses
employees = [
    {"name": "Aboli", "birthday": "2024-09-12", "email": "aboli.shinde@dtskill.com"},
]

# Function to send a birthday email
def send_birthday_email(to_email, to_name):
    sender_email = "abolishinde2124@gmail.com"  # Your email address
    sender_password = "eout ypof mczn fxch"  # Your app-specific password
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    msg = MIMEMultipart('related')
    msg['Subject'] = "Happy Birthday!"
    msg['From'] = sender_email
    msg['To'] = to_email

    # Email body with HTML content
    html = f"""
    <html>
    <body>
        <p>Dear {to_name},</p>
        <p>Wishing you a very happy birthday and a year filled with success and growth! 🎉</p>
        <p>Best Regards,<br>DTskill Inc</p>
        <img src="cid:image1" alt="DTskill Logo" />
    </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))

    # Attach the image
    with open(r'c:\Users\Avi Shinde\Downloads\img5.gif', 'rb') as img:
        img_data = img.read()
    image = MIMEImage(img_data, name='Happy-Birthday-Bouquet-Images.jpg')
    image.add_header('Content-ID', '<image1>')
    msg.attach(image)

    # Sending the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
            print(f"Sent Happy Birthday email to {to_name}")
    except Exception as e:
        print(f"Failed to send email to {to_name}. Error: {e}")

# Check birthdays and send emails
today = datetime.date.today().strftime('%Y-%m-%d')
for employee in employees:
    if employee["birthday"] == today:
        send_birthday_email(employee["email"], employee["name"])

