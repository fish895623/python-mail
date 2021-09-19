# mail

This is Python email script

`config` file layout

``` yaml
TOKEN: __app_password__
SENDER: __send_email__
RECEIVER: __reciever__
SMTP_SERVER: smtp.gmail.com
SMTP_PORT: 587
```

## usage

To send email,

``` bash
./app.py -T "__email_title__" -F "__Text_Contents__" --config __full_config_path__
```

``` sh
usage: app.py [-h] [-T T] -F F --config CONFIG

optional arguments:
  -h, --help       show this help message and exit
  -T T             Title
  -F F             string to send
  --config CONFIG  config location
```

## TODO

* Add how to create google email app password
