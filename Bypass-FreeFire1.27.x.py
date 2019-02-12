from os import system
from urllib.request import urlopen
from urllib.request import Request
import json
from time import sleep

login=False

def title():
	system("clear")
	system("figlet RedSHADOW")
def getJson(jsonstr):
	j=json.load(jsonstr)
	return j
def login():
	title()
	u=input("ชื่อผู้ใช้ : ")
	p=input("รหัสผ่าน : ")
	url="https://np2544.tk/redshadow/checkLogin.php?u="+u+"&p="+p
	h={
		"User-Agent":"RedSHADOW"
	}
	rq=Request(url,headers=h)
	print("กำลังเข้าสู่ระบบ....")
	g=urlopen(rq)
	get=g.read().decode("utf-8")
	data=json.loads(get)
	if data["status"]=="200":
		print("ล็อกอินสำเร็จ ✓")
		sleep(1.5)
		main()			
	elif data["status"]=="401":
		print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
		sleep(1.5)
		login()
def welcome():
	title()
	print("\n\n	[1] -> เมนูหลัก")
	print("\n\n	[2] -> ออก\n\n")
	g=input("เลือก : ")
	if g=="1":
		login()
	elif g=="2" or g=="exit":
		system("exit")

def writeStatus(s):
	f=open("s","w")
	f.write(s)
	f.close()

def main():
	title()
	print("บายพาสป้องกันเกมเด้ง Free Fire 1.27.x")
	try:
		f=open("s","r")
		s=f.read()
		f.close()
		if s=="1":
			print("   <<สถานะการบายพาส : เปิด>>")
		elif s=="0":
			print("   <<สถานะการบายพาส : ปิด>>")
	except:
		print("   <<สถานะการบายพาส : ปิด>>")
	print("\n\n	[1] -> เปิด")
	print("\n\n	[2] -> ปิด")
	print("\n\n	[exit] -> ออกจากโปรเเกรม")
	g=input("\n\nเลือก : ")
	if g=="3":
		os.exit()
	elif g=="1":
		writeStatus("1")
		main()
	elif g=="2":
		writeStatus("0")
		main()
	


welcome()
    