import base64
import os
import shutil
import time
import zipfile

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
    
    print("\033[1;96m[1] Kiểm tra và cài đặt OpenJDK 17")
    print("\033[1;932m[2] Sao chép tệp từ điện thoại vào Termux, giải nén và xóa tệp")
    print("\033[1;91m[3] Thoát")
    
    luachon = input("\033[1;92mLựa chọn: ")
    
    if luachon == '1':
        time.sleep(1)
        # Kiểm tra cài đặt OpenJDK 17
        result = os.system('java -version 2>&1 | grep "openjdk version" | grep "17"')
        if result == 0:
            print("\033[1;92mOpenJDK 17 đã được cài đặt.\n")
        else:
            os.system('pkg install openjdk-17 -y -y')
            print("\033[1;92mCài đặt OpenJDK 17 thành công.\n")
        
        continue
    elif luachon == '2':
        time.sleep(1)
        src_file = 'sdcard/Download/mad3.zip'
        dest_folder = '/data/data/com.termux/files/home/nro'
        
        try:
            os.makedirs(dest_folder, exist_ok=True)
            shutil.copy2(src_file, dest_folder)
            print("\033[1;92mĐã sao chép thành công từ điện thoại vào Termux.\n")
            
            with zipfile.ZipFile(os.path.join(dest_folder, 'mad3.zip'), 'r') as zip_ref:
                zip_ref.extractall(dest_folder)
                print("\033[1;92mĐã giải nén tệp.\n")
            
            os.remove(os.path.join(dest_folder, 'mad3.zip'))
            print("\033[1;92mĐã xóa tệp sau khi giải nén.\n")
            
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
