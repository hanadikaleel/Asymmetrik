import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from BusinessCard import ContactInfo


class BusinessCardParser:
    def getContactInfo(document):

        # getEmailAddress
        email = re.findall("\S*@{1}.*", document)[0]

        # getPhoneNumber
        phone = re.findall(
            "[+]?\d?\s?[(]?\d{3}[)-]?\s?\d{3}[-]?\d{4}", document)[0]
        phone = re.sub("\D", "", phone)

        # getName

        res = requests.get(
            "https://namecensus.com/top-first-names/top-first-names.html")
        soup = BeautifulSoup(res.content, 'lxml')
        table = soup.find('table')
        top_names = pd.read_html(str(table))[0].loc[:, 1]

        # first search through most common names database
        name = ""
        names = document.split("\n")
        names = [x for x in names if "&" not in x]
        for n1 in names:
            for n2 in top_names:
                if n2 in n1:
                    name = n1

        # if name not found in database, search for name by parsing email
        if name == "":
            lst = document.split("\n")
            lst.remove(email)
            for line in lst:
                if "&" in line:
                    lst.remove(line)
                last = line.split()[-1].lower()
                if last in email:
                    name = line

        return ContactInfo(name, phone, email)
