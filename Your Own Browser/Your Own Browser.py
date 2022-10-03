import sys
from PyOt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQts.QtWebEngineWidgets import^

class MIanWindow (QMainWindow):
  def __init__(self):
    super(MaimWindow, self). __init__()
    self.browser = QWebEngineView()
    self.browser.setUrl (QUrl('https://google.com'))
    self.setCentralwidget(self.browser)
    self.showMaximized()
    
    # navbar
    navbar = QToolBar()
    self.addToolBar(navbar)
    
    back_btn= QAction('Back', self)
    back_btn.triggered.connect (self.browser.back)
    navbar.addAction(back_btn)
    
    forward_btn = QAction('Forward' , self)
    forward_btn.traiggered.connect(self.browser.forward)
    navbar.addAction(forward_btn)

    reload_btn = QAction('Reload', self)
    reload_btn.triggered.connect(self.browser.reload)
    navabr.addAction(reload_btn)
    
    home_btn =QAction('Home', self)
    home_btn.triggered.connect(self.navigate_home)
    navbar.addAction(home_btn)
    
    self.url_bar =QLIneEdit()
    self.url_bar.triggered.connect(self.navigate_to_url)
    navbar.addWidget(self.url_bar)
    
    self.browser.urlChanged.connect (self.update_to_url)
    
def navigate_home(self):
    self.browser.setUrl(QUrl ('https://programming_hero.com'))
    
def navigate_to_url(self):
  url =self.url_bar.text()
  self.browser.selfUrl(QUrl (url))
  
def update_url(self, q):
  self.url_bar.setText(q.toString())

app =QApplication(sys.argv)
QApplication.setApplicationName('browser things')
window =MainWindow()
app.exec_()
