import subprocess
import threading
import time

def main():
    subprocess.run(["uvicorn","main:app","--port","8000"])

def cal():
    subprocess.run(["uvicorn","cal:app","--port","8001"])

if __name__=="__main__":
    print("strating the server")
    main_thread = threading.Thread(target=main)    
    main_thread.start()
    time.sleep(2)
    cal_thread = threading.Thread(target=cal)
    cal_thread.start()
    main_thread.join()
    cal_thread.join()