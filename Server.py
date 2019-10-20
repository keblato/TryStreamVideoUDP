import subprocess
import threading
from queue import Queue

NUMBER_OF_THREADS = 3
JOB_NUMBER = [1,2,3]
queue = Queue()


def create_jobs():
    for x in JOB_NUMBER:
        print(x)
        queue.put(x)
    queue.join()

def work():
    while True:
        print("Empezo")
        x = queue.get()
        print(x)
        if x == 1:
            while True:
                print("Proceso 1")              
                p = subprocess.Popen('ffmpeg -i F:/ARCHIVOS/Documentos/GitHub/APRENDIENDO/Python/UDP/data/zeus.mp4 -f mpegts udp://192.168.1.18:1337', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = p.communicate()
                print(p.returncode)

        if x == 2:
            while True:
                print("Proceso 2")  
                p = subprocess.Popen('ffmpeg -i F:/ARCHIVOS/Documentos/GitHub/APRENDIENDO/Python/UDP/data/rambo.mp4 -f mpegts udp://192.168.1.18:1338', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = p.communicate()
                print(p.returncode)

        if x == 3:  
            print("Proceso 3")  
            p = subprocess.Popen('ffmpeg -i F:/ARCHIVOS/Documentos/GitHub/APRENDIENDO/Python/UDP/data/noticias.mp4 -f mpegts udp://192.168.1.18:1339', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print(p.returncode)           

        queue.task_done()


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        print("Creando workers")
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()
    


create_workers()

create_jobs()


''' import ffmpeg
import socket
# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 1337

packet_size = 65507

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))


process = (
    ffmpeg
    .input('F:/ARCHIVOS/Documentos/GitHub/APRENDIENDO/Python/UDP/video.mp4')
    .output('-', format='mpegts')
    .run_async(pipe_stdout=True)
)

while process.poll() is None:
    packet = process.stdout.read(packet_size)
    try:
        serverSock.sendall(packet)
    except socket.error:
        process.stdout.close()
        process.wait()
        break '''