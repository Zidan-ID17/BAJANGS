import os, sys, socket, requests, subprocess
from supp.ctr import printl

putih  = "\033[97m"
merah = "\033[91m"

def koneksi():
    try:
        socket.create_connection(("8.8.8.8", 50))
        return True
      
    except OSError:
        print(f"{putih} tidak dapat terhubung ke internet {merah}!! ")
        return False

def main():
    os.system("cls" if os.name == "nt" else "clear" )
    print("")
    printl(f" {putih}SILAHKAN PILIH SISTEM OPERASI YANG ANDA GUNAKAN ")
    print("")
    printl("linux")
    printl("Windows")
    select = input("    ").lower()
    if select == "linux":
        linux = "https://raw.githubusercontent.com/Zidan-ID17/hozon/master/MyApp/linux/a.py"
        status = requests.get(linux, stream=True)
        if status.status_code == 200:
            with open("a.py", "wb") as file:
                file.write(status.content)
            subprocess.run(["python", "a.py"], check=True)
        else:
            print(" tidak dapat terhubung ke internet ! ")
            sys.exit()
          
    elif select == "windows":
        windows = "https://raw.githubusercontent.com/Zidan-ID17/hozon/master/MyApp/windows/a.py"
        status = requests.get(windows, stream=True)
        if status.status_code == 200:
            with open("a.py", "wb") as file:
                file.write(status.content)
            subprocess.run(["python", "a.py"], check=True))
        else:
            print(f"{putih} tidak dapat terhubung ke internet {merah}!! ")
            sys.exit()
          
    else:
        main()


if __name__ == "__main__":
    koneksi()
    main()
