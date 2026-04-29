import requests
def test_fastdl(insta_url):
    fastdl_url = "https://fastdl.app/instagram/?url=" + insta_url

    print("Requesting:", fastdl_url)

    response = requests.get(fastdl_url)

    print("Status:", response.status_code)
    print("--- PAGE CONTENT START ---")
    print(response.text[:2000])   # print only the first 2000 characters
    print("--- PAGE CONTENT END ---")

if __name__ == "__main__":
    # Example public post (any public IG post is OK)
    instagram_post = "https://www.instagram.com/p/C6t-U-OPVOG/"

    test_fastdl(instagram_post)
