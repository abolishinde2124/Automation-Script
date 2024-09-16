import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime, timedelta
import os

# List of employees with their start dates and email addresses
employees = [
    {"name": "Aboli", "start_date": "2023-09-14", "email": "aboli.shinde@dtskill.com"},
]

# Function to send a one-year anniversary email with an image
def send_anniversary_email(to_email, to_name):
    sender_email = "abolishinde2124@gmail.com"  # Your email address
    sender_password = "eout ypof mczn fxch"  # Your app-specific password
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    msg = MIMEMultipart('related')
    msg["Subject"] = "Happy One-Year Anniversary!"
    msg["From"] = sender_email
    msg["To"] = to_email

    # Email body with HTML content
    html = f"""
    <html>
    <body>
        <p>Dear {to_name},</p>
        <p>Congratulations on completing one year with us! 🎉 Your contributions are truly appreciated. Here’s to many more great years together! 🎉</p>
        <p>Best Regards,<br>DTskill Inc</p>
        <img src="cid:image1" alt="Anniversary Image" />
    </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))

    # Attach an image
    image_path = r"c:\Users\Avi Shinde\Downloads\OneYearCompletion.jpg"  # Update this path to your image file
    try:
        with open(image_path, "rb") as img_file:
            img_data = img_file.read()
        image = MIMEImage(img_data, name=os.path.basename(image_path))
        image.add_header('Content-ID', '<image1>')
        msg.attach(image)
        print("Image attached successfully.")
    except FileNotFoundError:
        print(f"Image file {image_path} not found. Skipping image attachment.")
    except Exception as e:
        print(f"Error attaching image: {e}")

    # Sending the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
            print(f"Sent one-year anniversary email to {to_name}")
    except Exception as e:
        print(f"Failed to send email to {to_name}. Error: {e}")

# Check anniversaries and send notifications
today = datetime.now().date()
for employee in employees:
    start_date = datetime.strptime(employee["start_date"], "%Y-%m-%d").date()
    one_year_anniversary = start_date + timedelta(days=365)
    
    # Debugging output to check dates
    print(f"Today's date: {today}, Checking anniversary for {employee['name']} on {one_year_anniversary}")
    
    if today == one_year_anniversary:
        send_anniversary_email(employee["email"], employee["name"])
    else:
        print(f"No anniversary today for {employee['name']}")


