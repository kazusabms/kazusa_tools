# -*- encoding: utf-8 -*-
#!/usr/bin/env python
'''
@file        :mainwindow.py
@describe    :
@time        :2022/09/16 16:42:44
@author      :touma_kazusa
@versions    :1.0
'''
import sys
try:
    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets
except ImportError:
    from PyQt5 import QtGui
    from PyQt5 import QtCore
    from PyQt5 import QtWidgets




class Kazusa_Tools_Ui(QtWidgets.QWidget):
    def __init__(self):
        super(Kazusa_Tools_Ui,self).__init__()
        self.setWindowTitle(u"Kazusa_tools_1.0")
        self.resize(450,400)
        
        
        self.create_connections()
        self.create_widgets()
        self.create_layouts()
        
        
        
    def create_widgets(self):
        self.model_button = QtWidgets.QRadioButton(u'model')
        self.rig_button = QtWidgets.QRadioButton(u'rig')
        self.animation_button = QtWidgets.QRadioButton(u'aniamtion')
        self.fx_button = QtWidgets.QRadioButton(u'fx')

        self.close_btn = QtWidgets.QPushButton(u'close')
        self.close_btn.close()

        
        



    def create_layouts(self):
        self.left_layout = QtWidgets.QColumnView()
        # self.left_layout.geometry[(190,70),250*290]
        self.modules_layout = QtWidgets.QFormLayout()
        self.modules_layout.setContentsMargins(30,50,30,20)
        self.modules_layout.setHorizontalSpacing(40)
        self.modules_layout.setVerticalSpacing(20)


        
        # self.modules_layout.addWidget
        self.modules_layout.addRow(self.model_button)
        self.modules_layout.addRow(self.rig_button)
        self.modules_layout.addRow(self.animation_button)
        self.modules_layout.addRow(self.fx_button)

        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.main_layout.addLayout(self.modules_layout)



    def create_connections(self):
        pass


if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    try:

        d.close()
        d.deleteLater()           #判断窗口已经打开，如果打开了就删掉
    except:
        pass 
    d=Kazusa_Tools_Ui()
    d.show()
    sys.exit(app.exec_())   
    
