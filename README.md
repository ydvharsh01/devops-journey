# System Info Script

## Project kya karta hai
Ye ek simple Python script hai jo computer ke operating system, processor architecture, aur disk space (Total, Used, Free) ki basic information fetch karke terminal par print karti hai.

## Kaise run karna hai
Is project ko run karne ke liye aapke system mein Python install hona chahiye. Terminal ya command prompt open karein aur niche di gayi command run karein:
`python system_info.py`
*(Mac/Linux users `python3 system_info.py` use karein)*

## Kaunse Python modules use kiye hain
Is script mein Python ki standard libraries ka use kiya gaya hai (alag se install karne ki zarurat nahi hai):
* **platform:** OS aur processor architecture ki details nikalne ke liye.
* **shutil:** Disk storage space check karne ke liye.