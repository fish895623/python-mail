#!/usr/bin/env python
import argparse
import smtplib
from email.mime.text import MIMEText

import yaml

parser = argparse.ArgumentParser()
parser.add_argument("-T", type=str, help="Title")
parser.add_argument("-F", type=str, required=True, help="string to send")
parser.add_argument("--config", type=str, required=True, help="config location")
args = parser.parse_args()

with open(args.config) as config:
    msg = MIMEText(args.F)
    msg["Subject"] = args.T
    config = yaml.load(config, Loader=yaml.FullLoader)
    s = smtplib.SMTP(config["SMTP_SERVER"], config["SMTP_PORT"])
    s.starttls()
    s.login(config["SENDER"], config["TOKEN"])
    s.sendmail(config["SENDER"], config["RECEIVER"], msg.as_string())
    s.quit()
