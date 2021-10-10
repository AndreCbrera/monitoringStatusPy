import os
import sys
import subprocess
import datetime
import time

FILE = os.path.join(os.getcwd(), "./networkinfo.log")
 

hostList = open("./hostList.txt", "r")

ips = hostList.readlines()

def pingCheck(ips):
    for ip in ips:
        response = subprocess.Popen(["ping", "-c", "1", ip.strip()],
                                stdout = subprocess.PIPE,
                                stderr = subprocess.STDOUT)

        stdout, stderr = response.communicate()

        if (response.returncode == 0):
            status = ip.rstrip() + " Online"
        else:
            status = ip.rstrip() + " Offline"    
        print(status)

def calculateTime(start, stop):
    diference = stop -start
    seconds = float(str(diference.totalSeconds()))
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]

def main():
    #print(ips)
    #pingCheck(ips)
    while True:
        if pingCheck(ips):
            time.sleep(5)
        else:
            downTime = datetime.datetime.now()
            failMsg = "disconnectetd at: " + str(downTime).split(".")[0]
            print(failMsg)

            with open(FILE, "a") as file:
                file.write(failMsg+ "\n")

            while not pingCheck(ips):

                time.sleep(1)

            upTime = datetime.datetime.now()

            upTimeMsg = "Connected again: " + str(upTime).split(".")[0]

            downTime = calculateTime(downTime, upTime)
            
            unavailablityTime = "Connection was  unavailablity for : " + downTime

            print(upTimeMsg)
            print(unavailablityTime)

            with open(FILE, "a") as file:

                file.write(upTimeMsg + "\n")
                file.write(unavailablityTime + "\n")



if __name__ == "__main__":
    main()
