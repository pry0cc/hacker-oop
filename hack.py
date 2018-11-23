import time
import requests
import progressbar

def read(url):
    return requests.get(url).text

class Hacker:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.motivation = 0
        self.crying = True
        self.progressbar = progressbar.ProgressBar(100)
        self.sleep_interval = 0.2
        self.post_hack_nap = 0.5 

    def stop_crying(self):
        self.crying = False

    def try_harder(self):
        self.motivation += 11

    @staticmethod
    def rtfm():
        return read("https://0x00sec.org/")

    @staticmethod
    def enumerate(target):
        target.increase_progress(10)
        return "Run gobuster & nmap?"

    def hack(self, target):
        print("[*] Initializing hacking against %s with hacker %s" % (target.hostname, self.name))
        self.progressbar.start()
        while not target.hacked:
            self.progressbar.update(target.hacked_progress)
            if self.motivation == 0:
                self.stop_crying()
                self.try_harder()
                self.rtfm()
            self.enumerate(target)
            time.sleep(self.sleep_interval)
        time.sleep(self.post_hack_nap)
        print("")
        print("???")
        print("Profit!")


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


target = Target("https://hackthebox.eu/")
me = Hacker("pry0cc", "0x00sec")
me.hack(target)
