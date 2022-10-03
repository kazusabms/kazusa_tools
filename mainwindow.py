# -*- encoding: utf-8 -*-
#!/usr/bin/env python
'''
@file        :mainwindow.py
@describe    :
@time        :2022/09/16 16:42:44
@author      :touma_kazusa
@versions    :1.0
'''

from cgi import test
from email.mime import image
from pickle import TRUE
import sys
import os
from turtle import width

try:
    from PyQt5.QtWidgets import*
    from PyQt5.QtGui import*
    from PyQt5.QtCore import*
  
except ImportError:
    from PySide2.QtWidgets import*
    from PySide2.QtGui import*
    from PySide2.QtCore import* 

class ImaageLabel(QWidget):
    """
        creat image label
    """

    def __init__(self, text, image_path):
        super().__init__()
        # get icon path
        icons_path = '\icons'
        _path = __file__.decode('gbk') if sys.version_info < (3, 0) else __file__
        root = os.path.dirname(os.path.dirname(_path))+icons_path
        path = os.path.join(root)

        lb_image = QLabel()

        #set pixmap size 
        pixmap = QPixmap(path + image_path).scaled(QSize(50, 50)) #返回缩放后的新的图片对象
        pixmap.load(path + image_path)
        lb_image.setPixmap(pixmap)
        lb_image.setAlignment(Qt.AlignCenter)

        lb_text = QPushButton()
        lb_text.setText(text)
        # lb_text.setIcon(image_path)
        # lb_text.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPixelSize(20)
        lb_text.setFont(font)

        # lab_btn =QPushButton()

        show_layout = QVBoxLayout()
        show_layout.setContentsMargins(0, 0, 0, 0)    #空间留白设置为零

        self.setLayout(show_layout)
        show_layout.addWidget(lb_image)
        show_layout.addWidget(lb_text)
        # show_layout.addWidget(lab_btn)

        #固定尺寸，set 控件大小
        self.setFixedSize(100, 100 + 20)
        lb_image.setFixedSize(100, 100)
        lb_text.setFixedSize(100, 30)
        

        print(pixmap)
        
