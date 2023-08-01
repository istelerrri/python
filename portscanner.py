import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("enter ip you want to scan : ")
ports = [80, 21, 443, 445, 4444, 4455]

def portscan(port):
  try:
    s.connect((ip, port))
    return True
  except:
    return False

  
for port in ports:
  if portscan(port):
     print(str(port) + " is open")
  else:
     print(str(port) + " is close")
