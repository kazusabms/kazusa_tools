# -*- encoding: utf-8 -*-
#!/usr/bin/env python
'''
@file        :mainwindow.py
@describe    :
@time        :2022/09/16 16:42:44
@author      :touma_kazusa
@versions    :1.0
'''

from pickle import TRUE
import sys
import os
from turtle import width
try:
    from PySide2.QtWidgets import*
    from PySide2.QtGui import*
    from PySide2.QtCore import*   
except ImportError:
    from PyQt5.QtWidgets import*
    from PyQt5.QtGui import*
    from PyQt5.QtCore import*

class ImaageLabel(QWidget):
    """
        creat image label
    """
    def __init__(self,text,image_path):
        super().__init__()
        # get icon path 
        _path = __file__.decode('gbk') if sys.version_info<(3,0) else __file__
        root = os.path.dirname(os.path.dirname(_path))
        path = os.path.join(root)

        

        lb_image = QLabel()
        
        pixmap = QPixmap(path+image_path).scaled(QSize(50,50))
        lb_image.setPixmap(pixmap)
        lb_image.setAlignment(Qt.AlignCenter)

        lb_text = QLabel()
        lb_text.setText(text)
        lb_text.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPixelSize(20)
        lb_text.setFont(font)

        show_layout = QVBoxLayout()
        show_layout.setContentsMargins(0,0,0,0)

        self.setLayout(show_layout)
        show_layout.addWidget(lb_image)
        show_layout.addWidget(lb_text)

        self.setFixedSize(100,100+20)
        lb_image.setFixedSize(100,100)
        lb_text.setFixedSize(100,20)




class Kazusa_Tools_Ui(QWidget):
    def __init__(self,parent=None):
        super(Kazusa_Tools_Ui,self).__init__(parent)
        self.setWindowTitle(u"Kazusa_tools_1.0")
        self.resize(450,400)
        
        
        self.create_connections()
        self.create_widgets()
        self.create_layouts()
        self.fx_ui()
        self.rig_ui()
        # self.btnstate()
        
    def create_widgets(self):
        self.model_button = QRadioButton('model')
        # self.model_button.setChecked(True)
        self.rig_button = QRadioButton('rig')
        self.rig_button.setChecked(True)
        self.rig_button.toggled.connect(self.rig_ui)
        self.animation_button = QRadioButton('aniamtion')
        self.fx_button = QRadioButton('fx')

        self.close_btn = QPushButton(u'close')
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setGeometry(50,350,100,40)


        self.stack_fx = QWidget()
        self.stack_rig = QWidget()
        self.stack_aniamtion = QWidget()
        self.stack_model =QWidget()

        self.stack_ui = QStackedWidget(self)
        self.stack_ui.addWidget(self.stack_model)
        self.stack_ui.addWidget(self.stack_rig)
        self.stack_ui.addWidget(self.stack_aniamtion)
        self.stack_ui.addWidget(self.stack_fx)
 
    
    def fx_ui(self):
        #create iamge ui 
        fx_layout = QHBoxLayout()
        self.lw = QListWidget()

        imglb = ImaageLabel('aaa','/icons/test.png')
        item = QListWidgetItem()
        item.setSizeHint(imglb.size())
        self.lw.addItem(item)
        self.lw.setItemWidget(item,imglb)
        fx_layout.addWidget(self.lw)
        
        self.stack_fx.setLayout(fx_layout)
        



    def rig_ui(self):
        self.rig_layout = QHBoxLayout()
        self.lw2 = QListWidget()
        imglb_2 =ImaageLabel('bbb','/icons/test.png')
        item2 = QListWidgetItem()
        item2.setSizeHint(imglb_2.size())
        self.lw2.addItem(item2)
        self.lw2.setItemWidget(item2,imglb_2)
        self.rig_layout.addWidget(self.lw2)
        self.main_layout.addLayout(self.rig_layout)
        
        # self.stack_rig.setLayout(self.rig_layout)


    def create_layouts(self):
        
        self.left_layout = QColumnView()
        # self.left_layout.geometry[(190,70),250*290]
        self.modules_layout = QFormLayout()
        self.modules_layout.setContentsMargins(30,50,30,20)
        self.modules_layout.setHorizontalSpacing(40)
        self.modules_layout.setVerticalSpacing(20)



        
        # self.modules_layout.addWidget
        self.modules_layout.addRow(self.model_button)
        self.modules_layout.addRow(self.rig_button)
        self.modules_layout.addRow(self.animation_button)
        self.modules_layout.addRow(self.fx_button)
        self.modules_layout.addWidget(self.close_btn)
        
        
        
        

        self.main_layout = QHBoxLayout(self)
        self.main_layout.addLayout(self.modules_layout)
        self.main_layout.addWidget(self.stack_ui)

        self.setLayout(self.main_layout)
            
        # self.main_layout.addWidget(self.left_layout)
        
        



    def create_connections(self):
        pass
        # self.model_button.toggle.connect(self.stack_model)
        # self.animation_button.toggle.connect(self.stack_aniamtion)
        # self.rig_button.toggled.connect(lambda:self.btnstate(self.rig_button))
        # self.close_btn.clicked.connect(self.rig_ui)
        

    # def btnstate(self,btn):
        # pass
        # if btn.text()=='rig':
        #     if btn.isChecked()==True:
        #         print(btn.text()+"is selected")
        #         self.stack_rig.setLayout(self.rig_layout)


        #     else:
        #         print(btn.text()+'is deselected')
        # else:
        #     pass
if __name__ =="__main__":
    app = QApplication(sys.argv)
    try:

        d.close()
        d.deleteLater()           #判断窗口已经打开，如果打开了就删掉
    except:
        pass 
    d=Kazusa_Tools_Ui()
    d.show()
    sys.exit(app.exec_())   
    
