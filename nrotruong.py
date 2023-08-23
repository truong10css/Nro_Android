import os
import shutil

def run_ngrok(port, ngrok_auth_token):
    os.system(f'ngrok tcp {port} -authtoken {ngrok_auth_token}')

while True:
    os.system('clear')

    print("\033[1;92m")
    print("███╗░░░███╗░██████╗░████████╗")
    print("████╗░████║██╔═══██╗╚══██╔══╝")
    print("██╔████╔██║██║██╗██║░░░██║░░░")
    print("██║╚██╔╝██║╚██████╔╝░░░██║░░░")
    print("██║░╚═╝░██║░╚═██╔═╝░░░░██║░░░")
    print("╚═╝░░░░░╚═╝░░░╚═╝░░░░░░╚═╝░░░")
    print("\033[1;96m[1] Cài đặt JDK 17")
    print("\033[1;932m[2] Giải nén tệp từ đường dẫn /sdcard/Download/nro1.zip")
    print("\033[1;92m[3] Chạy server")
    print("\033[1;92m[4] Online")
    print("\033[1;92m[5] Thoát")
    print("\033[1;92mLua chon: \033[1;33m")

    luachon = input().strip()

    if luachon == "1":
        os.system('pkg install openjdk-17 -y -y')
        os.system('clear')
    elif luachon == "2":
        src_zip_path = '/sdcard/Download/nro.zip'
        unzip_dir = '/data/data/com.termux/files/home/nro_folder/'
        
        if os.path.exists(unzip_dir):
            print("Đã tồn tại folder rồi!")
        else:
            os.makedirs(unzip_dir, exist_ok=True)
            shutil.copy(src_zip_path, unzip_dir)
            os.chdir(unzip_dir)
            os.system('unzip nro1.zip && clear')
            os.system('clear')
    elif luachon == "3":
            os.system('java -Xms2G  -Xmx2G -jar /data/data/com.termux/files/home/nro_dolder/BARCOLL_NROKING/dist/Heroes_Z.jar')
    elif luachon == "4":
        ngrok_auth_token = input("Nhập token ngrok của bạn: ").strip()
        port = input("Nhập port game: ").strip()
        run_ngrok(port, ngrok_auth_token)
    elif luachon == "5":  
        break
    else:
        print("\033[1;91mChon Sai Vui Lòng Chọn Lại")
        print("\033[1;93m-------------------------------------------------------------")
