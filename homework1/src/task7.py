import requests

def get_status_code(url):
    """
    Makes an HTTP GET request to the specified URL
    and returns the status code.
    """
    response = requests.get(url)
    return response.status_code

def main():
    url = "https://httpbin.org/get"
    status = get_status_code(url)
    print(f"Status code for {url}: {status}")

if __name__ == "__main__":
    main()
