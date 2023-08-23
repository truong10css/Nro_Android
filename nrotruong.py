import base64
import os
import time

print(base64.b64decode('LS0tLS1Ub29sIEVuY29kZSBCeSBNWFQtLS0tLQ==').decode())
time.sleep(2)

while True:
    print("\033[1;92m")
    print("███╗░░░███╗░██████╗░████████╗")
    print("████╗░████║██╔═══██╗╚══██╔══╝")
    print("██╔████╔██║██║██╗██║░░░██║░░░")
    print("██║╚██╔╝██║╚██████╔╝░░░██║░░░")
    print("██║░╚═╝░██║░╚═██╔═╝░░░░██║░░░")
    print("╚═╝░░░░░╚═╝░░░╚═╝░░░░░░╚═╝░░░")
    
    print("\033[1;96m[1] Thiết lập")
    print("\033[1;932m[2] Chạy máy chủ")
    luachon = input("\033[1;92mLựa chọn: ")
    
    if luachon == '1':
        time.sleep(1)
        os.system('pkg install openjdk-17 -y -y && wget -O src.zip  https://github.com/KhanhNguyen9872/Nro-Offline_src/blob/main/src.zip?raw=true && unzip src.zip && clear ')
        os.system('rm -rf src.zip')
        os.system('clear')
        time.sleep(1)
        continue
    elif luachon == '2':
        time.sleep(1)
        print("\033[1;35mĐang khởi động máy chủ...")
        os.system('java -Xms2G  -Xmx2G -jar dist/mad.jar')
        break
    else:
        print("\033[1;91mLựa chọn không hợp lệ. Vui lòng chọn lại.")
        print("\033[1;93m-------------------------------------------------------------")
        time.sleep(1)
        continue
