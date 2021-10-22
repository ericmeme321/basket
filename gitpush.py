import os
import datetime

today = datetime.datetime.today().strftime("%Y%m%d")

os.system("git add .")
os.system(f"git commit -m {today}")
os.system("git push origin master")