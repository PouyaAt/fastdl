import requests
from bs4 import BeautifulSoup
import sys
import os

FASTDL_BASE = "https://fastdl.app/en"
POST_URL = os.getenv("IG_URL")

if not POST_URL:
    raise Exception("IG_URL environment variable is missing")

print("Downloading FastDL page...")

# 1. Request FastDL page
try:
    r = requests.get(f"{FASTDL_BASE}/download?url={POST_URL}", timeout=20)
    r.raise_for_status()
except Exception as e:
    with open("error_log.txt", "w") as f:
        f.write("FASTDL REQUEST ERROR:\n" + str(e))
    sys.exit(1)

html = r.text
with open("fastdl_output.html", "w", encoding="utf-8") as f:
    f.write(html)

print("FastDL page saved.")


# 2. Parse the FastDL page
soup = BeautifulSoup(html, "html.parser")

download_link = None

# FastDL usually uses <a class="button is-success" href="real_media_url">
for a in soup.find_all("a"):
    href = a.get("href", "")
    if "instagram" in href or ".jpg" in href or ".mp4" in href:
        download_link = href
        break

if not download_link:
    with open("error_log.txt", "w") as f:
        f.write("ERROR: Could not locate download link in HTML.\n")
    sys.exit(1)

print("Found media link:", download_link)

# 3. Download media
try:
    media = requests.get(download_link, timeout=20)
    media.raise_for_status()
except Exception as e:
    with open("error_log.txt", "w") as f:
        f.write("MEDIA DOWNLOAD ERROR:\n" + str(e))
    sys.exit(1)

content_type = media.headers.get("Content-Type", "")

if "image" in content_type:
    ext = ".jpg"
elif "video" in content_type:
    ext = ".mp4"
else:
    ext = ""

filename = f"downloaded{ext}"

print("Saving media as:", filename)

with open(filename, "wb") as f:
    f.write(media.content)

print("DONE.")
