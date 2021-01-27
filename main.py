import socket
try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.settimeout(10)
   s.connect(("10.10.0.250", 8010))

   print(s)

   while True:
      try:
          s.send(b'1b02fa031b03c8')
          reply = s.recv(131072)
          if not reply:
              break
          print("recvd: ", reply)
        except KeyboardInterrupt:
             print("bye")
             break
    s.close()
    except socket.error as socketerror:
    s.close()
   print("Error: ", socketerror)


