import pyshorteners

url=input("Enter ur site name :")

s=pyshorteners.Shortener()

short_url=s.tinyurl.short(url)

print("Ur shortened url is :"+short_url)