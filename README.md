# C.H.I.P + RuuviTag temperature sensors

I use [RuuviTags](https://ruuvi.com/) to monitor the temerature at home, but unfortunately the bluetooth radio broke on my previous setup. Fortunately I happened to have a C.H.I.P computer lying around. Apparently the company has gone bust, but the device works and has a bluetooth radio.

## Set up C.H.I.P

Connect the C.H.I.P to a Linux computer using a micro usb cable. (macOS might work as well)
 
Find the right tty:
```
dmesg | tail
```

Look for a line like: 
```
[ 3815.617128] cdc_acm 3-1:2.0: ttyACM0: USB ACM device
```

Use `screen` to connect to the device:
```
sudo screen /dev/ttyACM0
```

The default user is `root` and the default password is `chip`. 

Change the password using `passwd`

Connect to wifi using `nmtui`. It will open a console UI.

Install ssh and git: `apt-get install ssh git`

Now you can connect to the C.H.I.P with ssh instead of the usb cable.

## TODO