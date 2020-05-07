# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainShop.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


#  Note - After every checkout to previous window (before shop), make sure to add the cart to the user_purchase db
#         because the last transaction is updated according to the last entry in the db


# TODO - Adding previously purchased items (using Vishvesh Function)
#        Can take discount string from discount table and take the first substring

from PyQt5 import QtCore, QtGui, QtWidgets

# from categoryShop import Ui_categoryShopWindow

import sqlite3 , sys
from PyQt5.QtGui import QPixmap 
from samik import SamikWindow


class Ui_mainShopWindow(object):

    def __init__ (self , window, cart, user_id):
        self.mainShopWindow = window
        self.cart = cart
        self.previousCart = []
        self.user_id = user_id
        self.reciept_id = self.getCurrentRecieptId()
        self.purchaseId = self.getCurrentFirstPurchaseId() # initialy first purchase id


    def getCurrentFirstPurchaseId(self):

        # Getting the last reciept_id and incrementing it for the current Purchase Session

        connection = sqlite3.connect("dbms_db.db")
        crsr = connection.cursor()
        query = "SELECT MAX(purchase_id) FROM user_purchases;"
        crsr.execute(query)
        lastPurcchaseId = crsr.fetchall()
        currentPurchaseID = lastPurcchaseId[0][0] + 1
        print("Purchase Id: "+str(currentPurchaseID))
        return currentPurchaseID


    def getCurrentRecieptId(self):

        # Getting the last reciept_id and incrementing it for the current Purchase Session

        connection = sqlite3.connect("dbms_db.db")
        crsr = connection.cursor()
        query = "SELECT MAX(receipt_id) FROM user_purchases;"
        crsr.execute(query)
        lastReciept = crsr.fetchall()
        currentReciept = lastReciept[0][0] + 1
        print("Current Reciept: "+str(currentReciept))
        return currentReciept

    def openCategoryShop(self, category):
        self.window = QtWidgets.QMainWindow()
        self.category = category
        self.ui = Ui_categoryShopWindow(self.window,self.category,self.cart)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, mainShopWindow):
        locationOffset = 300
        mainShopWindow.setObjectName("mainShopWindow")
        mainShopWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(mainShopWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(0,0,1280,720)
        self.backgroundLabel.setObjectName("backgroundLabel")
        backgroundImage = QPixmap('Images/floor.jpg')
        backgroundImage = backgroundImage.scaledToHeight(720)
        self.backgroundLabel.setPixmap(backgroundImage)

        
        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.bgLabel.setText("")
        self.bgLabel.setPixmap(QtGui.QPixmap("Images/shop-map.jpeg"))
        self.bgLabel.setScaledContents(True)
        self.bgLabel.setObjectName("bgLabel")
        self.checkoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkoutButton.setGeometry(QtCore.QRect(160, 120, 431, 41))
        self.checkoutButton.setObjectName("checkoutButton")
        self.addPreviousToCartButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPreviousToCartButton.setGeometry(QtCore.QRect(610, 120, 491, 41))
        self.addPreviousToCartButton.setObjectName("addPreviousToCartButton")
        self.buttonFood = QtWidgets.QPushButton(self.centralwidget)
        self.buttonFood.setGeometry(QtCore.QRect(60, 420, 111, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonFood.setFont(font)
        self.buttonFood.setObjectName("buttonFood")
        self.buttonDrinks = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDrinks.setGeometry(QtCore.QRect(710, 280, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonDrinks.setFont(font)
        self.buttonDrinks.setObjectName("buttonDrinks")
        self.buttonBeautyAndWellness = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBeautyAndWellness.setGeometry(QtCore.QRect(240, 400, 161, 211))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonBeautyAndWellness.setFont(font)
        self.buttonBeautyAndWellness.setObjectName("buttonBeautyAndWellness")
        self.buttonCleaningAndHousehold = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCleaningAndHousehold.setGeometry(QtCore.QRect(1020, 230, 191, 451))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonCleaningAndHousehold.setFont(font)
        self.buttonCleaningAndHousehold.setObjectName("buttonCleaningAndHousehold")
        self.locationBgLabel = QtWidgets.QLabel(self.centralwidget)
        self.locationBgLabel.setGeometry(QtCore.QRect(610, 440, 361, 231))
        self.locationBgLabel.setAutoFillBackground(True)
        self.locationBgLabel.setText("")
        self.locationBgLabel.setStyleSheet("background-color:rgb(255, 0, 255)")
        self.locationBgLabel.setObjectName("locationBgLabel") 
        self.locationTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.locationTextLabel.setGeometry(QtCore.QRect(650, 460, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.locationTextLabel.setFont(font)
        self.locationTextLabel.setObjectName("locationTextLabel")
        self.productNameInput = QtWidgets.QTextEdit(self.centralwidget)
        self.productNameInput.setGeometry(QtCore.QRect(960-locationOffset, 510, 251, 30))
        self.productNameInput.setReadOnly(False)
        self.productNameInput.setObjectName("productNameInput")
        self.productLocationButton = QtWidgets.QPushButton(self.centralwidget)
        self.productLocationButton.setGeometry(QtCore.QRect(1040-locationOffset, 550, 93, 28))
        self.productLocationButton.setObjectName("productLocationButton")
        self.productLocationOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.productLocationOutput.setGeometry(QtCore.QRect(950-locationOffset, 590, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productLocationOutput.setFont(font)
        self.productLocationOutput.setReadOnly(True)
        self.productLocationOutput.setObjectName("productLocationOutput")

        mainShopWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainShopWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        mainShopWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainShopWindow)
        self.statusbar.setObjectName("statusbar")
        mainShopWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(mainShopWindow)
        QtCore.QMetaObject.connectSlotsByName(mainShopWindow)

        # Buttons for category shopping :

        self.buttonCleaningAndHousehold.clicked.connect(lambda: self.openCategoryShop("Cleaning and Household"))
        self.buttonBeautyAndWellness.clicked.connect(lambda: self.openCategoryShop("beauty and wellness"))
        self.buttonDrinks.clicked.connect(lambda: self.openCategoryShop("drinks"))
        self.buttonFood.clicked.connect(lambda: self.openCategoryShop("food"))
        self.buttonCleaningAndHousehold.setStyleSheet("background-color: #FECD96")
        self.buttonBeautyAndWellness.setStyleSheet("background-color: #97FAFC")
        self.buttonDrinks.setStyleSheet("background-color: tomato")
        self.buttonFood.setStyleSheet("background-color: #CA4CF7")



        # For location of the product:

        self.productLocationButton.clicked.connect(self.showProductLocation)

        # Checkout button returns the cart List:

        self.checkoutButton.clicked.connect(self.checkout)

        # Add previously bought items in cart:
        self.addPreviousToCartButton.clicked.connect(self.addPreviousItemsToCart)

    def addPreviousItemsToCart(self):
        db=sqlite3.connect("dbms_db.db")
        cur=db.cursor()
        cur.execute("SELECT product_id,quantity,discount_id,name,category FROM user_purchases NATURAL JOIN products NATURAL JOIN discounts WHERE receipt_id=(SELECT MAX(receipt_id) FROM transactions WHERE user_id=?);",(self.user_id,))
        self.previousCart=cur.fetchall()
        print(self.previousCart)

    def checkout(self):
        
        quantityDict = {} # {product_id : quantity}
        discountDict = {}# same as above and for below
        sellingCost = {}
        beforeDiscountDict = {}
        afterDiscountDict = {}

        samikCart = []

        for p in self.previousCart:
            if(p[0] in quantityDict):
                quantityDict[p[0]] += p[1]
            else:
                quantityDict[p[0]] = p[1]

            if(p[0] not in discountDict):
                discountDict[p[0]] = p[2]

            if(p[0] not in sellingCost):
                db=sqlite3.connect("dbms_db.db")
                cur=db.cursor()
                cur.execute("SELECT selling_cost FROM products where product_id=?;",(p[0],))
                sc=cur.fetchall()
                print("sc=",str(sc))
                sellingCost[p[0]] = sc[0][0]

        for p in self.cart:

            if(p[0] in quantityDict):
                quantityDict[p[0]] = quantityDict[p[0]] + 1
            else:
                quantityDict[p[0]] = 1

            if(p[0] not in discountDict):
                discountDict[p[0]] = p[5]

            if(p[0] not in sellingCost):
                sellingCost[p[0]] = p[4]
        
        for p in quantityDict:

            totalBeforeCost = quantityDict[p] * sellingCost[p]
            discount = 0

            if(discountDict[p] == ''):
                discount = 0
            elif (discountDict[p] == 1):
                discount = 10
            elif(discountDict[p] == 2):
                discount = 15
            elif(discountDict[p] == 3):
                discount = 40
            elif(discountDict[p] == 4):
                discount = 50
            
            totalAfterCost = (int)(totalBeforeCost - (totalBeforeCost * (discount/100)))

            beforeDiscountDict[p] = totalBeforeCost
            afterDiscountDict[p] = totalAfterCost

        for p in quantityDict:
            proInfo = []
            proInfo.append(self.purchaseId)
            proInfo.append(self.user_id)
            proInfo.append(self.reciept_id)
            proInfo.append(p) #product_id
            proInfo.append(quantityDict[p]) #quantity
            if(discountDict[p] == ''): # discount id 1,2,3 (0 if not)
                proInfo.append(0)
            else:
                proInfo.append(discountDict[p])
            proInfo.append(beforeDiscountDict[p]) #before_discount
            proInfo.append(afterDiscountDict[p]) #after_discount

            self.purchaseId = self.purchaseId + 1
            samikCart.append(proInfo)
        
        del self.cart[:] #clearing ther cart and changing it to user_purchase style
        
        for s in samikCart:
            self.cart.append(s)

        print ("Kart bhaiya jo change hai -> : " + str(self.cart))


        self.mainShopWindow.close()
        
        finalwin = SamikWindow(self.cart)
        finalwin.show()
        
        
        

    def showProductLocation(self):

        productName = self.productNameInput.toPlainText()
        productLocation = ""

        if(productName == ""):
            self.productLocationOutput.setPlainText("No product name entered!")
        
        else:

            # Getting the product with the name

            connection = sqlite3.connect("dbms_db.db")
            crsr = connection.cursor()
            fetch_product = "SELECT product_name, location_aisle, location_shelf from map where product_name LIKE '%"+productName+"%';"
            crsr.execute(fetch_product)
            productDetail = crsr.fetchall()
            outputLoc = ""

            if(productDetail == []):
                outputLoc = "Not a Valid Product!"
            else:
                for x in productDetail:
                    print(x)
                    outputLoc+=(str(x[0])+"-> Aisle:"+str(x[1])+" Shelf:"+str(x[2])+"\n")

            self.productLocationOutput.setPlainText(outputLoc)
            



    def retranslateUi(self, mainShopWindow):
        _translate = QtCore.QCoreApplication.translate
        mainShopWindow.setWindowTitle(_translate("mainShopWindow", "shopMain"))
        self.checkoutButton.setText(_translate("MainWindow", "Checkout"))
        self.addPreviousToCartButton.setText(_translate("MainWindow", "Add previously bought items to cart"))
        self.buttonFood.setText(_translate("MainWindow", "Food"))
        self.buttonDrinks.setText(_translate("MainWindow", "Drinks"))
        self.buttonBeautyAndWellness.setText(_translate("MainWindow", "Beauty \n"
" and \n"
" Wellness"))
        self.buttonCleaningAndHousehold.setText(_translate("MainWindow", "Cleaning \n"
" and \n"
" Household"))
        self.productNameInput.setPlaceholderText(_translate("mainShopWindow", "Enter Product Name"))
        self.productLocationButton.setText(_translate("mainShopWindow", "Get Location"))
        self.locationTextLabel.setText(_translate("MainWindow", "Where is my product?"))

class Ui_categoryShopWindow(object):

    def __init__ (self,window,category,cart):
        self.categoryShopWindow = window
        self.category = category
        self.cart = cart
        print(self.category,self.cart)


    def setupUi(self, categoryShopWindow):
        categoryShopWindow.setObjectName("categoryShopWindow")
        categoryShopWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(categoryShopWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(0,0,1280,720)
        self.backgroundLabel.setObjectName("backgroundLabel")
        backgroundImage = QPixmap('Images/cart.jpg')
        backgroundImage = backgroundImage.scaledToHeight(720)
        self.backgroundLabel.setPixmap(backgroundImage)

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(480, 610, 93, 28))
        self.backButton.setObjectName("backButton")
        self.productsLabel = QtWidgets.QLabel(self.centralwidget)
        self.productsLabel.setGeometry(QtCore.QRect(90, 60, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.productsLabel.setFont(font)
        self.productsLabel.setObjectName("productsLabel")
        self.cartLabel = QtWidgets.QLabel(self.centralwidget)
        self.cartLabel.setGeometry(QtCore.QRect(600, 60, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cartLabel.setFont(font)
        self.cartLabel.setObjectName("cartLabel")

        categoryShopWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(categoryShopWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 26))
        self.menubar.setObjectName("menubar")

        categoryShopWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(categoryShopWindow)
        self.statusbar.setObjectName("statusbar")
        categoryShopWindow.setStatusBar(self.statusbar)

        self.retranslateUi(categoryShopWindow)
        QtCore.QMetaObject.connectSlotsByName(categoryShopWindow)

        # Vertical Layout Widget and Layout for Inventory:

        self.verticalLayoutWidgetInventory = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidgetInventory.setGeometry(QtCore.QRect(100, 150, 323, 624))
        self.verticalLayoutWidgetInventory.setObjectName("verticalLayoutWidget")
        
        self.verticalLayoutInventory = QtWidgets.QVBoxLayout(self.verticalLayoutWidgetInventory)
        self.verticalLayoutInventory.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayoutInventory.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutInventory.setObjectName("verticalLayout")

        # Vertical Layout Widget and Layout for Cart:

        self.verticalLayoutWidgetCart = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidgetCart.setGeometry(QtCore.QRect(600, 150, 323, 624))
        self.verticalLayoutWidgetCart.setObjectName("verticalLayoutWidget")
        
        self.verticalLayoutCart = QtWidgets.QVBoxLayout(self.verticalLayoutWidgetCart)
        self.verticalLayoutCart.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayoutCart.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutCart.setObjectName("verticalLayout")

        self.backButton.clicked.connect(self.goBack)


        # --------------------------------------------------
        # Getting the products of the category from the database

        connection = sqlite3.connect("dbms_db.db")
        crsr = connection.cursor()
        fetch_product = "SELECT * from products where category LIKE '"+self.category+"';"
        crsr.execute(fetch_product)
        products = crsr.fetchall()
        print(products)

        self.updateCart() # showing cart whenever category shop opens

        for i in products:
            self.productViewBar = QtWidgets.QHBoxLayout()

            self.productLabel = QtWidgets.QLabel(i[1],self.verticalLayoutWidgetInventory)

            self.productBuyButton = QtWidgets.QPushButton("Add",self.verticalLayoutWidgetInventory)
            self.productBuyButton.setObjectName(str(i[0]))

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.productBuyButton.sizePolicy().hasHeightForWidth())

            productDetails = i
            self.productBuyButton.setSizePolicy(sizePolicy)
            self.productBuyButton.clicked.connect(lambda state, pd=productDetails: self.buyButtonClicked(pd))

            self.productViewBar.addWidget(self.productLabel)
            self.productViewBar.addWidget(self.productBuyButton)

            self.verticalLayoutInventory.addLayout(self.productViewBar)


    def buyButtonClicked(self,pd):
        print(pd)
        self.cart.append(pd)
        print(self.cart)
        self.updateCart()

    def updateCart(self):

        self.clearCart(self.verticalLayoutCart)

        for i in self.cart:
            self.cartViewBar = QtWidgets.QHBoxLayout()

            self.cartLabel = QtWidgets.QLabel(str(i[1]),self.verticalLayoutWidgetCart)

            self.productCancelButton = QtWidgets.QPushButton("Cancel",self.verticalLayoutWidgetCart)
            self.productCancelButton.setObjectName(str(i[0]))

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.productCancelButton.sizePolicy().hasHeightForWidth())
            self.productCancelButton.setSizePolicy(sizePolicy)
            self.productCancelButton.clicked.connect(lambda state, pd=i: self.removeButtonClicked(pd))

            self.cartViewBar.addWidget(self.cartLabel)
            self.cartViewBar.addWidget(self.productCancelButton)

            self.verticalLayoutCart.addLayout(self.cartViewBar)

    def goBack(self):
        self.categoryShopWindow.close()

    def clearCart(self,layout):
            if layout is not None:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
                    else:
                        self.clearCart(item.layout())

    def removeButtonClicked(self,pd):
        self.cart.remove(pd)
        self.updateCart()



    def retranslateUi(self, categoryShopWindow):
        _translate = QtCore.QCoreApplication.translate
        categoryShopWindow.setWindowTitle(_translate("categoryShopWindow", "categoryShop"))
        self.backButton.setText(_translate("categoryShopWindow", "Back"))
        self.productsLabel.setText(_translate("categoryShopWindow", "Products:"))
        self.cartLabel.setText(_translate("categoryShopWindow", "Cart:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainShopWindow = QtWidgets.QMainWindow()
    ui = Ui_mainShopWindow(mainShopWindow,[],9)
    ui.setupUi(mainShopWindow)
    mainShopWindow.show()
    sys.exit(app.exec_())
