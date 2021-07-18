import requests
from sys import argv
from termcolor import colored
import colorama
colorama.init()

try:
	url = argv[1]
except IndexError:
	print("ADDRESS => !")
	print("python scanner.py http://ADRES")
	exit()

print(">>> Skanowanie strony: " + url)

with open("dict.txt", "r") as f:
	all_page = f.readlines()
	for i, podstrona in enumerate(all_page):
		podstrona = podstrona.strip()
		if not "# " in podstrona and podstrona != "#" and len(podstrona) > 0:
			try:
				if i % 50 == 0:
					print(f"{round(i/len(all_page)*100, 2)}%        ", end="\r")

				r = requests.get(url + podstrona)
				if r.status_code == 404:
					raise Exception()
				
				col = "green"
				if r.status_code == 503:
					col = "red"
				elif r.status_code == 403:
					col = "yellow"

				print(url + podstrona + ":", colored(str(r.status_code), col))
			except KeyboardInterrupt:
				exit()
			except:
				pass # not found the page
                print("NOT FOUND THE PAGE")
print(">>> End of SCANNING!")