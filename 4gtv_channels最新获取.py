from curl_cffi import requests
import time

# 本地代理（Clash / V2Ray / Surge 等）
proxies = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897",
}

# 创建 session 并模拟 Chrome
session = requests.Session()
session.proxies = proxies
session.impersonate = "chrome124"  # 模拟 Chrome 124

# 输出 TXT 文件
txt_file = "4gtv_channels.txt"

with open(txt_file, "w", encoding="utf-8") as f:

    for i in range(1, 300):
        url = f"https://api2.4gtv.tv/Channel/GetChannel/{i}"

        try:
            r = session.get(
                url,
                timeout=10,
                headers={
                    "Accept": "application/json",
                    "Referer": "https://www.4gtv.tv/",
                }
            )

            if r.status_code != 200:
                print(f"频道 {i} HTTP {r.status_code}")
                continue

            data = r.json()

            if data.get("Success") and data.get("Data"):
                name = data["Data"].get("fsNAME")
                cid = data["Data"].get("fs4GTV_ID")

                if name and cid:
                    line = f"{name},{cid}\n"
                    f.write(line)
                    print(line.strip())  # 控制台打印

            else:
                print(f"频道 {i} 无有效数据")

        except Exception as e:
            print(f"频道 {i} 出错: {e}")

        time.sleep(0.15)  # 控制抓取速度

print(f"\n✅ 抓取完成，结果已保存到 {txt_file}")
