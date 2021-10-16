import os
print("you need to root your phone")
print()
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/ABIRHOSSAIN10/OneShot_Termux_installer")

os.system("cd ..;chmod +x OneShot/oneshot.py")

print("Now Go To Home Directory[~] And Enter This Command :\nsudo python OneShot/oneshot.py -i wlan0 -K")
