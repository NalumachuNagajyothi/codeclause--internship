import pyshorteners

def short_url(url):
    shortener=pyshorteners.Shortener()
    a=shortener.tinyurl.short(url)
    return a
url_data="https://youtu.be/Lp9Ftuq2sVI?si=8e9apW5dYwa6z3Wd"
print(short_url(url_data))
