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
    
    print("\033[1;96m[1] Kiểm tra và cài đặt OpenJDK 17")
    print("\033[1;932m[2] Sao chép tệp từ điện thoại và tạo thư mục 'nro'")
    print("\033[1;94m[3] Chạy server")
    print("\033[1;91m[4] Thoát")
    
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
        src_zip_path = '/sdcard/Download/nro.zip'
        unzip_dir = '/data/data/com.termux/files/home/nro_folder/'
        
        if os.path.exists(unzip_dir):
            print("Đã tồn tại folder rồi!")
        else:
            os.makedirs(unzip_dir, exist_ok=True)
            shutil.copy(src_zip_path, unzip_dir)
            os.chdir(unzip_dir)
            os.system('unzip mad3.zip && clear')
            os.system('rm -rf mad3.zip')
            os.system('clear')
            print("\033[1;92mĐã sao chép thành công từ điện thoại và tạo thư mục 'nro'.\n")
          continue
    elif luachon == '3':
        time.sleep(1)
        # Kiểm tra thư mục đã giải nén
        if os.path.exists('/data/data/com.termux/files/home/nro/dist/mad.jar'):
            print("\033[1;35mĐang khởi động máy chủ...")
            os.system('java -jar /data/data/com.termux/files/home/nro/dist/mad.jar')
        else:
            print("\033[1;91mThư mục 'nro' chưa được giải nén. Vui lòng thực hiện bước 2 trước.\n")
        
        break
    elif luachon == '4':
        print("\033[1;91mĐã thoát chương trình.")
        break
    else:
        print("\033[1;91mLựa chọn không hợp lệ. Vui lòng chọn lại.")
        print("\033[1;93m-------------------------------------------------------------")
        time.sleep(1)
        continue
