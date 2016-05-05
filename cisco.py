import Connectivity
import Systems
m = Systems.OperatingSystems['IOS']
iplist = ['192.168.1.1','192.168.1.2']
cmdlist = ['show ip int brief','show cdp nei detail','show arp','show ver']
for ip in iplist:
    if ip == '192.168.1.1':
        s = Connectivity.Session(ip,23,"telnet",m)
        s.login("", "passwd")
    else:
        s = Connectivity.Session(ip,22,"ssh",m)
        s.login("username", "passwd")
    s.escalateprivileges('enpasswd')
    f = open(ip+'.txt','w+')
    for cmd in cmdlist:
        a = s.sendcommand(cmd)
        f.write(ip+cmd+'\n')
        f.write(a+'\n')
    f.close()
    s.logout()
