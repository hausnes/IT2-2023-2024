# Laga av Trygve Kvåle Garatun

import json
import numpy as np
import datetime
import unittest

# Mye av denne koden er hentet og inpirert av et tidligere prosjekt som jeg har jobbet med på fritiden. 
# https://github.com/Raydog69/NutrientsApp/blob/Edit/backendMain.py #Lenke til github-repositoryen min

#Del B

class SamleObjekt():
    def __init__(self, name, sold_price, current_price, kategori):
        self.name = name
        self.sold_price = sold_price
        self.current_price = current_price
        self.kategori = kategori

    def toDict(self):
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")] #https://stackoverflow.com/questions/1398022/looping-over-all-member-variables-of-a-class-in-python
        dict = {}
        self.__dict__.items()
        for attribute, value in self.__dict__.items():
            dict[attribute] = value
        return dict
    
class Spel(SamleObjekt):
    def __init__(self, name, sold_price, current_price, kategori, franchise, difficulty):
        super().__init__(name, sold_price, current_price, kategori)
        self.franchise = franchise
        self.difficulty = difficulty

class Film(SamleObjekt):
    def __init__(self, name, sold_price, current_price, kategori, franchise, lenght):
        super().__init__(name, sold_price, current_price, kategori)
        self.franchise = franchise
        self.lenght = lenght

class Datamaskin(SamleObjekt):
    def __init__(self, name, sold_price, current_price, kategori, gPU, cPU, rAM):
        super().__init__(name, sold_price, current_price, kategori)
        self.gPU = gPU
        self.cPU = cPU
        self.rAM = rAM


def loadJSON(file_path):
    with open(file_path) as json_file:
        file_contents = json_file.read()
    dict = json.loads(file_contents)
    return dict

def writeJSON(file_path, loaded_Json):
    with open(file_path, "w") as json_file:
            json.dump(loaded_Json, json_file, indent=4)

def InitializeAllProducts(products_path = "samle.json"):
    productsData = loadJSON(products_path)
    productsDic = {}
    for product in productsData:
        if productsData[product]["kategori"] == "spel":
            productsDic[product] = Spel(name=product, 
                                    sold_price = productsData[product]["sold_price"],
                                    current_price = productsData[product]["current_price"],
                                    kategori = productsData[product]["kategori"],
                                    franchise = productsData[product]["franchise"],
                                    difficulty = productsData[product]["difficulty"],
                                    )
        if productsData[product]["kategori"] == "film":
            productsDic[product] = Film(name=product, 
                                    sold_price = productsData[product]["sold_price"],
                                    current_price = productsData[product]["current_price"],
                                    kategori = productsData[product]["kategori"],
                                    franchise = productsData[product]["franchise"],
                                    lenght = productsData[product]["lenght"],
                                    )
        if productsData[product]["kategori"] == "datamaskin":
            productsDic[product] = Datamaskin(name=product, 
                                    sold_price = productsData[product]["sold_price"],
                                    current_price = productsData[product]["current_price"],
                                    kategori = productsData[product]["kategori"],
                                    gPU = productsData[product]["gPU"],
                                    cPU = productsData[product]["cPU"],
                                    rAM = productsData[product]["rAM"],
                                    )
    return productsDic

productsDic = InitializeAllProducts()

def writeAllProductsToJson(file_path = "samle.json"):
    products_data = {}
    for (key, product) in productsDic.items():
        products_data[key] = product.toDict()
    writeJSON(file_path, products_data)

def addNewProduct(name = None, sold_price = None, current_price = None, kategori = None, franchise = None, difficulty = None, lenght = None, gPU = None, cPU = None, rAM = None):
    if kategori == "spel":
        product = Spel(name, sold_price, current_price, kategori, franchise, difficulty)
    elif kategori == "film":
        product = Film(name, sold_price, current_price, kategori, franchise, lenght)
    elif kategori == "datamaskin":
        product = Datamaskin(name, sold_price, current_price, kategori, gPU, cPU, rAM)
    
    productsDic[name] = product
    writeAllProductsToJson()  

def removeProduct(product):
    productsDic.pop(product, None)
    writeAllProductsToJson()

# Kan også brukes til å endre på verdier av objektet.
addNewProduct(name = "Fortnite Battle Royale", sold_price = 250, current_price = 200, kategori = "spel", franchise = "Fortnite", difficulty = "Hard")
addNewProduct(name = "Spider-Man: No Way Home", sold_price = 69, current_price = 59, kategori = "film", franchise = "Marvel", lenght = 152)
addNewProduct(name = "Acer Aspire", sold_price = 12560, current_price = 87590, kategori = "datamaskin", cPU = "Intel Inside I-...", gPU="NVidia RTX 4090-ti", rAM=64)

# Del C

# productsDic["Plakat"] = None
class TestSum(unittest.TestCase): 

    def test_if_products_is_instance(self): # Sjekker at alle verdiene i ordboken productsDic er Sanne.
        for product in productsDic:
            self.assertTrue(productsDic[product], "is False or None")
            # self.assertTrue(productsDic[product].sold_price, "is False or None") #Sjekker om objektet har en verdi for sold_price

    def test_if_products_has_values_of_None(self): 
        for product in productsDic:
            # print(productsDic[product].__dict__) #https://stackoverflow.com/questions/2675028/list-attributes-of-an-object
            for value in productsDic[product].__dict__.values():
                self.assertTrue(value, "is Null") 
if __name__ == '__main__':
    unittest.main()