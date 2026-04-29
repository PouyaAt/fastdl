import requests
import traceback
import os

def write_marker(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def test_fastdl(insta_url):
    try:
        write_marker("script_started.txt", "Python script has started.\n")

        fastdl_url = "https://fastdl.app/instagram/?url=" + insta_url
        headers = {"User-Agent": "Mozilla/5.0"}

        r = requests.get(fastdl_url, headers=headers, timeout=20)

        write_marker("fastdl_output.html", r.text)

        write_marker("script_finished.txt", "Python script finished successfully.\n")

    except Exception:
        write_marker("error_log.txt", traceback.format_exc())

if __name__ == "__main__":
    test_fastdl("https://www.instagram.com/p/C6t-U-OPVOG/")
