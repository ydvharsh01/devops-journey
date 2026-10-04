import platform # give detail of OS and hardware 
# NAme of os platform.system()
#OS version platform.release()
# process architucture platform.machine()
import shutil # info about dick storage 
#totle use and free space of disk  shutil.disk_usage()
# But data in the form of byte here ans/(1024 ** 3)
import datetime # added new module for showing date and time 

print("=====system info=====")
# current date aund time 
now = datetime.datetime.now()

print(f"current date/time: {now.strftime('%y-%m-%d %H:%M:%S')}")

print(f"OS Name: {platform.system()}")
print(f"OS Version: {platform.release()}")
print(f"Process Architecture: {platform.machine()}")

print("=====Disk info=====")
# Window ke liye C: AUR baki sabhi OS ke liye "/" (root) ka use karenge 
path = "C:\\" if platform.system() == "Windows" else "/"
total, used, free = shutil.disk_usage(path)

#convert bytes to GB
gb = (1024 ** 3)
print(f"Total Disk Space: {total/gb:.2F} GB")
print(f"Used Disk Space: {used/gb:.2F} GB")
print(f"Free Disk Space: {free/gb:.2F} GB")





