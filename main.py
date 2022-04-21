import urllib.request
import json


# prints count of qualifying lines in title and returns that count
# parameter 'title' is a tuple of the number of the title and the address of the CSV file
def law_count(title):

    # to avoid 'Forbidden' response
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=title[1], headers=headers)
    filein = urllib.request.urlopen(req)

    # checks string to make sure 'Repealed' or 'Reserved' or 'Effective until' or 'Expired"do not appear only at beginning of statute body
    # otherwise counts and prints and returns total
    total = 0
    for line in filein:
        if "|Repeale" not in str(line) and "|Reserved." not in str(line) and "|(Effective u" not in str(line) and "|Expired." not in str(line):
            total += 1
    print("There are currently", total, "active laws in Title", title[0], "of the Code of Virginia.")
    return total


# JSON of all titles stored by Virginia Law Online Library
page = "https://law.lis.virginia.gov/api/CoVTitlesGetListOfJson"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=page, headers=headers)
try:
    filein = urllib.request.urlopen(req)
except IOError as error:
    print("File could not be found.")


# create local list of dictionaries
for item in filein:
    myList = json.loads(item)

# create dictionary of TitleNumber (key) and address where that title is stored online (value)
titleList = {}
for dic in myList:
    titleList[dic['TitleNumber']] = "https://law.lis.virginia.gov/CSV/CoVTitle_" + dic['TitleNumber'] + ".csv"

# there is a superfluous line at the beginning of Title 1, so codeTotal starts at -1
# run law_count and add each title's total to codeTotal
codeTotal = -1
for item in titleList.items():
    codeTotal += law_count(item)

print("\n" + "This is a grand total of " + f'{codeTotal:,}' + " currently active laws in the Code of Virginia")
filein.close()
