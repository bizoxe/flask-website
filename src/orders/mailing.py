"""
This module contains helper functions for sending a message with order details to the makeup artist's mailbox.
"""

import datetime
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any

from flask import current_app

from src.orders.forms import OrderForm


def prepare_order_message(
    order_data: dict[str, Any],
    mail_subject: str,
    mail_from: str,
    mail_to: str,
) -> MIMEMultipart:
    mail = MIMEMultipart("alternative")
    mail["Subject"] = mail_subject
    mail["From"] = mail_from
    mail["To"] = mail_to

    current_day = datetime.datetime.now().day
    current_time = datetime.datetime.now().hour
    if order_data["date"].day == current_day and order_data["time"].hour == current_time:
        order_data["date"] = "не задано"
        order_data["time"] = "не задано"
    if issubclass(type(order_data["time"]), datetime.time):
        order_data["time"] = order_data["time"].strftime("%H:%M")
    msg_string = ""
    for key, value in order_data.items():
        if key != "csrf_token":
            msg_string += f"{key} : {value}{'<br>'}"

    msg_html = f"<html><head></head><body>{msg_string}</body></html>"
    mail.attach(MIMEText(msg_html, "html"))

    return mail


def send_email(form: OrderForm) -> bool:
    smtp_server = current_app.config["SMTP_SERVER_NAME"]
    port = current_app.config["SMTP_PORT"]
    sender_email = current_app.config["MAIL_SENDER"]
    receiver_email = current_app.config["MAIL_RECIPIENT"]
    password = current_app.config["SMTP_PASSWORD"]
    subj_message = current_app.config["MAIL_SUBJECT"]
    order_data = form.data
    message = prepare_order_message(
        order_data=order_data,
        mail_subject=subj_message,
        mail_from=sender_email,
        mail_to=receiver_email,
    )

    context = ssl.create_default_context()
    server = None
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg=message, from_addr=sender_email, to_addrs=receiver_email)
        return True
    except Exception as e:
        current_app.logger.error("Failed to send an e-mail: %s", e)
    finally:
        if server is not None:
            server.quit()

    return False
