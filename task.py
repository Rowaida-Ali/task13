import PyQt5.QtWidgets as qtw
from task13 import Ui_MainWindow
class main_window (qtw.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super ().__init__()
        self.setupUi(self)
        self.price=0



        self.apples.clicked.connect(self.add)
        self.bananas.clicked.connect(self.add2)
        self.mangoes1.clicked.connect(self.add3)
        self.mangoes2_2.clicked.connect(self.add4)
        self.guaves_2.clicked.connect(self.add5)
        self.checkpoint.clicked.connect(self.add6)
    
    def add(self):
        a=2.4
        self.price+=a
        self.price1.setText(str(a))     
    def add2(self): 
        b=6
        self.price+=b
        self.price2.setText (str(b))
    def add3(self):  
        m=7
        self.price+=m
        self.price3.setText (str(m)) 
    def add4(self):  
        m2=4.5
        self. price+=m2
        self.price4.setText (str(m2))
    def add5(self):  
        g=4.5
        self. price+=g
        self.price5.setText (str(g))        
    def  add6(self):
        self.totalprice.setText(str(self.price)) 







app=qtw.QApplication([])
application_window=main_window()
application_window.show()
app.exec()       
        



