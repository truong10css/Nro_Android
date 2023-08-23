import base64
import os
import shutil
import time
import zipfile

def clear_screen():
    os.system('clear')

print("\033[1;91m HI!IAM QUANG TRUONG.")
time.sleep(2)

while True:
    clear_screen()
    print("\033[1;92m")
    print("███╗░░░███╗░██████╗░████████╗")
    print("████╗░████║██╔═══██╗╚══██╔══╝")
    print("██╔████╔██║██║██╗██║░░░██║░░░")
    print("██║╚██╔╝██║╚██████╔╝░░░██║░░░")
    print("██║░╚═╝░██║░╚═██╔═╝░░░░██║░░░")
    print("╚═╝░░░░░╚═╝░░░╚═╝░░░░░░╚═╝░░░")
    
    print("\033[1;96m[1] Kiểm tra và cài đặt OpenJDK 17")
    print("\033[1;932m[2] Sao chép và giải nén tệp từ điện thoại vào Termux, sau đó xóa thư mục")
    print("\033[1;94m[3] Chạy server")
    print("\033[1;91m[4] Thoát")
    
    luachon = input("\033[1;92mLựa chọn: ")
    
    if luachon == '1':
        clear_screen()
        time.sleep(1)
        # Kiểm tra cài đặt OpenJDK 17
        result = os.system('java -version 2>&1 | grep "openjdk version" | grep "17"')
        if result == 0:
            print("\033[1;92mOpenJDK 17 đã được cài đặt.\n")
        else:
            os.system('pkg install openjdk-17 -y -y')
            print("\033[1;92mCài đặt OpenJDK 17 thành công.\n")
        
        input("\033[1;92mNhấn Enter để tiếp tục...")
        continue
    elif luachon == '2':
        clear_screen()
        time.sleep(1)
        file_name = input("\033[1;92mNhập tên tệp từ điện thoại (ví dụ: mad3.zip): ")
        src_file = os.path.join('/sdcard/Download', file_name)
        dest_folder = '/data/data/com.termux/files/home/nro'
        
        try:
            if os.path.exists(src_file):
                os.makedirs(dest_folder, exist_ok=True)
                shutil.copy2(src_file, os.path.join(dest_folder, file_name))
                print("\033[1;92mĐã sao chép thành công từ điện thoại vào Termux.\n")
                
                if not os.path.exists(os.path.join(dest_folder, 'dist/mad.jar')):
                    with zipfile.ZipFile(os.path.join(dest_folder, file_name), 'r') as zip_ref:
                        zip_ref.extractall(dest_folder)
                        print("\033[1;92mĐã giải nén tệp.\n")
                    
                    os.remove(os.path.join(dest_folder, file_name))
                    print("\033[1;92mĐã xóa tệp sau khi giải nén.\n")
                else:
                    print("\033[1;91mThư mục đã giải nén tồn tại.\n")
            
            else:
                print("\033[1;91mTệp từ điện thoại không tồn tại.\n")
        
        except Exception as e:
            print("\033[1;91mĐã xảy ra lỗi: {}\n".format(e))
        
        input("\033[1;92mNhấn Enter để tiếp tục...")
        continue
    elif luachon == '3':
        clear_screen()
        time.sleep(1)
        if os.path.exists('/data/data/com.termux/files/home/nro/dist/mad.jar'):
            print("\033[1;35mĐang khởi động máy chủ...")
            os.system('java -Xms2G -Xmx2G -jar /data/data/com.termux/files/home/nro/dist/mad.jar')
        else:
            print("\033[1;91mThư mục 'nro' chưa được giải nén. Vui lòng thực hiện bước 2 trước.\n")
        
        input("\033[1;92mNhấn Enter để tiếp tục...")
        break
    elif luachon == '4':
        clear_screen()
        print("\033[1;91mĐã thoát chương trình.")
        break
    else:
        clear_screen()
        print("\033[1;91mLựa chọn không hợp lệ. Vui lòng chọn lại.")
        print("\033[1;93m-------------------------------------------------------------")
        input("\033[1;92mNhấn Enter để tiếp tục...")
        continue
