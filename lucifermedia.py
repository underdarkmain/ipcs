#Jangan ganti author , hargai creator cape loh buat nya

import LIST
from LIST.id import *
from LIST.it import *
from LIST.jp import *
from LIST.us import *
from LIST.fr import *
from LIST.kr import *
from LIST.de import *
from LIST.tr import *
import requests,re,os

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"



def main():
    os.system('clear')
    print("{}        ____ ").format(r)
    print("   _[]_/____\__n_ ")
    print("  |_____.--.__()_|")
    print("  |Lu   //# \\\    |")
    print("{}  |CI   \\\__//    | ").format(w)
    print("  |Fer   '--'     | ")
    print("{}  '--------------'----------{}------------------.  ").format(r,w)
    print("{}  | {}Gelistirici  : {}XluciferX {}     | {}LUCIFER{}CAMERA{}{}HACKER         | ").format(r,w,r,w,r,ir,reset,w)
    print("{}  | {}Youtube : {}Under_DarK {}| {}http://lucifermedia.tr.ht {}|").format(r,w,w,w,lgray,w)
    print("{}  '------------------------------------{}-------'  ").format(r,w)
    print ("  {}[ 1 ] {}Turkiye").format(r,w)
    print ("  {}[ 2 ] {}Italya").format(r,w)
    print ("  {}[ 3 ] {}Endonezya").format(r,w)
    print ("  {}[ 4 ] {}Japonya").format(r,w)
    print ("  {}[ 5 ] {}Amerika").format(r,w)
    print ("  {}[ 6 ] {}Fransa").format(r,w)
    print ("  {}[ 7 ] {}Kore").format(r,w)
    print ("  {}[ 8 ] {}Almanya").format(r,w)
    print ("  {}[ 9 ] {}Iptal").format(r,w)
    print ""
    select = input("\033[1;31m[ \033[1;37mSelect@Number \033[1;31m]\033[1;37m> ")
    filtering(select)



def filtering(pilih):
    if pilih == 2:
        italy()
    elif pilih == 3:
        indonesia()
    elif pilih == 4:
        japan()
    elif pilih == 5:
        unitedstates()
    elif pilih == 6:
        france()
    elif pilih == 7:
        korea()
    elif pilih == 8:
        german()
    elif pilih == 1:
        turkey()
    elif pilih == 9:
        print (r+"Iptal Ediliyor ..."+w)
        os.sys.exit()
    else:
        print (r+"Iptal Ediliyor ..."+w)
        os.sys.exit()

if __name__ == '__main__':
    main()
