import time
import requests

def read(url):
	return requests.get(url)

class Hacker:
	def __init__(self, name, team):
		self.name = name
		self.team = team
		self.motivation = 0
		self.crying = True

	def stop_crying(self):
		self.crying = False

	def try_harder(self):
		self.motivation += 11

	def rtfm(self):
		read("https://0x00sec.org/")

	def enumerate(self, target):
		target.increase_progress(10)
		return "Run gobuster & nmap?"


class Target:
	def __init__(self, hostname):
		self.hostname = hostname
		self.hacked = False
		self.hacked_progress = 0

	def increase_progress(self, amount):
		if self.hacked_progress >= 100:
			self.hacked = True
		else:
			self.hacked_progress += amount


def hack(hacker, target):
    while True:
        if hacker.motivation == 0:
            hacker.stop_crying()
            hacker.try_harder()
            hacker.rtfm()
        else:
            hacker.enumerate(target)
            if target.hacked == True:
                print("???")
                print("Profit!")
                break
        time.sleep(0)


target = Target("https://hackthebox.eu/")
me = Hacker("pry0cc", "0x00sec")
hack(me, target)
