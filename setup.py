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
    os.system("cls" if os.name == "nt" else "clear" )
    sistem = platform.system()
    if sistem == "Windows":
        subprocess.run(["python", "for/win"], check=True)
    elif sistem == "Linux":
        subprocess.run({"python","for/lin"}, check=True)
    else:
        print(F"{putih}sistem operasi tidak diketahui/didukung {merah}!!")
        sys.exit()


if __name__ == "__main__":
    koneksi()
    main()
