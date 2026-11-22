# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        """ PyInstaller compatibility """
        return f"{os.path.join(sys._MEIPASS, relative_path).replace(os.sep, '/')}"
    else:
        # 개발 환경에서는 절대 경로에서 리소스를 찾음
        return os.path.join(os.path.abspath("/"), relative_path)

checkbox_off_path = resource_path("gui/images/svg_icons/checkbox_off.svg")
checkbox_on_path = resource_path("gui/images/svg_icons/checkbox_on.svg")

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1010, 755)
        MainPages.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(MainPages)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.pages.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.pages.setLineWidth(2)

        # page_1
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        font = QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.page_1.setFont(font)
        self.page_1.setStyleSheet(u"")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(500, 300))
        self.welcome_base.setMaximumSize(QSize(500, 300))
        self.welcome_base.setStyleSheet(u"background: transparent;")
        self.welcome_base.setFrameShape(QFrame.Shape.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Shadow.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(250, 250))
        self.logo.setMaximumSize(QSize(250, 250))
        self.logo.setFrameShape(QFrame.Shape.NoFrame)
        self.logo.setFrameShadow(QFrame.Shadow.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)
        self.center_page_layout.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)
        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(500, 50))
        self.label.setMaximumSize(QSize(500, 50))
        self.label.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.center_page_layout.addWidget(self.label)
        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignmentFlag.AlignHCenter)
        self.pushButton = QPushButton(self.page_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 45))
        self.pushButton.setMaximumSize(QSize(200, 45))
        self.pushButton.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.page_1_layout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)
        self.pages.addWidget(self.page_1)

        # page_2
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.page_3_layout = QVBoxLayout(self.page_2)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.verticalFrame = QFrame(self.page_2)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.verticalFrame.setStyleSheet(u"background: transparent;")
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.info_label_2 = QLabel(self.verticalFrame)
        self.info_label_2.setObjectName(u"info_label_2")
        self.info_label_2.setMinimumSize(QSize(0, 200))
        self.info_label_2.setMaximumSize(QSize(16777215, 200))
        self.info_label_2.setFont(font)
        self.info_label_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.info_label_2.setStyleSheet(u"")
        self.info_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label_2.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.verticalLayout_2.addWidget(self.info_label_2)
        self.horizontalFrame_4 = QFrame(self.verticalFrame)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        self.horizontalFrame_4.setMinimumSize(QSize(0, 60))
        self.horizontalFrame_4.setMaximumSize(QSize(16777215, 60))
        self.horizontalFrame_4.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.path_lineEdit_2 = QLineEdit(self.horizontalFrame_4)
        self.path_lineEdit_2.setObjectName(u"path_lineEdit_2")
        self.path_lineEdit_2.setMinimumSize(QSize(0, 35))
        self.path_lineEdit_2.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.horizontalLayout.addWidget(self.path_lineEdit_2, 0, Qt.AlignmentFlag.AlignTop)
        self.path_button_2 = QPushButton(self.horizontalFrame_4)
        self.path_button_2.setObjectName(u"path_button_2")
        self.path_button_2.setMinimumSize(QSize(150, 35))
        self.path_button_2.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.horizontalLayout.addWidget(self.path_button_2, 0, Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_2.addWidget(self.horizontalFrame_4)
        self.progressBar_2 = QProgressBar(self.verticalFrame)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(0)
        self.verticalLayout_2.addWidget(self.progressBar_2)
        self.frame_3 = QFrame(self.verticalFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.image_output_2 = QLabel(self.frame_3)
        self.image_output_2.setScaledContents(False)
        self.image_output_2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image_output_2.setObjectName(u"image_output_2")
        self.image_output_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_3.addWidget(self.image_output_2)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalFrame = QFrame(self.verticalFrame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 45))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 45))
        self.horizontalFrame.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Back_button_2 = QPushButton(self.horizontalFrame)
        self.Back_button_2.setObjectName(u"Back_button_2")
        self.Back_button_2.setMinimumSize(QSize(150, 35))
        self.Back_button_2.setMaximumSize(QSize(150, 35))
        self.Back_button_2.setStyleSheet("font-size: 24px;")  # 글자 크기 변경        
        self.horizontalLayout_4.addWidget(self.Back_button_2, 0, Qt.AlignmentFlag.AlignLeft)
        self.Next_button_2 = QPushButton(self.horizontalFrame)
        self.Next_button_2.setObjectName(u"Next_button_2")
        self.Next_button_2.setMinimumSize(QSize(150, 35))
        self.Next_button_2.setMaximumSize(QSize(150, 35))
        self.Next_button_2.setStyleSheet("""QPushButton {
                                                font-size: 24px;
                                                background-color: #ffffff;  /* 기본 배경색 */
                                                color: #6B7894;              /* 기본 텍스트 색 */}
                                        QPushButton:disabled {
                                                font-size: 24px;
                                                background-color: #ffffff;  /* 비활성화 배경색 */
                                                color: #cccccc;             /* 비활성화 텍스트 색 */}""")  # 글자 크기 변경
        self.Next_button_2.setEnabled(False)
        self.horizontalLayout_4.addWidget(self.Next_button_2)
        self.verticalLayout_2.addWidget(self.horizontalFrame)
        self.page_3_layout.addWidget(self.verticalFrame)
        self.pages.addWidget(self.page_2)
        
        # page_3
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setKerning(False)
        self.page_3.setFont(font4)
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalFrame1 = QFrame(self.page_3)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        font5 = QFont()
        font5.setPointSize(9)
        font5.setKerning(True)
        self.verticalFrame1.setFont(font5)
        self.verticalFrame1.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.verticalFrame1.setStyleSheet(u"background: transparent;")
        self.gridLayout_3 = QGridLayout(self.verticalFrame1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.info_label_3 = QLabel(self.verticalFrame1)
        self.info_label_3.setObjectName(u"info_label_3")
        self.info_label_3.setMinimumSize(QSize(0, 200))
        self.info_label_3.setMaximumSize(QSize(16777215, 200))
        self.info_label_3.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.info_label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label_3.setStyleSheet("font-size: 24px;")  # 글자 크기 변경 
        self.gridLayout_3.addWidget(self.info_label_3, 0, 0, 1, 1)
        self.horizontalFrame_5 = QFrame(self.verticalFrame1)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        self.horizontalFrame_5.setMinimumSize(QSize(0, 45))
        self.horizontalFrame_5.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Back_button_3 = QPushButton(self.horizontalFrame_5)
        self.Back_button_3.setObjectName(u"Back_button_3")
        self.Back_button_3.setMinimumSize(QSize(150, 35))
        self.Back_button_3.setMaximumSize(QSize(150, 35))
        self.Back_button_3.setStyleSheet("font-size: 24px;")  # 글자 크기 변경 
        self.horizontalLayout_12.addWidget(self.Back_button_3, 0, Qt.AlignmentFlag.AlignLeft)
        self.Next_button_3 = QPushButton(self.horizontalFrame_5)
        self.Next_button_3.setObjectName(u"Next_button_3")
        self.Next_button_3.setMinimumSize(QSize(150, 35))
        self.Next_button_3.setMaximumSize(QSize(150, 35))
        self.Next_button_3.setStyleSheet("font-size: 24px;")  # 글자 크기 변경 
        self.horizontalLayout_12.addWidget(self.Next_button_3)
        self.gridLayout_3.addWidget(self.horizontalFrame_5, 2, 0, 1, 1)
        self.gridFrame = QFrame(self.verticalFrame1)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridLayout_2 = QGridLayout(self.gridFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.A_image_output_3 = QLabel(self.gridFrame)
        self.A_image_output_3.setObjectName(u"A_image_output_3")
        self.A_image_output_3.setMinimumSize(450, 600)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.A_image_output_3.sizePolicy().hasHeightForWidth())
        self.A_image_output_3.setSizePolicy(sizePolicy1)
        self.gridLayout_2.addWidget(self.A_image_output_3, 1, 0, 1, 1)
        self.B_button_3 = QRadioButton(self.gridFrame)
        self.B_button_3.setObjectName(u"B_button_3")
        self.B_button_3.setMinimumSize(QSize(0, 35))
        self.B_button_3.setMaximumSize(QSize(16777215, 35))
        self.B_button_3.setStyleSheet(f"""QRadioButton {{font-size: 24px;}}
                                        QRadioButton::indicator {{
                                                width: 24px;
                                                height: 24px;}}
                                        QRadioButton::indicator:unchecked {{
                                                image: url({checkbox_off_path});}}
                                        QRadioButton::indicator:checked {{
                                                image: url({checkbox_on_path});}}""")
        self.gridLayout_2.addWidget(self.B_button_3, 0, 1, 1, 1)
        self.C_image_output_3 = QLabel(self.gridFrame)
        self.C_image_output_3.setObjectName(u"C_image_output_3")
        self.C_image_output_3.setMinimumSize(450, 600)
        sizePolicy1.setHeightForWidth(self.C_image_output_3.sizePolicy().hasHeightForWidth())
        self.C_image_output_3.setSizePolicy(sizePolicy1)
        self.gridLayout_2.addWidget(self.C_image_output_3, 1, 2, 1, 1)
        self.A_button_3 = QRadioButton(self.gridFrame)
        self.A_button_3.setObjectName(u"A_button_3")
        self.A_button_3.setMinimumSize(QSize(0, 35))
        self.A_button_3.setMaximumSize(QSize(16777215, 35))
        self.A_button_3.setChecked(True)
        self.A_button_3.setStyleSheet(f"""QRadioButton {{font-size: 24px;}}
                                        QRadioButton::indicator {{
                                                width: 24px;
                                                height: 24px;}}
                                        QRadioButton::indicator:unchecked {{
                                                image: url({checkbox_off_path});}}
                                        QRadioButton::indicator:checked {{
                                                image: url({checkbox_on_path});}}""")
        self.gridLayout_2.addWidget(self.A_button_3, 0, 0, 1, 1)
        self.C_button_3 = QRadioButton(self.gridFrame)
        self.C_button_3.setObjectName(u"C_button_3")
        self.C_button_3.setMinimumSize(QSize(0, 35))
        self.C_button_3.setMaximumSize(QSize(16777215, 35))
        self.C_button_3.setStyleSheet(f"""QRadioButton {{font-size: 24px;}}
                                        QRadioButton::indicator {{
                                                width: 24px;
                                                height: 24px;}}
                                        QRadioButton::indicator:unchecked {{
                                                image: url({checkbox_off_path});}}
                                        QRadioButton::indicator:checked {{
                                                image: url({checkbox_on_path});}}""")
        self.gridLayout_2.addWidget(self.C_button_3, 0, 2, 1, 1)
        self.B_image_output_3 = QLabel(self.gridFrame)
        self.B_image_output_3.setObjectName(u"B_image_output_3")
        self.B_image_output_3.setMinimumSize(450, 600)
        sizePolicy1.setHeightForWidth(self.B_image_output_3.sizePolicy().hasHeightForWidth())
        self.B_image_output_3.setSizePolicy(sizePolicy1)
        self.gridLayout_2.addWidget(self.B_image_output_3, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.gridFrame, 1, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.verticalFrame1)
        self.pages.addWidget(self.page_3)

        # page_4
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_29 = QVBoxLayout(self.page_4)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalFrame_4 = QFrame(self.page_4)
        self.verticalFrame_4.setObjectName(u"verticalFrame_4")
        self.verticalFrame_4.setStyleSheet(u"background: transparent;")
        self.gridLayout_8 = QGridLayout(self.verticalFrame_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_18 = QLabel(self.verticalFrame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 150))
        self.label_18.setMaximumSize(QSize(16777215, 150))
        self.label_18.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_18.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.gridLayout_8.addWidget(self.label_18, 0, 0, 1, 1)
        self.gridFrame_3 = QFrame(self.verticalFrame_4)
        self.gridFrame_3.setObjectName(u"gridFrame_3")
        self.gridLayout_7 = QGridLayout(self.gridFrame_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.exel_info_4 = QLabel(self.gridFrame_3)
        self.exel_info_4.setObjectName(u"exel_info_4")
        self.exel_info_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.exel_info_4.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.gridLayout_7.addWidget(self.exel_info_4, 0, 3, 1, 1)
        self.image2_output_4 = QLabel(self.gridFrame_3)
        self.image2_output_4.setObjectName(u"image2_output_4")
        self.image2_output_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image2_output_4.setMinimumSize(320, 500)
        self.image2_output_4.setMaximumSize(450, 600)
        self.gridLayout_7.addWidget(self.image2_output_4, 1, 1, 1, 1)
        self.image1_output_4 = QLabel(self.gridFrame_3)
        self.image1_output_4.setObjectName(u"image1_output_4")
        self.image1_output_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image1_output_4.setMinimumSize(320, 500)
        self.image1_output_4.setMaximumSize(450, 600)
        self.gridLayout_7.addWidget(self.image1_output_4, 1, 0, 1, 1)
        self.exel_output_4 = QTableWidget(self.gridFrame_3)
        self.exel_output_4.setObjectName(u"exel_output_4")
        self.exel_output_4.setMinimumSize(QSize(320, 500))
        self.exel_output_4.setMaximumSize(QSize(640, 800))
        self.exel_output_4.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.gridLayout_7.addWidget(self.exel_output_4, 1, 3, 1, 1)
        self.image1_info_4 = QLabel(self.gridFrame_3)
        self.image1_info_4.setObjectName(u"image1_info_4")
        self.image1_info_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.image1_info_4.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.gridLayout_7.addWidget(self.image1_info_4, 0, 0, 1, 1)
        self.image2_info_4 = QLabel(self.gridFrame_3)
        self.image2_info_4.setObjectName(u"image2_info_4")
        self.image2_info_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.image2_info_4.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.gridLayout_7.addWidget(self.image2_info_4, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.gridFrame_3, 1, 0, 1, 1)
        self.horizontalFrame_2 = QFrame(self.verticalFrame_4)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setMinimumSize(QSize(0, 45))
        self.horizontalFrame_2.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Back_button_4 = QPushButton(self.horizontalFrame_2)
        self.Back_button_4.setObjectName(u"Back_button_4")
        self.Back_button_4.setMinimumSize(QSize(150, 35))
        self.Back_button_4.setMaximumSize(QSize(150, 35))
        self.Back_button_4.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.horizontalLayout_7.addWidget(self.Back_button_4, 0, Qt.AlignmentFlag.AlignLeft)
        self.Next_button_4 = QPushButton(self.horizontalFrame_2)
        self.Next_button_4.setObjectName(u"Next_button_4")
        self.Next_button_4.setMinimumSize(QSize(150, 35))
        self.Next_button_4.setMaximumSize(QSize(150, 35))
        self.Next_button_4.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.horizontalLayout_7.addWidget(self.Next_button_4)
        self.gridLayout_8.addWidget(self.horizontalFrame_2, 2, 0, 1, 1)
        self.verticalLayout_29.addWidget(self.verticalFrame_4)
        self.pages.addWidget(self.page_4)
        
        # page_6
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_6 = QVBoxLayout(self.page_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalFrame_3 = QFrame(self.page_6)
        self.verticalFrame_3.setObjectName(u"verticalFrame_3")
        self.verticalFrame_3.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.verticalFrame_3.setStyleSheet(u"background: transparent;")
        self.verticalLayout_14 = QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.info_label_6 = QLabel(self.verticalFrame_3)
        self.info_label_6.setObjectName(u"info_label_6")
        self.info_label_6.setMinimumSize(QSize(0, 300))
        self.info_label_6.setMaximumSize(QSize(16777215, 300))
        self.info_label_6.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.info_label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label_6.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.verticalLayout_14.addWidget(self.info_label_6)
        self.horizontalWidget_7 = QWidget(self.verticalFrame_3)
        self.horizontalWidget_7.setObjectName(u"horizontalWidget_7")
        self.horizontalWidget_7.setMinimumSize(QSize(0, 60))
        self.horizontalWidget_7.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalWidget_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.path_lineEdit_6 = QLineEdit(self.horizontalWidget_7)
        self.path_lineEdit_6.setObjectName(u"path_lineEdit_6")
        self.path_lineEdit_6.setMinimumSize(QSize(0, 35))
        self.path_lineEdit_6.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.horizontalLayout_10.addWidget(self.path_lineEdit_6, 0, Qt.AlignmentFlag.AlignTop)
        self.path_button_6 = QPushButton(self.horizontalWidget_7)
        self.path_button_6.setObjectName(u"path_button_6")
        self.path_button_6.setMinimumSize(QSize(150, 35))
        self.path_button_6.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.horizontalLayout_10.addWidget(self.path_button_6, 0, Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_14.addWidget(self.horizontalWidget_7)
        self.progressBar = QProgressBar(self.verticalFrame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.verticalLayout_14.addWidget(self.progressBar)
        self.frame = QFrame(self.verticalFrame_3)
        self.frame.setObjectName(u"frame")
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_15.addWidget(self.label_15)
        self.verticalLayout_14.addWidget(self.frame)
        self.horizontalFrame_41 = QFrame(self.verticalFrame_3)
        self.horizontalFrame_41.setObjectName(u"horizontalFrame_41")
        self.horizontalFrame_41.setMinimumSize(QSize(0, 45))
        self.horizontalFrame_41.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalFrame_41)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Back_button_6 = QPushButton(self.horizontalFrame_41)
        self.Back_button_6.setObjectName(u"Back_button_6")
        self.Back_button_6.setMinimumSize(QSize(150, 35))
        self.Back_button_6.setMaximumSize(QSize(150, 35))
        self.Back_button_6.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.horizontalLayout_11.addWidget(self.Back_button_6, 0, Qt.AlignmentFlag.AlignLeft)
        self.Next_button_6 = QPushButton(self.horizontalFrame_41)
        self.Next_button_6.setObjectName(u"Next_button_6")
        self.Next_button_6.setMinimumSize(QSize(150, 35))
        self.Next_button_6.setMaximumSize(QSize(150, 35))
        self.Next_button_6.setStyleSheet("""QPushButton {
                                                font-size: 24px;
                                                background-color: #ffffff;  /* 기본 배경색 */
                                                color: #6B7894;              /* 기본 텍스트 색 */}
                                        QPushButton:disabled {
                                                font-size: 24px;
                                                background-color: #ffffff;  /* 비활성화 배경색 */
                                                color: #cccccc;             /* 비활성화 텍스트 색 */}""") 
        self.Next_button_6.setEnabled(False)
        self.horizontalLayout_11.addWidget(self.Next_button_6)
        self.verticalLayout_14.addWidget(self.horizontalFrame_41)
        self.verticalLayout_6.addWidget(self.verticalFrame_3)
        self.pages.addWidget(self.page_6)

        # page_7
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_25 = QVBoxLayout(self.page_7)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.info_label_71 = QLabel(self.page_7)
        self.info_label_71.setObjectName(u"info_label_71")
        self.info_label_71.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.info_label_71.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.verticalLayout_24.addWidget(self.info_label_71)
        self.path_lineEdit_7 = QLineEdit(self.page_7)
        self.path_lineEdit_7.setObjectName(u"path_lineEdit_7")
        self.path_lineEdit_7.setMinimumSize(QSize(0, 200))
        self.path_lineEdit_7.setMaximumSize(QSize(16777215, 200))
        self.path_lineEdit_7.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.path_lineEdit_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_24.addWidget(self.path_lineEdit_7)
        self.info_label_72 = QLabel(self.page_7)
        self.info_label_72.setObjectName(u"info_label_72")
        self.info_label_72.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.info_label_72.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.verticalLayout_24.addWidget(self.info_label_72)
        self.verticalLayout_25.addLayout(self.verticalLayout_24)
        self.horizontalFrame_7 = QFrame(self.page_7)
        self.horizontalFrame_7.setObjectName(u"horizontalFrame_7")
        self.horizontalFrame_7.setMinimumSize(QSize(0, 45))
        self.horizontalFrame_7.setMaximumSize(QSize(16777215, 45))
        self.horizontalFrame_7.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalFrame_7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.Back_button_7 = QPushButton(self.horizontalFrame_7)
        self.Back_button_7.setObjectName(u"Back_button_7")
        self.Back_button_7.setMinimumSize(QSize(150, 35))
        self.Back_button_7.setMaximumSize(QSize(150, 35))
        self.Back_button_7.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.horizontalLayout_17.addWidget(self.Back_button_7, 0, Qt.AlignmentFlag.AlignLeft)
        self.Home_button_7 = QPushButton(self.horizontalFrame_7)
        self.Home_button_7.setObjectName(u"Home_button_7")
        self.Home_button_7.setMinimumSize(QSize(150, 35))
        self.Home_button_7.setMaximumSize(QSize(150, 35))
        self.Home_button_7.setStyleSheet("font-size: 24px;")  # 글자 크기 변경
        self.horizontalLayout_17.addWidget(self.Home_button_7)
        self.verticalLayout_25.addWidget(self.horizontalFrame_7)
        self.pages.addWidget(self.page_7)

        # page_5
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_19 = QVBoxLayout(self.page_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalFrame_31 = QFrame(self.page_5)
        self.verticalFrame_31.setObjectName(u"verticalFrame_31")
        self.verticalFrame_31.setStyleSheet(u"background: transparent;")
        self.verticalLayout_22 = QVBoxLayout(self.verticalFrame_31)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.info_label_5 = QLabel(self.verticalFrame_31)
        self.info_label_5.setObjectName(u"info_label_5")
        self.info_label_5.setMinimumSize(QSize(0, 200))
        self.info_label_5.setMaximumSize(QSize(16777214, 200))
        self.info_label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label_5.setStyleSheet("font-size: 24px;")  # 글자 크기 변경 
        self.verticalLayout_22.addWidget(self.info_label_5)
        self.gridFrame_2 = QFrame(self.verticalFrame_31)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridLayout_6 = QGridLayout(self.gridFrame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalFrame_5 = QFrame(self.gridFrame_2)
        self.verticalFrame_5.setObjectName(u"verticalFrame_5")
        self.verticalLayout_13 = QVBoxLayout(self.verticalFrame_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.image1_button_5 = QCheckBox(self.verticalFrame_5)
        self.image1_button_5.setObjectName(u"image1_button_5")
        self.image1_button_5.setStyleSheet(f"""QCheckBox {{font-size: 24px;}}
                                                QCheckBox::indicator {{
                                                        width: 24px;
                                                        height: 24px;}}
                                                QCheckBox::indicator:unchecked {{
                                                        image: url({checkbox_off_path});}}
                                                QCheckBox::indicator:checked {{
                                                        image: url({checkbox_on_path});}}""") 
        self.verticalLayout_13.addWidget(self.image1_button_5, 0, Qt.AlignmentFlag.AlignLeft)
        self.image2_button_5 = QCheckBox(self.verticalFrame_5)
        self.image2_button_5.setObjectName(u"image2_button_5")
        self.image2_button_5.setStyleSheet(f"""QCheckBox {{font-size: 24px;}}
                                                QCheckBox::indicator {{
                                                        width: 24px;
                                                        height: 24px;}}
                                                QCheckBox::indicator:unchecked {{
                                                        image: url({checkbox_off_path});}}
                                                QCheckBox::indicator:checked {{
                                                        image: url({checkbox_on_path});}}""") 
        self.verticalLayout_13.addWidget(self.image2_button_5, 0, Qt.AlignmentFlag.AlignLeft)
        self.exel_button_5 = QCheckBox(self.verticalFrame_5)
        self.exel_button_5.setObjectName(u"exel_button_5")
        self.exel_button_5.setStyleSheet(f"""QCheckBox {{font-size: 24px;}}
                                                QCheckBox::indicator {{
                                                        width: 24px;
                                                        height: 24px;}}
                                                QCheckBox::indicator:unchecked {{
                                                        image: url({checkbox_off_path});}}
                                                QCheckBox::indicator:checked {{
                                                        image: url({checkbox_on_path});}}""") 
        self.verticalLayout_13.addWidget(self.exel_button_5, 0, Qt.AlignmentFlag.AlignLeft)
        self.gridLayout_6.addWidget(self.verticalFrame_5, 1, 1, 1, 1)
        self.frame_2 = QFrame(self.gridFrame_2)
        self.frame_2.setObjectName(u"frame_2")
        self.verticalLayout_21 = QVBoxLayout(self.frame_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.gridLayout_6.addWidget(self.frame_2, 1, 2, 1, 1)
        self.frame1 = QFrame(self.gridFrame_2)
        self.frame1.setObjectName(u"frame1")
        self.verticalLayout_20 = QVBoxLayout(self.frame1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_6.addWidget(self.frame1, 1, 0, 1, 1)
        self.verticalLayout_22.addWidget(self.gridFrame_2)
        self.horizontalFrame_6 = QFrame(self.verticalFrame_31)
        self.horizontalFrame_6.setObjectName(u"horizontalFrame_6")
        self.horizontalFrame_6.setMinimumSize(QSize(0, 45))
        self.horizontalFrame_6.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.Back_button_5 = QPushButton(self.horizontalFrame_6)
        self.Back_button_5.setObjectName(u"Back_button_5")
        self.Back_button_5.setMinimumSize(QSize(150, 35))
        self.Back_button_5.setMaximumSize(QSize(150, 35))
        self.Back_button_5.setStyleSheet("font-size: 24px;")  # 글자 크기 변경 
        self.horizontalLayout_15.addWidget(self.Back_button_5, 0, Qt.AlignmentFlag.AlignLeft)
        self.Next_button_5 = QPushButton(self.horizontalFrame_6)
        self.Next_button_5.setObjectName(u"Next_button_5")
        self.Next_button_5.setMinimumSize(QSize(150, 35))
        self.Next_button_5.setMaximumSize(QSize(150, 35))
        self.Next_button_5.setStyleSheet("""QPushButton {
                                                font-size: 24px;
                                                background-color: #ffffff;  /* 기본 배경색 */
                                                color: #6B7894;              /* 기본 텍스트 색 */}
                                        QPushButton:disabled {
                                                font-size: 24px;
                                                background-color: #ffffff;  /* 비활성화 배경색 */
                                                color: #cccccc;             /* 비활성화 텍스트 색 */}""") 
        self.Next_button_5.setEnabled(False)
        self.horizontalLayout_15.addWidget(self.Next_button_5)
        self.verticalLayout_22.addWidget(self.horizontalFrame_6)
        self.verticalLayout_19.addWidget(self.verticalFrame_31)
        self.pages.addWidget(self.page_5)
        self.horizontalLayout_2.addWidget(self.pages)
        self.retranslateUi(MainPages)
        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p>Welcome to Yippee Size Calculator</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainPages", u"Start!", None))
        self.info_label_2.setText(QCoreApplication.translate("MainPages", u"This is the setting step.\n\n\u203b Select one image. \u203b", None))
        self.path_button_2.setText(QCoreApplication.translate("MainPages", u"click here", None))
        self.image_output_2.setText(QCoreApplication.translate("MainPages", u"", None))
        self.Back_button_2.setText(QCoreApplication.translate("MainPages", u"Back", None))
        self.Next_button_2.setText(QCoreApplication.translate("MainPages", u"Next", None))
        self.info_label_71.setText(QCoreApplication.translate("MainPages", u"Success!\n"
"\n"
"The image analysis is completed.\n"
"The analyzed files are stored in the following path.", None))
        self.info_label_72.setText(QCoreApplication.translate("MainPages", u"Click 'Home' to end the analysis and move home.", None))
        self.Back_button_7.setText(QCoreApplication.translate("MainPages", u"Back", None))
        self.Home_button_7.setText(QCoreApplication.translate("MainPages", u"Home", None))
        self.label_18.setText(QCoreApplication.translate("MainPages", u"These are results of your image. We provide three types of results.\n"
"Click \u201cBack\u201d to test another image in setting step.", None))
        self.exel_info_4.setText(QCoreApplication.translate("MainPages", u"Excel file\n"
"", None))
        self.image2_output_4.setText(QCoreApplication.translate("MainPages", u"", None))
        self.image1_output_4.setText(QCoreApplication.translate("MainPages", u"", None))
        self.image1_info_4.setText(QCoreApplication.translate("MainPages", u"Image option \u2460 \n"
"Raw + border + number \n"
"", None))
        self.image2_info_4.setText(QCoreApplication.translate("MainPages", u"Image option \u2461 \n"
"Binary + number\n"
"", None))
        self.Back_button_4.setText(QCoreApplication.translate("MainPages", u"Back", None))
        self.Next_button_4.setText(QCoreApplication.translate("MainPages", u"Next", None))
        self.info_label_6.setText(QCoreApplication.translate(
    "MainPages",
    u"\n"
    "This is the analysis step.\n"
    "\n"
    "\u203b Select Folder for analysis. \u203b\n" 
    "Allowed structure: “Folder” > Subfolder > Image file.\n"
    "\n"
    "If you analyze a folder that has already been analyzed, the newly analyzed results will replace the existing results.",
    None
))
        self.path_button_6.setText(QCoreApplication.translate("MainPages", u"click here", None))
        self.label_15.setText("")
        self.Back_button_6.setText(QCoreApplication.translate("MainPages", u"Back", None))
        self.Next_button_6.setText(QCoreApplication.translate("MainPages", u"Next", None))
        self.info_label_3.setText(QCoreApplication.translate("MainPages", u"\n"
"Select the image in which the edge of the leaf most closely matches the red line.\n"
"", None))
        self.Back_button_3.setText(QCoreApplication.translate("MainPages", u"Back", None))
        self.Next_button_3.setText(QCoreApplication.translate("MainPages", u"Next", None))
        self.A_image_output_3.setText(QCoreApplication.translate("MainPages", u"", None))
        self.B_button_3.setText(QCoreApplication.translate("MainPages", None))
        self.C_image_output_3.setText(QCoreApplication.translate("MainPages", u"", None))
        self.A_button_3.setText(QCoreApplication.translate("MainPages", None))
        self.C_button_3.setText(QCoreApplication.translate("MainPages", None))
        self.B_image_output_3.setText(QCoreApplication.translate("MainPages", u"", None))
        self.info_label_5.setText(QCoreApplication.translate("MainPages", u"\n"
"This is the step for setting up storage options.\n"
"Click the types of files you want to save.\n"
"(You can select more than one option.)", None))
        self.image1_button_5.setText(QCoreApplication.translate("MainPages", u" Image option \u2460\n"
" Raw + Border + number", None))
        self.image2_button_5.setText(QCoreApplication.translate("MainPages", u" Image option \u2461 \n"
" Binary + number", None))
        self.exel_button_5.setText(QCoreApplication.translate("MainPages", u" Excel file ", None))
        self.Back_button_5.setText(QCoreApplication.translate("MainPages", u"Back", None))
        self.Next_button_5.setText(QCoreApplication.translate("MainPages", u"Next", None))
    # retranslateUi