import requests
import traceback

def test_fastdl(insta_url):
    try:
        # FastDL endpoint
        fastdl_url = "https://fastdl.app/instagram/?url=" + insta_url

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        # Fetch FastDL page
        r = requests.get(fastdl_url, headers=headers, timeout=20)

        # Save full HTML output
        with open("fastdl_output.html", "w", encoding="utf-8") as f:
            f.write(r.text)

        print("Saved fastdl_output.html from FastDL successfully.")

    except Exception:
        # In case of ANY error, save traceback
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(traceback.format_exc())

        print("Error occurred. Saved to error_log.txt.")


if __name__ == "__main__":
    # Replace this with any Instagram post URL
    test_fastdl("https://www.instagram.com/p/C6t-U-OPVOG/")
