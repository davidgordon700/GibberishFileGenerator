import os
import sys
import csv
import random
import string
import datetime

#fake intellisense
from commonSeedDataTypes import commonSeedDataTypes as cSDY


currentPath = os.path.dirname(os.path.abspath(__file__))
seedDataPath = os.path.join(currentPath,"SeedData") 

if not os.path.exists(seedDataPath):
    print("SeedData path does NOT exists ", seedDataPath)
    sys.exit(99)
else:
    print("SeedData path exists ", seedDataPath)

# seedDataTypes = ["FirstNames","LastNames"]

def getRandom0to9Str():
    """ 
    returns a random 0 to 9 value
    """
    
    return str(random.randrange(10))

def getRandomAtoZ():
    """ 
    returns a random A to Z value
    """
    
    return random.choice(string.ascii_letters.upper())

def getRandomItemFromList(existingList = []):
    """ 
    returns a random item from a list
    """
    if len(existingList) == 0:
        return "empty seed data"
    else:
        return random.choice(existingList)
    

def getSeedDataFromFile(seedDataType = "FirstNames"):
    """
    reads seed data from the support text files and returns a list.
    """

    seedData = []
    fileAndPath = os.path.join(seedDataPath, f"{seedDataType}.txt")
    if not os.path.exists(fileAndPath):
        print ("seed data does not exist", fileAndPath)
    else:    
        with open(fileAndPath,encoding='utf8') as f:
            for line in f:
                line = line.replace("\n","")
                if line != "":
                    seedData.append(line)

    return seedData

def getListOfDogPictures():
    path = "./SeedData/dogs/"

    listOfDogPictures = []
    
    if not os.path.exists(path):
        print ("seed data dog pictures folder does not exist", path)
    else:
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path,f)):
                filename,ext = os.path.splitext(f)
                if ext.upper() in [".JPEG",".PNG"]:
                    listOfDogPictures.append(os.path.join(path,f))

    return listOfDogPictures


def getSeedDataCityList():
    """
    reads seed data from the a CSV file of canadian cities.
    """

    seedData = []
    fileAndPath = os.path.join(seedDataPath, f"cgn_canada_csv_eng.csv")
    if not os.path.exists(fileAndPath):
        print ("seed data city list does not exist", fileAndPath)
    else:    
        f = open(fileAndPath,encoding='utf8')
        fcsv = csv.DictReader(f)
        for row in fcsv:
            CityName = row["Geographical Name"]
            ProvinceName = row["Province - Territory"]
            PostalCode = ""
            if ProvinceName == "British Columbia":
                PostalCode = "V"
            elif ProvinceName == "Newfoundland and Labrador":
                PostalCode = "A" 
            elif ProvinceName == "Nova Scotia":
                PostalCode = "B"
            elif ProvinceName == "Prince Edward Island":
                PostalCode = "C"
            elif ProvinceName == "New Brunswick":
                PostalCode = "E"
            elif ProvinceName == "Eastern Quebec":
                PostalCode = "H"
            elif ProvinceName == "Metropolitan Montreal":
                PostalCode = "J"
            elif ProvinceName == "Western Quebec":
                PostalCode = "J"
            elif ProvinceName == "Eastern Ontario":
                PostalCode = "K"
            elif ProvinceName == "Central Ontario":
                PostalCode = "L"
            elif ProvinceName == "Manitoba":
                PostalCode = "R"
            elif ProvinceName == "Saskatchewan":
                PostalCode = "B"
            elif ProvinceName == "Alberta":
                PostalCode = "B"
            else:
                PostalCode = "?"  #https://www.canadapost-postescanada.ca/cpc/en/support/articles/addressing-guidelines/postal-codes.page

            PostalCode = PostalCode + getRandom0to9Str() + getRandomAtoZ() + " " + getRandom0to9Str() + getRandomAtoZ() + getRandom0to9Str()
            
            city = {"CityName":CityName,
                    "Province": ProvinceName,
                     "PostalCode": PostalCode }     
            seedData.append(city)

    return seedData


def test_GetSeedData_FirstName():
    seedDataType = cSDY.FirstNames
    sdFirstName = getSeedDataFromFile(seedDataType=seedDataType)
    print("test - there are ",len(sdFirstName),seedDataType)

def test_GetSeedData_CityList():
    sdCityList = getSeedDataCityList()
    print("test - there are ",len(sdCityList),"cities")
    print(getRandomItemFromList(existingList=sdCityList))

if __name__ == '__main__':
    
    test_GetSeedData_FirstName()
    test_GetSeedData_CityList()
    print("")
    #getSeedDataCityList()

    