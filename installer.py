import os
print("you need to root your phone")
print()
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/ABIRHOSSAIN10/WIFI-HACK")

os.system("cd ..;chmod +x WIFI-HACK/oneshot.py")

print("Enter This Command :\nsudo python WIFI-HACK/oneshot.py -i wlan0 -K")
