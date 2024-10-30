import re


def main():
    print(parse(input("HTML:")))


def parse(s):
    match = re.search(r'<iframe.*?src="(https|http)://(www\.|)youtube\.com/embed/([^"]+)".*?>' , s)
    if match:
        return f"https://youtu.be/{match.group(3)}"




if __name__ == "__main__":
    main()

