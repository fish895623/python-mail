import argparse
import smtplib
import sys
from email.mime.text import MIMEText

import yaml

parser = argparse.ArgumentParser()
parser.add_argument("-t", type=str, help="Title")
parser.add_argument("-f", type=str, required=True, help="string to send")
args = parser.parse_args()

with open("config.yml") as config:
    msg = MIMEText(args.f)
    msg["Subject"] = args.t
    config = yaml.load(config, Loader=yaml.FullLoader)
    s = smtplib.SMTP(config["SMTP_SERVER"], config["SMTP_PORT"])
    s.starttls()
    s.login(config["SENDER"], config["TOKEN"])
    s.sendmail(config["SENDER"], config["RECEIVER"], msg.as_string())
    s.quit()
