import os
os.system("mkdir ~/AOSP && cd ~/AOSP && sudo apt install repo && repo init --partial-clone --no-use-superproject -b android-latest-release -u https://android.googlesource.com/platform/manifest")
os.system("repo sync -c -j8")
print("compilings over!!!")
print("P.S. don't forget your device tree or whatever you wanna add to it, also good luck")