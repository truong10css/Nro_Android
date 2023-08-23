import base64
import os
import shutil
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
    
    print("\033[1;96m[1] Cài đặt OpenJDK 17")
    print("\033[1;932m[2] Sao chép tệp từ điện thoại và tạo thư mục 'nro'")
    print("\033[1;91m[3] Thoát")
    
    luachon = input("\033[1;92mLựa chọn: ")
    
    if luachon == '1':
        time.sleep(1)
        os.system('pkg install openjdk-17 -y -y')
        time.sleep(1)
        os.system('clear')
        print("\033[1;92mCài đặt OpenJDK 17 thành công.\n")
        continue
    elif luachon == '2':
        time.sleep(1)
        src_file = 'sdcard/Download/mad3.zip'
        dest_folder = '/data/data/com.termux/files/home/nro'
        
        try:
            os.makedirs(dest_folder, exist_ok=True)
            shutil.copy2(src_file, dest_folder)
            print("\033[1;92mĐã sao chép thành công từ điện thoại và tạo thư mục 'nro'.\n")
        except Exception as e:
            print("\033[1;91mĐã xảy ra lỗi: {}\n".format(e))
        
        continue
    elif luachon == '3':
        print("\033[1;91mĐã thoát chương trình.")
        break
    else:
        print("\033[1;91mLựa chọn không hợp lệ. Vui lòng chọn lại.")
        print("\033[1;93m-------------------------------------------------------------")
        time.sleep(1)
        continue
