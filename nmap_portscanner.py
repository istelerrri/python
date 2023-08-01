import nmap

scan = nmap.PortScanner()

ip = input("enter ip adress : ")
scan.scan(ip)
