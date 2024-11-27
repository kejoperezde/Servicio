import bluetooth
import time

def conectar_a_dispositivo(direccion_mac):
    try:
        # Intentamos establecer una conexión RFCOMM (comunicación serie)
        print(f"Intentando conectar a {direccion_mac}...")
        
        # El puerto RFCOMM por defecto es 1, pero podría variar dependiendo del dispositivo
        puerto = 1  # Usualmente el puerto de comunicación serial es el 1
        
        # Creamos el socket RFCOMM
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        
        # Conectamos al dispositivo Bluetooth en el puerto RFCOMM
        socket.connect((direccion_mac, puerto))
        
        print(f"Conectado exitosamente a {direccion_mac}")
        
        # Enviar '1' al dispositivo
        socket.send(b'1')
        # print("Enviado '1' al dispositivo.")
        
        # Esperar 10 segundos
        time.sleep(10)
        
        # Enviar '0' al dispositivo
        socket.send(b'0')
        # print("Enviado '0' al dispositivo.")
        
        # Cerramos el socket después de la comunicación
        socket.close()
        print("Conexión cerrada.")
        
    except bluetooth.BluetoothError as e:
        print(f"No se pudo conectar al dispositivo: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    direccion_mac = "00:06:66:0A:42:5D"  # Dirección MAC del dispositivo Bluetooth
    conectar_a_dispositivo(direccion_mac)
