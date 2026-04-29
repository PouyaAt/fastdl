import requests
import os
import sys

IG_URL = os.getenv("IG_URL")

def fail(msg):
    with open("error_log.txt", "w", encoding="utf-8") as f:
        f.write(msg)
    print(msg)
    sys.exit(1)

if not IG_URL:
    fail("IG_URL missing")

print("Calling FastDL API...")

api_url = "https://fastdl.app/api/instagram"

payload = {
    "url": IG_URL
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

try:
    r = requests.post(api_url, json=payload, headers=headers, timeout=30)
    r.raise_for_status()
except Exception as e:
    fail(f"API request failed: {e}")

data = r.json()

with open("fastdl_api_response.json", "w", encoding="utf-8") as f:
    f.write(str(data))

if "media" not in data or not data["media"]:
    fail("No media found in API response")

media_url = data["media"][0].get("url")
if not media_url:
    fail("Media URL missing")

print("Downloading media:", media_url)

try:
    media_resp = requests.get(media_url, timeout=30)
    media_resp.raise_for_status()
except Exception as e:
    fail(f"Media download failed: {e}")

ctype = media_resp.headers.get("Content-Type", "")

if "video" in ctype:
    filename = "downloaded.mp4"
elif "image" in ctype:
    filename = "downloaded.jpg"
else:
    filename = "downloaded.bin"

with open(filename, "wb") as f:
    f.write(media_resp.content)

print("Saved:", filename)
