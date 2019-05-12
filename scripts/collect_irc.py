#!/usr/bin/env python

import os, sys, socket, time, datetime

networks = {
    "Freenode": ("chat.freenode.net",6667),
    "SpotChat": ("irc.spotchat.org",6667),
    "EFNet": ("irc.underworld.no",6667),
    "OFTC": ("irc.oftc.net",6667)
}

freenode_channels = [
        '#archlinux',
        '#ubuntu',
        '#debian',
        '#gentoo',
        '#freebsd',
        '#nixos',
        '#openbsd',
        '#fedora',
        '#ZorinOS',
        '#pfsense',
        '#centos',
        '#kali-linux',
        '#freenas',
        '#coreos',
        '#suse',
        '#antiX',
        '#lxle',
        '#parrotsec',
        '#PCLinuxOS',
        '#deepin',
        '#puppylinux',
        '#raspbian',
        '#alpine-linux',
        '#android-x86',
        '#qubes_os',
        '#rhel',
        '##proxmox',
        '#devuan',
        '#NetBSD',
        '#smartos',
        '#voidlinux',
        '#illumos',
        '#kubuntu',
        '##slackware',
        '#Solus',
        '#freeswitch',
        '#reactos',
        '#guix',
        '#vyos',
        '#freepbx',
        '#antergos',
        '#funtoo',
        '#haiku',
        '#OPNsense',
        '#manjaro',
        '#openindiana',
        '#xubuntu',
        '#kde-neon',
        '#retropie',
        '#omnios',
        '#exherbo',
        '#parabola',
        '#ubuntu-mate',
        '#ubuntu-budgie',
        '#ubuntustudio',
        '#archbang',
        '#archlabslinux',
        '#knoppix',
        '#lakka',
        '#redcorelinux',
        '#libreelec',
        '#UltimateEdition',
        '#nutyx',
        '#korora',
        '##slax',
        '#bodhi',
        '#blackarch',
        '#mageia',
        '#lubuntu',
        '#openmandriva',
        '#calculate',
        '##oraclelinux',
        '#clonezilla',
        '#vectorlinux',
        '#pcbsd',
        '#minix',
        '#elive',
        '#morphos',
        '#trueos',
        '#sabayon',
        '#nas4free',
        '#pentoo',
        '#galliumos',
        '#opensolaris',
        '#elementary',
        '#trisquel',
        '#chakra',
        '#mirbsd',
        '#steamOS',
        '#hyperbola',
        '#endless',
        '#kaosx',
        '#crux'
]

distro_map = {}

class IRC:
    network = ""
    botnick = "distrobot"
    irc = socket.socket()

    def __init__(self,network):
        self.network = network
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostport = networks[network]
        self.connect(hostport[0],hostport[1])

    def connect(self,server,port):
        self.irc.connect((server,port))
        self.irc.send("USER " + self.botnick + " " + self.botnick +" " + self.botnick + " :This is a distroratings bot!\n")
        self.irc.send("NICK " + self.botnick + "\n")
        data = self.irc.recv(8048)
        while data != None:
            sys.stdout.write(data)
            if "376" in data:
                break
            data = self.irc.recv(8048)

    def close(self):
        self.irc.send("QUIT :exiting!\n")
        self.irc.close()

    def identify(self,password):
        self.irc.send("PRIVMSG NickServ :IDENTIFY " + self.botnick + " " + password + "\n")
        time.sleep(2)
        data = self.irc.recv(8048)
        sys.stdout.write(data)
        time.sleep(2)
        data = self.irc.recv(8048)
        sys.stdout.write(data)

    def get_channel(self,channel):
        self.irc.send("JOIN "+channel+"\n")
        data = self.irc.recv(8048)
        c = 0
        while data != None:
            if data.endswith("\r\n"):
                lines = data.split("\r\n")
                for line in lines:
                    if line == '':
                        continue
                    line = line.split(" ")
                    if line[1] == "353":
                        c += len(line)-6
                    if line[1] == "366":
                        data = None
                        break
                if data == None:
                    break
                data = ""
            data += self.irc.recv(8048)
        self.irc.send("PART "+channel+"\n")
        distro_map[channel+" on "+self.network] = int(c)

    def get_list(self,keys):
        self.irc.send("LIST\n")
        data = self.irc.recv(8048)
        while data != None:
            if data.endswith("\r\n"):
                lines = data.split("\r\n")
                for line in lines:
                    if line == '':
                        continue
                    line = line.split(" ")
                    code = line[1].strip()
                    if code == "323":
                        data = None
                    elif code == "322":
                        try:
                            channel = line[3].strip()
                            participants = int(line[4].strip())
                            if channel in keys:
                                distro_map[channel+" on "+self.network] = participants
                        except:
                            print line
                if data == None:
                    break
                data = ""
            data += self.irc.recv(8048)

irc = IRC("Freenode")
irc.identify(os.environ["DISTROBOT_PWD"])
irc.get_list(freenode_channels)
# some channels are not in /list
irc.get_channel("#kali-linux")
irc.get_channel("#alpine-linux")
irc.get_channel("#android-x86")
irc.get_channel("#manjaro")
irc.get_channel("#parabola")
irc.get_channel("#Solus")
irc.close()

# Linux Mint (this guys use separate IRC channel, Germans I guess)
irc = IRC("SpotChat")
time.sleep(60)
irc.get_list(["#linuxmint-help"])
irc.close()

# DragonFlyBSD (not sure why they use EFNet but ohh well)
irc = IRC("EFNet")
irc.get_channel("#dragonflybsd")
irc.close()

# aptosid (this guys use OFTC)
irc = IRC("OFTC")
irc.get_channel("#aptosid")
irc.close()

# sort results
print "\n\n\ndata collected!\n\n\n"
print "--BEGIN--"
print "Channel, Network, Users   # stats collected at "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M %Z")
keys = sorted(distro_map, key=distro_map.__getitem__, reverse=True)
for key in keys:
    print key.replace(" on ",", ")+", "+str(distro_map[key])
