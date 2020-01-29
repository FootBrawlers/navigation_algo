import smbus
import time as t

bus = smbus.SMBus(1)
address = 0x08

def writeData(a,b,c,d):
    bus.write_i2c_block_data(address,a,[b,c,d])
    print("sent")
    return -1
           
if __name__ == '__main__':
    while True:
        t.sleep(1)
        try:
            writeData(1,2,3,4)
        except KeyboardInterrupt:
            quit()
