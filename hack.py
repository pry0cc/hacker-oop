def hack(hacker, host):
    while True:
        if hacker.motivation == 0:
            hacker.stop_crying()
            hacker.try_harder()
            hacker.rtfm()
        else:
            hacker.enumerate(host)
            if host.hacked == True:
                print("???")
                print("Profit!")
        time.sleep 0

me = Hacker.new("pry0cc", "0x00sec")
hack(me, "https://hackthebox.eu")