class Kazusa_Tools_Ui(QWidget):
    def __init__(self ):
        super(Kazusa_Tools_Ui, self).__init__()
        self.setWindowTitle(u"Kazusa_tools_1.0")
        self.resize(450, 400)

        self.create_connections()
        self.create_widgets()
        self.create_layouts()
        self.model_ui()
        self.fx_ui()
        self.rig_ui()
        self.animation_ui()
        # self.btnstate()

    def create_widgets(self):
        self.model_button = QRadioButton('model')
        self.model_button.setChecked(True)
        self.rig_button = QRadioButton('rig')
        # self.rig_button.setChecked(True)

        self.animation_button = QRadioButton('animation')
        self.fx_button = QRadioButton('fx')

        self.close_btn = QPushButton(u'close')
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setGeometry(50, 350, 100, 40)

        self.rig_button.toggled.connect(lambda :self.btnstate(self.rig_button))
        self.animation_button.toggled.connect(lambda :self.btnstate(self.animation_button))
        self.fx_button.toggled.connect(lambda :self.btnstate(self.fx_button))
        self.model_button.toggled.connect(lambda :self.btnstate(self.model_button))

    
    def add_item(self,text,image_path):
        imglb = ImaageLabel(text,image_path)
        # img_btn = QPushButton(text)
        
        # img_btn.setIcon(imglb)
        
        item = QListWidgetItem()
        
        item.setSizeHint(imglb.size())
        self.lw.addItem(item)
        self.lw.setItemWidget(item, imglb)
        print(image_path)

    def test(self):
        print('test button')

    def fx_ui(self):
        # create iamge ui
        fx_tool_list = ["fx1",'fx2','fx3','fx4']
        
        self.layout = QHBoxLayout()
        self.lw = QListWidget()
        self.lw.setFlow(QListWidget.LeftToRight)  #button left to right
        self.lw.setWrapping(True)
        self.lw.setResizeMode(QListView.Adjust)
        for i in fx_tool_list:
            self.add_item(i,'/test{}.png'.format(fx_tool_list.index(i)))
        self.lw.setItemWidget(self.test)


        self.layout.addWidget(self.lw)
        self.stack_fx.setLayout(self.layout)
        
    def rig_ui(self):
        rig_tool_list = ["rig1",'rig2','rig3','rig4']
        
        self.layout = QHBoxLayout()
        self.lw = QListWidget()
        self.lw.setFlow(QListWidget.LeftToRight)  #button left to right
        self.lw.setWrapping(True)
        self.lw.setResizeMode(QListView.Adjust)
        for i in rig_tool_list:
            self.add_item(i,'/test{}.png'.format(rig_tool_list.index(i)))
    
        self.layout.addWidget(self.lw)
        self.stack_rig.setLayout(self.layout)
        print("rig")
    def animation_ui(self):
        self.layout = QHBoxLayout()
        self.lw = QListWidget()
        self.imglb_test = ImaageLabel('ccc', '/test2.png')
        
        item = QListWidgetItem()
        item.setSizeHint(self.imglb.size())
        self.lw.addItem(item)
        self.lw.setItemWidget(item, self.imglb)
        self.layout.addWidget(self.lw)
        # self.main_layout.addLayout(self.rig_layout)

        self.stack_animation.setLayout(self.layout)
        print("animation")

    def model_ui(self):
        self.layout = QHBoxLayout()
        self.lw = QListWidget()
        self.imglb = ImaageLabel('ddd', '/test1.png')
        item = QListWidgetItem()
        item.setSizeHint(self.imglb.size())
        self.lw.addItem(item)
        self.lw.setItemWidget(item, self.imglb)
        self.layout.addWidget(self.lw)

        self.stack_model.setLayout(self.layout)
        print("model")
    def create_layouts(self):
        self.left_layout = QColumnView()
        # self.left_layout.geometry[(190,70),250*290]
        self.modules_layout = QFormLayout()
        self.modules_layout.setContentsMargins(30, 50, 30, 20)
        self.modules_layout.setHorizontalSpacing(40)
        self.modules_layout.setVerticalSpacing(20)

        # self.modules_layout.addWidget
        self.modules_layout.addRow(self.model_button)
        self.modules_layout.addRow(self.rig_button)
        self.modules_layout.addRow(self.animation_button)
        self.modules_layout.addRow(self.fx_button)
        self.modules_layout.addWidget(self.close_btn)

        self.stack_fx = QWidget()
        self.stack_rig = QWidget()
        self.stack_animation = QWidget()
        self.stack_model = QWidget()

        self.stack_ui = QStackedWidget(self)
        self.stack_ui.addWidget(self.stack_model)
        self.stack_ui.addWidget(self.stack_rig)
        self.stack_ui.addWidget(self.stack_animation)
        self.stack_ui.addWidget(self.stack_fx)

        self.main_layout = QHBoxLayout(self)
        self.main_layout.addLayout(self.modules_layout)
        self.main_layout.addWidget(self.stack_ui)

        self.setLayout(self.main_layout)

        

    def create_connections(self):
        pass


    def btnstate(self,btn):

        if btn.text() == 'model':
            if btn.isChecked() == True:
                print(btn.text() + " is selected")
                # self.stack_model.setLayout(self.layout)
                self.stack_ui.setCurrentIndex(0)

            else:
                print(btn.text() + ' is deselected')
        if btn.text()=='rig':
            if btn.isChecked()==True:
                print(btn.text()+"is selected")
                # self.stack_rig.setLayout(self.layout)
                self.stack_ui.setCurrentIndex(1)


            else:
                print(btn.text()+' is deselected')

        if btn.text() == 'animation':
            if btn.isChecked() == True:
                print(btn.text() + " is selected")
                # self.stack_animation.setLayout(self.layout)
                self.stack_ui.setCurrentIndex(2)


            else:
                print(btn.text() + ' is deselected')

        if btn.text()=='fx':
            if btn.isChecked()==True:
                print(btn.text()+" is selected")
                # self.stack_fx.setLayout(self.layout)
                self.stack_ui.setCurrentIndex(3)
                


            else:
                print(btn.text()+' is deselected')



if __name__ == "__main__":

    app = QApplication(sys.argv)
    try:
        d.close()
        d.deleteLater()  # 判断窗口已经打开，如果打开了就删掉
    except:
        pass
    d = Kazusa_Tools_Ui()
    d.show()
    sys.exit(app.exec_())