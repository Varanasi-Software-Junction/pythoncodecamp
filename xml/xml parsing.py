import xml.etree.ElementTree as ET

import requests


def loadRSS():
    url = 'https://varanasisoftwarejunction.blogspot.com/rss.xml'
    resp = requests.get(url)
    with open('vsjblog.xml', 'wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    return root


def main():
    # loadRSS()
    root = parseXML("vsjblog.xml")
    print("Root", root)
    print("Children in Root")

    for child in root:
        print(child, child.tag, child.attrib)
        for subchild in child:
            print("Sub Children in Root")
            print(subchild, subchild.attrib)
    print("Cities")
    for city in root.findall('city'):
        rank = city.find('rank').text
        name = city.get('name')
        print("name: ", name, "rank: ", rank, "items:", city.items(), "text: ", city.text)
        print("City: ", city)
        for text in city:
            print("text; ", text.text)
            for mytags in text:
                print("mytags: ", mytags)


if __name__ == "__main__":
    main()
