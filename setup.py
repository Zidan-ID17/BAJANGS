import os, sys, socket, requests, subprocess
from support.clr import merah, putih

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
    subprocess.run(["python","support/cnt"], check=True)
    main()
