import smtplib
import yaml
import sys

with open("config.yml") as config:
    config = yaml.load(config, Loader=yaml.FullLoader)
    s = smtplib.SMTP(config['SMTP_SERVER'], config['SMTP_PORT'])
    s.starttls()
    s.login(config["SENDER"], config['TOKEN'])
    s.sendmail(config["SENDER"], config["RECEIVER"], sys.argv[1])
    s.quit()
