import requests
import time

url = "https://shreesevahospital-1.onrender.com/api/blogs"
headers = {
    "Host": "shreesevahospital-1.onrender.com",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": "\"Chromium\";v=\"135\", \"Not-A.Brand\";v=\"8\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Sec-Ch-Ua-Mobile": "?0",
    "Accept": "*/*",
    "Origin": "https://shreesevahospital.vercel.app",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Storage-Access": "active",
    "Referer": "https://shreesevahospital.vercel.app/",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=4, i",
    "Connection": "keep-alive"
}

def send_request():
    try:
        response = requests.get(url, headers=headers)
        print(f"[+] Status Code: {response.status_code}")
        print(f"[+] Response: {response.text[:100]}...")  # Print first 100 characters of response
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    while True:
        send_request()
        print("[*] Waiting 10 minutes before next request...\n")
        time.sleep(180)  # 600 seconds = 3 minutes
