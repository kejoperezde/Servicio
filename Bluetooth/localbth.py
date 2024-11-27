
import bluetooth

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

bd_addr = "00:06:66:0A:42:5D"
port = 0x1001

sock.connect((bd_addr, port))

sock.send("1")

sock.close()