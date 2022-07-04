import asyncio
import serial_asyncio
import bpy
import random

loop = None
terminar = False

class OutputProtocol(asyncio.Protocol):
    
    def connection_made(self, transport):
        self.transport = transport
        print('port opened', transport)
        transport.serial.rts = False  # You can manipulate Serial object via transport
        transport.write(b'Hello, World!\n')  # Write serial data via transport

    def data_received(self, data):
        #print('data received', repr(data))
        for caracter in data:
            if caracter == ord('+'):
                print("más")
                bpy.ops.mesh.primitive_cube_add(
                    size=1, 
                    enter_editmode=False, 
                    align='WORLD', 
                    location=(-5+random.random()*10, -5+random.random()*10, -5+random.random()*10), 
                    scale=(1, 1, 1)
                )

            elif caracter == ord('-'):
                bpy.ops.mesh.primitive_monkey_add(
                    size=1, 
                    enter_editmode=False, 
                    align='WORLD', 
                    location=(-5+random.random()*10, -5+random.random()*10, -5+random.random()*10), 
                    scale=(1, 1, 1)
                )

                print("menos")
        if b'*' in data:
            self.transport.close()
            

    def connection_lost(self, exc):
        print('port closed')
        self.transport.loop.stop()

    def pause_writing(self):
        print('pause writing')
        print(self.transport.get_write_buffer_size())

    def resume_writing(self):
        print(self.transport.get_write_buffer_size())
        print('resume writing')


loop = asyncio.get_event_loop()


corutinaSerial = serial_asyncio.create_serial_connection(loop, OutputProtocol, '/dev/ttyACM0', baudrate=115200)
transport, protocol = loop.run_until_complete(corutinaSerial)

    
def cicloAsyncio():
    global loop
    #loop = asyncio.get_event_loop()
    loop.stop()
    loop.run_forever()
    #asyncio.run()
    return 0.001
    
bpy.app.timers.register(cicloAsyncio)
#loop.run_forever()
#loop.close()


