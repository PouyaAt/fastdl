import requests
import traceback

def test_fastdl(insta_url):
    try:
        fastdl_url = "https://fastdl.app/instagram/?url=" + insta_url

        headers = {"User-Agent": "Mozilla/5.0"}

        r = requests.get(fastdl_url, headers=headers)

        with open("fastdl_output.html", "w", encoding="utf-8") as f:
            f.write(r.text)

        print("Saved fastdl_output.html")

    except Exception:
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(traceback.format_exc())

        print("Error saved to error_log.txt")


if __name__ == "__main__":
    test_fastdl("https://www.instagram.com/p/C6t-U-OPVOG/")
