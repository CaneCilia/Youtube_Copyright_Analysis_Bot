import smtplib
from email.message import EmailMessage

def notify_owner(email, media_name):
    msg = EmailMessage()
    msg.set_content(f"Your media '{media_name}' may have been reused without credit.")
    msg["Subject"] = "⚠️ Copyright Alert"
    msg["From"] = "noreply@yourbot.com"
    msg["To"] = email

    # Dummy SMTP config
    with smtplib.SMTP("smtp.mailtrap.io", 587) as server:
        server.login("your_username", "your_password")
        server.send_message(msg)
