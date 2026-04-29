import requests

def test_fastdl(insta_url):
    fastdl_url = "https://fastdl.app/instagram/?url=" + insta_url

    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(fastdl_url, headers=headers)

    with open("fastdl_output.html", "w", encoding="utf-8") as f:
        f.write(r.text)

    print("Saved fastdl_output.html")


if __name__ == "__main__":
    test_fastdl("https://www.instagram.com/p/C6t-U-OPVOG/")
