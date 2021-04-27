import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QAction, QComboBox
from PyQt5.QtGui import QIcon
from combobox import Ui_MainWindow



class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem("Евро")
        self.ui.comboBox.addItem("Доллар США")
        self.ui.comboBox.addItem("Фунт стерлингов")
        self.ui.comboBox.addItem("Швейцарский франк")
        self.ui.comboBox.addItem("Японская иена")
        self.ui.comboBox.addItem("Канадский доллар")
        self.ui.comboBox.addItem("Австралийский доллар")
        self.ui.comboBox.addItem("Датская крона")
        self.ui.comboBox.addItem("Шведская крона")
        self.ui.comboBox.addItem("Российский рубль")

        self.ui.comboBox_2.addItem("Евро")
        self.ui.comboBox_2.addItem("Доллар США")
        self.ui.comboBox_2.addItem("Фунт стерлингов")
        self.ui.comboBox_2.addItem("Швейцарский франк")
        self.ui.comboBox_2.addItem("Японская иена")
        self.ui.comboBox_2.addItem("Канадский доллар")
        self.ui.comboBox_2.addItem("Австралийский доллар")
        self.ui.comboBox_2.addItem("Датская крона")
        self.ui.comboBox_2.addItem("Шведская крона")
        self.ui.comboBox_2.addItem("Российский рубль")

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        s = int(self.ui.comboBox.currentIndex())
        f = int(self.ui.comboBox_2.currentIndex())
        value = self.ui.spinBox.value()
        if s == f:
            self.ui.label_4.setText('Валюты введены некорректно, выберите разные валюты')
            self.ui.label_5.setText('')
            return
        n = 10
        inf = 10 ** 9
        used = [False] * n
        dist = [0] * n
        # EUR	USD	GBP	CHF	JPY	CAD	AUD	DKK	SEK RUB
        graph = [[0, 0.9194, 1.19330, 0.941, 0.0084, 0.6937, 0.6187, 0.1339, 0.0953, 0.01446],
                 [1.028, 0, 1.29790, 1.02350, 0.0091, 0.7545, 0.673, 0.1456, 0.1037, 0.0156],
                 [0.79, 0.72, 0, 0.7876, 0.007, 0.5814, 0.5185, 0.1122, 0.0799, 0.012],
                 [0.99, 0.92, 1.19, 0, 0.0089, 0.7372, 0.6575, 0.1423, 0.1013, 0.01534],
                 [113.06, 104.36, 135.7, 106.73, 0, 82.8151, 73.8652, 15.983, 11.37910, 1.7476],
                 [1.35, 1.25, 1.71, 1.28, 0.009, 0, 0.8919, 0.193, 0.1374, 0.02068],
                 [1.52, 1.4, 1.92, 1.43, 0.011, 1.05, 0, 0.2164, 0.1541, 0.02357],
                 [7.086, 6.51, 8.9, 6.66, 0.04, 4.91, 4.37, 0, 0.712, 0.11],
                 [9.95, 9.14, 12.51, 9.36, 0.076, 6.9, 6.15, 0.001, 0, 0.15],
                 [65.69, 60.89, 79.17, 61.93, 0.54, 45.94, 40.31, 8.64, 6.33, 0]]

        p = [-1] * n
        dist[s] = 1
        max_dist = 0
        max_vertex = s
        answer = []

        while True:
            max_dist = 0
            for i in range(n):
                if dist[i] > max_dist and (not used[i]):
                    max_dist = dist[i]
                    max_vertex = i
            if max_dist == 0:
                break
            i = max_vertex
            used[i] = True
            for j in range(n):
                if dist[j] < dist[i] * graph[i][j] and graph[i][j] != -1:
                    dist[j] = dist[i] * graph[i][j]
                    p[j] = i

        g = f
        while g != -1:
            answer.append(g + 1)
            g = p[g]
        answer = answer[::-1]
        currencies = ['Евро', 'Доллар США', 'Фунт стерлингов', 'Швейцарский франк', 'Японская йена', 'Канадский доллар',
                      'Австралийский доллар', 'Датская крона', 'Шведская крона', 'Российский рубль']
        s = currencies[s]
        f = currencies[f]
        a = []

        for r in range(len(answer) - 1):
            a.append(currencies[answer[r] - 1])
            a.append(' -> ')
        a.append(currencies[answer[-1] - 1])

        text = str()
        text = str(value) + ' ' + str(s) + '  ->  ' + str(round(value/dist[currencies.index(f)], 3)) + ' ' + str(f)
        self.ui.label_4.setText(' '.join(a))
        self.ui.label_5.setText(''.join(text))



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1551, 707)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(0, 320, 1551, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 160, 1451, 41))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(4, 120, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 280, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 500, 1551, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 410, 1551, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 369, 1551, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(0, 160, 101, 41))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setRange(1, 100000)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1551, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Самая выгодная конвертация валют"))
        self.label_2.setText(_translate("MainWindow", "Выберите исходную валюту и ее количество"))
        self.label_3.setText(_translate("MainWindow", "Выберите желаемую валюту"))
        self.pushButton.setText(_translate("MainWindow", "Нажмите для вывода самой выгодной конвертации"))




app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
