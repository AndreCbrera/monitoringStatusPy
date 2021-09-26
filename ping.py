import subprocess

hostList = open("./hostList.txt", "r")

ips = hostList.readlines()

def pingcheck(ips):
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

def main():
    #print(ips)
    pingcheck(ips)

if __name__ == "__main__":
    main()
