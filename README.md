# RuuviTag to Grafana

Send [RuuviTag](https://ruuvi.com/) data to Grafana.


## Install dependencies

Switch to root

```
sudo su
```

Install dependencies

```
apt-get install libbz2-dev liblzma-dev libsqlite3-dev \
libncurses5-dev libgdbm-dev zlib1g-dev libreadline-dev \
python3-pip python3-dev python3-psutil \
libssl-dev tk-dev bluetooth bluez bluez-hcidump


pip3 install --upgrade setuptools
pip3 install ptyprocess requests ruuvitag_sensor
```

Edit the `ruuvi.py` script to include the correct InfluxDB host and update interval

Test the script

```
python3 ruuvi.py
```

Copy the `ruuvi_start.sh` and `ruuvi.py` to `/root/`

```
cp ruuvi_start.sh ruuvi.py /root/
```

Make the script start after reboot by adding it to root's crontab: `crontab -e`

```
@reboot /root/ruuvi_start.sh
```

Finally reboot to apply all the changes


# Sources

* https://github.com/ttu/ruuvitag-sensor

# License

Licensed under the [MIT License](LICENSE).

