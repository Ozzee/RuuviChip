#!/bin/sh

echo "Installing dependencies"

apt-get install libbz2-dev liblzma-dev libsqlite3-dev \
libncurses5-dev libgdbm-dev zlib1g-dev libreadline-dev \
python3-pip python3-dev python3-psutil \
libssl-dev tk-dev bluetooth bluez bluez-hcidump \


pip3 install --upgrade setuptools
pip3 install ptyprocess requests ruuvitag_sensor
