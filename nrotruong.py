import os
import shutil
import time
import zipfile

def clear_screen():
    os.system('clear')

def setup_jdk():
    print("\033[1;92mĐang kiểm tra và cài đặt OpenJDK 17...")
    result = os.system('java -version 2>&1 | grep "openjdk version" | grep "17"')
    if result == 0:
        print("\033[1;92mOpenJDK 17 đã được cài đặt.\n")
    else:
        os.system('pkg install openjdk-17 -y -y')
        print("\033[1;92mCài đặt OpenJDK 17 thành công.\n")

def copy_and_extract(source_path, target_folder):
    try:
        if os.path.exists(source_path):
            os.makedirs(target_folder, exist_ok=True)
            shutil.copy2(source_path, os.path.join(target_folder, os.path.basename(source_path)))
            print("\033[1;92mĐã sao chép thành công từ điện thoại vào Termux.\n")
            
            if not os.path.exists(os.path.join(target_folder, 'dist/mad.jar')):
                with zipfile.ZipFile(os.path.join(target_folder, os.path.basename(source_path)), 'r') as zip_ref:
                    zip_ref.extractall(target_folder)
                    print("\033[1;92mĐã giải nén tệp.\n")
                
                os.remove(os.path.join(target_folder, os.path.basename(source_path)))
                print("\033[1;92mĐã xóa tệp sau khi giải nén.\n")
            else:
                print("\033[1;91mThư mục đã giải nén tồn tại.\n")
        else:
            print("\033[1;91mTệp từ điện thoại không tồn tại.\n")
    
    except Exception as e:
        print("\033[1;91mĐã xảy ra lỗi: {}\n".format(e))
        print("\033[1;91mĐang thực hiện xóa toàn bộ thư mục đã tạo trong Termux...\n")
        shutil.rmtree(target_folder)
        print("\033[1;91mĐã xóa toàn bộ thư mục đã tạo trong Termux.\n")

def run_server():
    if os.path.exists('/data/data/com.termux/files/home/Nro_Android/dist'):
        dist_files = os.listdir('/data/data/com.termux/files/home/Nro_Android/dist')
        if dist_files:
            print("\033[1;96mCác tệp .jar hiện có trong thư mục 'dist':")
            for index, file in enumerate(dist_files, start=1):
                if file.endswith('.jar'):
                    print(f"{index}. {file}")
            selected_index = int(input("\033[1;92mNhập số tương ứng với tệp .jar để chạy: ")) - 1
            if 0 <= selected_index < len(dist_files) and dist_files[selected_index].endswith('.jar'):
                selected_jar_file = dist_files[selected_index]
                print("\033[1;35mĐang khởi động máy chủ...")
                os.system(f'java -Xms2G -Xmx2G -jar /data/data/com.termux/files/home/Nro_Android/dist/{selected_jar_file}')
            else:
                print("\033[1;91mLựa chọn không hợp lệ.\n")
        else:
            print("\033[1;91mThư mục 'dist' không có tệp .jar.\n")
    else:
        print("\033[1;91mThư mục 'dist' không tồn tại.\n")

def delete_folders():
    clear_screen()
    print("\033[1;91mĐang thực hiện xóa toàn bộ thư mục đã tạo trong Termux...\n")
    shutil.rmtree('/data/data/com.termux/files/home/Nro_Android')
    print("\033[1;91mĐã xóa toàn bộ thư mục đã tạo trong Termux.\n")
    
    input("\033[1;92mNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    clear_screen()
    print("\033[1;91mHI! IAM QUANG TRUONG.")
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
        print("\033[1;932m[2] Sao chép và giải nén tệp từ điện thoại vào Termux, sau đó xóa thư mục (nếu có lỗi)")
        print("\033[1;94m[3] Chạy server")
        print("\033[1;91m[4] Xóa toàn bộ thư mục đã tạo trong Termux")
        print("\033[1;93m[5] Thoát")
        
        luachon = input("\033[1;92mLựa chọn: ")
        
        if luachon == '1':
            clear_screen()
            time.sleep(1)
            setup_jdk()
            input("\033[1;92mNhấn Enter để tiếp tục...")
        elif luachon == '2':
            clear_screen()
            time.sleep(1)
            file_name = input("\033[1;92mNhập tên tệp từ điện thoại (ví dụ: mad3.zip): ")
            src_file = os.path.join('/sdcard/Download', file_name)
            dest_folder = '/data/data/com.termux/files/home/Nro_Android'
            copy_and_extract(src_file, dest_folder)
            input("\033[1;92mNhấn Enter để tiếp tục...")
        elif luachon == '3':
            clear_screen()
            time.sleep(1)
            run_server()
            input("\033[1;92mNhấn Enter để tiếp tục...")
        elif luachon == '4':
            delete_folders()
            continue
        elif luachon == '5':
            clear_screen()
            print("\033[1;91mĐã thoát chương trình.")
            break
        else:
            clear_screen()
            print("\033[1;91mLựa chọn không hợp lệ. Vui lòng chọn lại.")
            print("\033[1;93m")
            input("Nhấn Enter để tiếp tục...")
