#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

"""
Capricorn    December 21 – January 18
Aquarius     January 19 – February 17
Pisces       February 18 – March 19
Aries        March 20 – April 18
Taurus       April 19 – May 19
Gemini       May 20 – June 20
Cancer       June 21 – July 21
Leo          July 22 – August 21
Virgo        August 22 – September 21
Libra        September 22 – October 22
Scorpio      October 23 – November 21
Sagittarius  November 22 – December 20
"""

def download(url):
    return requests.get(url).text

def get_horoscope(sign, mode="daily"):
    soup = source2soup(download(get_url(sign.lower())))
    content = soup.find("div", attrs={"class": "views-row"}).text

    if "Sorry the page cannot be found" in content:
        raise Error("Horoscope couldn't be found. Sorry!")
    
    if mode == "daily":
        daily = content.split("Daily")[1].split("Weekly")[0]
        return prettify(daily)
    elif mode == "weekly":
        weekly = content.split("Weekly")[1].split("Monthly")[0]
        return prettify(weekly)
    elif mode == "monthly":
        monthly = content.split("Monthly")[1].split("Year to Come")[0]
        return prettify(monthly)
    elif mode == "yearly":
        yearly = content.split("Year to Come")[1].split("Do You Want to Learn More?")[0]
        return prettify(yearly)
    else:
        raise Error("This mode is not supported.")

def get_url(sign):
    url = "https://www.shelleyvonstrunckel.com/site/starsigns?alias={}"
    return url.format(sign)

def prettify(text):
    if "Finances and Work" in text and "Love and Relationships" in text:
        # probably annual horoscope
        text = "\n\n".join(text.split("\n")[1:8])
    else:
        text = text.strip("\n\t\n").strip(" \n\n\t\t\t")
    return text

def source2soup(source):
    return BeautifulSoup(source, "html5lib")

def main():
    signs = ["Capricorn", "Aquarius", "Pisces", "Aries",
             "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius"]

    sign = "Aries"

    print([get_horoscope(sign, "daily")], end="\n\n")

    print([get_horoscope(sign, "weekly")], end="\n\n")

    print([get_horoscope(sign, "monthly")], end="\n\n")
    
    print([get_horoscope(sign, "yearly")], end="\n\n")


if __name__ == "__main__":
    main()

