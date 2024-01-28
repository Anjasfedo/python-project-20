import urllib.request as urllib

def main(url):
    print("Checking connectivity")

    res = urllib.urlopen(url)

    print(f"Connected to {url} successfuly")

    print(f"With response code {res.getcode()}")


print("Site connectivity checker")

domain = input("> Input domain of site (e.g: google.com): ")

full_domain = f"https://www.{domain}"

main(full_domain)