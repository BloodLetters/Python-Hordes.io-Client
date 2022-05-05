import sys
import time

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

import CReader
from pypresence.presence import Presence


class main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(main, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.setFixedWidth(CReader.getResolution("w"))
        self.setFixedHeight(CReader.getResolution("h"))
        self.browser.setUrl(QUrl("http://hordes.io"))
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.urlbar = QLineEdit()
        self.show()

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - Playing!" % title)
        self.setWindowIcon(QtGui.QIcon('Data/Icon/icon.png'))

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


client_id = '971570577057935390'
RPC = Presence(client_id, pipe=0)
RPC.connect()
RPC.update(start=int(time.time()), large_image="horde", details="Playing As " + CReader.getFaction())

app = QApplication(sys.argv)
app.setApplicationName("Hordes.io")
window = main()
app.exec_()