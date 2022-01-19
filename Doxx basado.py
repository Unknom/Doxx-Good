#created by Archxty
import sys, os, webbrowser, platform, subprocess

import webbrowser

def __limpiar():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')
def menu():
	__limpiar()

	print """
\033[1;31m                                ____            _
\033[1;31m                              
\033[1;37m                          
\033[1;37m                              
\033[1;31m                             
\033[1;31m                                                     

"""
	print '''
\033[1;33m 1. IP 	      \033[1;33m 7. Dateas      
\033[1;33m 2. Dni	 	  \033[1;33m 8. Tineye        
\033[1;33m 3. EstCiv      \033[1;33m 9. Pipl           
\033[1;33m 4. Operadora   \033[1;33m 10. Osintfrant     
\033[1;33m 5. Troyanos    \033[1;33m 11. ExifData      
\033[1;33m 6. Correo    \033[1;33m 12. Acreditacion
		'''
	d = raw_input("\033[1;30m Doxing > ")

	if d == "1":
		webbrowser.open('https://www.ip-adress.com/')

		menu()
	elif d == "2":
		webbrowser.open('http://www.consultadni.info/')
		menu()
	elif d == "3":
		webbrowser.open('https://cel.reniec.gob.pe/valreg/valreg.do')
		menu()
	elif d == "4":
		webbrowser.open('https://www.revealname.com/')
		menu()
	elif d == "5":
		webbrowser.open('https://mega.nz/file/a08X2ALS#vjgrtfeZpYj2ENv0sAWwP__J1lFFZzGrE8Ay88XMPTU')
		menu()
	elif d == "6":
		webbrowser.open('https://anonymousemail.me/')
		menu()
	elif d == "7":
		webbrowser.open('https://www.dateas.com/')
		menu()
	elif d == "8":
		webbrowser.open('https://tineye.com/')
		menu()
	elif d == "9":
		webbrowser.open('https://pipl.com/')
		menu()
	elif d == "10":
		webbrowser.open('https://osintframework.com/')
		menu()
	elif d == "11":
		webbrowser.open('http://exifdata.com')
		menu()
	