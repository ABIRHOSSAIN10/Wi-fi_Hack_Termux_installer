## Termux installation 

## Full cradit

https://github.com/drygdryg

### Setup
```
$ pkg update && pkg upgrade

$ pkg install git python

$ git clone https://github./ABIRHOSSAIN10/OneShot_Termux_installer

$ cd OneShot_Termux_installer

$ python Installer.py

```
### Run
Disable Wi-Fi in the system settings and run:
```
sudo python OneShot/oneshot.py -i wlan0 -K
```
### How to update OneShot
To check for updates and update, run the following command:
```
(cd OneShot && git pull)
```
