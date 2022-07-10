from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar = QToolBar()
        self.addToolBar(navbar)
        back_button = QAction("Back",self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)
        forward_button = QAction("Forward",self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)
        reload_button = QAction("Reload",self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)
        home_page = QAction("Home",self)
        home_page.triggered.connect(self.homepage)
        navbar.addAction(home_page)
        self.url_bar =QLineEdit()
        self.url_bar.returnPressed.connect(self.url_change)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.change_url)
    def homepage(self): 
        self.browser.setUrl(QUrl("https://realtime-pizza-delivery-app.herokuapp.com/"))    
    def url_change(self):
        url = self.url_bar.text()
        org_url = url.replace(" ","+")
        g_url = f"https://www.google.com/search?q={org_url}"
        if "https://" in url:
           self.browser.setUrl(QUrl(url))
        else:

         self.browser.setUrl(QUrl(g_url)) 
    def change_url(self,q):
        self.url_bar.setText(q.toString())    
app = QApplication(sys.argv)        
QApplication.setApplicationName("Juicy Browser")
window = MainWindow()
app.exec_()
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtWebEngineWidgets import *


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.browser = QWebEngineView()
#         self.browser.setUrl(QUrl('http://google.com'))
#         self.setCentralWidget(self.browser)
#         self.showMaximized()

#         # navbar
#         navbar = QToolBar()
#         self.addToolBar(navbar)

#         back_btn = QAction('Back', self)
#         back_btn.triggered.connect(self.browser.back)
#         navbar.addAction(back_btn)

#         forward_btn = QAction('Forward', self)
#         forward_btn.triggered.connect(self.browser.forward)
#         navbar.addAction(forward_btn)

#         reload_btn = QAction('Reload', self)
#         reload_btn.triggered.connect(self.browser.reload)
#         navbar.addAction(reload_btn)

#         home_btn = QAction('Home', self)
#         home_btn.triggered.connect(self.navigate_home)
#         navbar.addAction(home_btn)

#         self.url_bar = QLineEdit()
#         self.url_bar.returnPressed.connect(self.navigate_to_url)
#         navbar.addWidget(self.url_bar)

#         self.browser.urlChanged.connect(self.update_url)

#     def navigate_home(self):
#         self.browser.setUrl(QUrl('http://programming-hero.com'))

#     def navigate_to_url(self):
#         url = self.url_bar.text()
#         self.browser.setUrl(QUrl(url))

#     def update_url(self, q):
#         self.url_bar.setText(q.toString())


# app = QApplication(sys.argv)
# QApplication.setApplicationName('My Cool Browser')
# window = MainWindow()
# app.exec_()
            