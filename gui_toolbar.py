# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Apps\DEV\PROJECTS\KoHighlights\gui_toolbar.ui'
#
# Created: Sun Mar  3 11:56:15 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ToolBar(object):
    def setupUi(self, ToolBar):
        ToolBar.setObjectName("ToolBar")
        ToolBar.resize(864, 75)
        ToolBar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        ToolBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(ToolBar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtGui.QFrame(ToolBar)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.check_btn = QtGui.QToolButton(self.frame)
        self.check_btn.setMinimumSize(QtCore.QSize(80, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../KataLib/:/stuff/exec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check_btn.setIcon(icon)
        self.check_btn.setIconSize(QtCore.QSize(48, 48))
        self.check_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.check_btn.setAutoRaise(True)
        self.check_btn.setObjectName("check_btn")
        self.horizontalLayout.addWidget(self.check_btn)
        self.select_btn = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_btn.sizePolicy().hasHeightForWidth())
        self.select_btn.setSizePolicy(sizePolicy)
        self.select_btn.setMinimumSize(QtCore.QSize(80, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/stuff/folder_reader.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_btn.setIcon(icon1)
        self.select_btn.setIconSize(QtCore.QSize(48, 48))
        self.select_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.select_btn.setAutoRaise(True)
        self.select_btn.setObjectName("select_btn")
        self.horizontalLayout.addWidget(self.select_btn)
        self.save_btn = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setMinimumSize(QtCore.QSize(80, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/stuff/file_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon2)
        self.save_btn.setIconSize(QtCore.QSize(48, 48))
        self.save_btn.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.save_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.save_btn.setAutoRaise(True)
        self.save_btn.setArrowType(QtCore.Qt.NoArrow)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.open_btn = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_btn.sizePolicy().hasHeightForWidth())
        self.open_btn.setSizePolicy(sizePolicy)
        self.open_btn.setMinimumSize(QtCore.QSize(80, 0))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/stuff/files_view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_btn.setIcon(icon3)
        self.open_btn.setIconSize(QtCore.QSize(48, 48))
        self.open_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.open_btn.setAutoRaise(True)
        self.open_btn.setObjectName("open_btn")
        self.horizontalLayout.addWidget(self.open_btn)
        self.merge_btn = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.merge_btn.sizePolicy().hasHeightForWidth())
        self.merge_btn.setSizePolicy(sizePolicy)
        self.merge_btn.setMinimumSize(QtCore.QSize(80, 0))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/stuff/files_merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.merge_btn.setIcon(icon4)
        self.merge_btn.setIconSize(QtCore.QSize(48, 48))
        self.merge_btn.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.merge_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.merge_btn.setAutoRaise(True)
        self.merge_btn.setObjectName("merge_btn")
        self.horizontalLayout.addWidget(self.merge_btn)
        self.delete_btn = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy)
        self.delete_btn.setMinimumSize(QtCore.QSize(80, 0))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/stuff/files_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon5)
        self.delete_btn.setIconSize(QtCore.QSize(48, 48))
        self.delete_btn.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.delete_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.delete_btn.setAutoRaise(True)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        self.clear_btn = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy)
        self.clear_btn.setMinimumSize(QtCore.QSize(80, 0))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/stuff/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_btn.setIcon(icon6)
        self.clear_btn.setIconSize(QtCore.QSize(48, 48))
        self.clear_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.clear_btn.setAutoRaise(True)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        spacerItem = QtGui.QSpacerItem(86, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.view_frame = QtGui.QGroupBox(self.frame)
        self.view_frame.setObjectName("view_frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.view_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.books_btn = QtGui.QToolButton(self.view_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.books_btn.sizePolicy().hasHeightForWidth())
        self.books_btn.setSizePolicy(sizePolicy)
        self.books_btn.setMinimumSize(QtCore.QSize(80, 0))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/stuff/view_books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.books_btn.setIcon(icon7)
        self.books_btn.setIconSize(QtCore.QSize(48, 48))
        self.books_btn.setCheckable(True)
        self.books_btn.setAutoExclusive(True)
        self.books_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.books_btn.setAutoRaise(True)
        self.books_btn.setObjectName("books_btn")
        self.horizontalLayout_3.addWidget(self.books_btn)
        self.highlights_btn = QtGui.QToolButton(self.view_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.highlights_btn.sizePolicy().hasHeightForWidth())
        self.highlights_btn.setSizePolicy(sizePolicy)
        self.highlights_btn.setMinimumSize(QtCore.QSize(80, 0))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/stuff/view_highlights.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.highlights_btn.setIcon(icon8)
        self.highlights_btn.setIconSize(QtCore.QSize(48, 48))
        self.highlights_btn.setCheckable(True)
        self.highlights_btn.setAutoExclusive(True)
        self.highlights_btn.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.highlights_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.highlights_btn.setAutoRaise(True)
        self.highlights_btn.setObjectName("highlights_btn")
        self.horizontalLayout_3.addWidget(self.highlights_btn)
        self.horizontalLayout.addWidget(self.view_frame)
        self.about_btn = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_btn.sizePolicy().hasHeightForWidth())
        self.about_btn.setSizePolicy(sizePolicy)
        self.about_btn.setMinimumSize(QtCore.QSize(80, 0))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/stuff/logo48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_btn.setIcon(icon9)
        self.about_btn.setIconSize(QtCore.QSize(48, 48))
        self.about_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.about_btn.setAutoRaise(True)
        self.about_btn.setObjectName("about_btn")
        self.horizontalLayout.addWidget(self.about_btn)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(ToolBar)
        QtCore.QMetaObject.connectSlotsByName(ToolBar)

    def retranslateUi(self, ToolBar):
        ToolBar.setWindowTitle(QtGui.QApplication.translate("ToolBar", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.check_btn.setText(QtGui.QApplication.translate("ToolBar", "Testing Button", None, QtGui.QApplication.UnicodeUTF8))
        self.select_btn.setToolTip(QtGui.QApplication.translate("ToolBar", "Scans a directory for Koreader metadata files\n"
"Can also be the eReader\'s root directory (Ctrl+L)", None, QtGui.QApplication.UnicodeUTF8))
        self.select_btn.setStatusTip(QtGui.QApplication.translate("ToolBar", "Scans a directory for Koreader metadata files. Can also be the eReader\'s root directory (Ctrl+L)", None, QtGui.QApplication.UnicodeUTF8))
        self.select_btn.setText(QtGui.QApplication.translate("ToolBar", "Scan Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setToolTip(QtGui.QApplication.translate("ToolBar", "Save selected highlights to text (Ctrl+S)", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setStatusTip(QtGui.QApplication.translate("ToolBar", "Save selected highlights to text (Ctrl+S)", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setText(QtGui.QApplication.translate("ToolBar", "Save selected", None, QtGui.QApplication.UnicodeUTF8))
        self.open_btn.setToolTip(QtGui.QApplication.translate("ToolBar", "View the selected book (Ctrl+B)", None, QtGui.QApplication.UnicodeUTF8))
        self.open_btn.setStatusTip(QtGui.QApplication.translate("ToolBar", "View the selected book (Ctrl+B)", None, QtGui.QApplication.UnicodeUTF8))
        self.open_btn.setText(QtGui.QApplication.translate("ToolBar", "Open Book", None, QtGui.QApplication.UnicodeUTF8))
        self.merge_btn.setToolTip(QtGui.QApplication.translate("ToolBar", "Merge the highlights from the same book in two different\n"
"devices, and/or sync their reading position.\n"
"Active only if two entries of the same book are selected.", None, QtGui.QApplication.UnicodeUTF8))
        self.merge_btn.setStatusTip(QtGui.QApplication.translate("ToolBar", "Merge the highlights from the same book in two different devices, and/or sync their reading position. Active only if two entries of the same book are selected.", None, QtGui.QApplication.UnicodeUTF8))
        self.merge_btn.setText(QtGui.QApplication.translate("ToolBar", "Merge/Sync", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_btn.setToolTip(QtGui.QApplication.translate("ToolBar", "Delete selected highlights (Del)", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_btn.setStatusTip(QtGui.QApplication.translate("ToolBar", "Delete selected highlights (Del)", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_btn.setText(QtGui.QApplication.translate("ToolBar", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_btn.setToolTip(QtGui.QApplication.translate("ToolBar", "Clears the books list (Ctrl+Backspace)", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_btn.setStatusTip(QtGui.QApplication.translate("ToolBar", "Clears the books list (Ctrl+Backspace)", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_btn.setText(QtGui.QApplication.translate("ToolBar", "Clear List", None, QtGui.QApplication.UnicodeUTF8))
        self.books_btn.setToolTip(QtGui.QApplication.translate("ToolBar", "Books View", None, QtGui.QApplication.UnicodeUTF8))
        self.books_btn.setStatusTip(QtGui.QApplication.translate("ToolBar", "Books View", None, QtGui.QApplication.UnicodeUTF8))
        self.books_btn.setText(QtGui.QApplication.translate("ToolBar", "Books", None, QtGui.QApplication.UnicodeUTF8))
        self.highlights_btn.setToolTip(QtGui.QApplication.translate("ToolBar", "Highlights View", None, QtGui.QApplication.UnicodeUTF8))
        self.highlights_btn.setStatusTip(QtGui.QApplication.translate("ToolBar", "Highlights View", None, QtGui.QApplication.UnicodeUTF8))
        self.highlights_btn.setText(QtGui.QApplication.translate("ToolBar", "Highlights", None, QtGui.QApplication.UnicodeUTF8))
        self.about_btn.setToolTip(QtGui.QApplication.translate("ToolBar", "Info about the KoHighlights", None, QtGui.QApplication.UnicodeUTF8))
        self.about_btn.setStatusTip(QtGui.QApplication.translate("ToolBar", "Info about the KoHighlights", None, QtGui.QApplication.UnicodeUTF8))
        self.about_btn.setText(QtGui.QApplication.translate("ToolBar", "About", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
