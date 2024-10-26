from pymodbus.client import ModbusTcpClient
import time
client=ModbusTcpClient('192.168.0.133',port=502)
connection=client.connect()
if connection:
    print('Connected')
    client.write_coil(16,True)
    for i in range(10):
        client.write_register(128,i)
        client.write_register(129,i+2)
        time.sleep(1)
    client.write_coil(16,False)
    client.close()