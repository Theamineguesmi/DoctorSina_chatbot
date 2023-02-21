import logging
import mimetypes
import os
import smtplib
import traceback
from email.message import EmailMessage
from email.utils import make_msgid
from pathlib import Path

logger = logging.getLogger(__name__)


def send_email(subject:str, recipient_email:str, content:str):
    try:
        message_data = EmailMessage()
        message_data["Subject"] = subject

        message_data["From"] ="amine.guesmi@esprit.tn"
        message_data["To"] = recipient_email
        this_path = Path(os.path.realpath(__file__))
        
        message_data.add_alternative(content, subtype="html")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
            smtp_server.login("amine.guesmi@esprit.tn", "mywordismypasswordX00199741")
            smtp_server.send_message(message_data)
        return True
    except Exception as error:
        logger.error(f"Error: {error}")
        logger.info(traceback.print_exc())
        return False


def get_image_data(filepath:str):
    with open(filepath, "rb") as image_data:
        maintype, subtype = mimetypes.guess_type(image_data.name)[0].split("/")
        return image_data.read(), maintype, subtype


def get_html_data(filepath:str):
    with open(filepath, "r") as html_data:
        return html_data.read()