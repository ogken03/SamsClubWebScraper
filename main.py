import requests
from bs4 import BeautifulSoup
def productSearch(input):
    url = "https://www.samsclub.com/s/{}".format(input)
    html = requests.get(url)

    s = BeautifulSoup(html.content, 'html.parser')

    results = s.find(id="main")

    #find names
    productNames= results.find_all("h3")
    productPrices = results.find_all(class_="Price-group")


    print("\nHere is 4 searches for |"+input+"|.\n")
    for x in range(4):
        print(productNames[x].text)
        print(productPrices[x].text[:21].rstrip('$'))




if __name__ == '__main__':
    search = input("Please enter what you want to search: ")
    productSearch(search)
