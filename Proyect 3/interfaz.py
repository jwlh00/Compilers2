# importing required libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from YAPL_Printer import YAPLPrinter
from TranslateToTAC import *
from TranslatetoMIPS import *

import os
import sys



class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.codeEditor = editor

    def sizeHint(self):
        return QSize(self.codeEditor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event)

class NumberedPlainTextEdit(QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        super(NumberedPlainTextEdit, self).__init__(*args, **kwargs)
        self.lineNumberArea = LineNumberArea(self)

        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        self.updateLineNumberAreaWidth(0)

    def lineNumberAreaWidth(self):
        digits = 1
        max_num = max(1, self.blockCount())
        while max_num >= 10:
            max_num /= 10
            digits += 1
        space = 3 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super(NumberedPlainTextEdit, self).resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), Qt.lightGray)

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(Qt.black)
                painter.drawText(0, int(top), self.lineNumberArea.width(), self.fontMetrics().height(), Qt.AlignRight, number)


            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            block_number += 1

    def highlightCurrentLine(self):
        extra_selection = QTextEdit.ExtraSelection()
        line_color = QColor(Qt.yellow).lighter(160)
        extra_selection.format.setBackground(line_color)
        extra_selection.format.setProperty(QTextFormat.FullWidthSelection, True)
        extra_selection.cursor = self.textCursor()
        extra_selection.cursor.clearSelection()
        self.setExtraSelections([extra_selection])
# Creating main window class
class MainWindow(QMainWindow):

	# constructor
	def __init__(self, *args, **kwargs):
		self.content_editor = ''
		super(MainWindow, self).__init__(*args, **kwargs)
		# self.setGeometry(1200, 800)

		# setting window geometry
		self.setGeometry(100, 100, 1200, 800)
		# self.setAcceptDrops(True)
		# setting font to the editor
		fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
		fixedfont.setPointSize(10)

		# creating a layout
		mainlayout = QVBoxLayout()

		# Initialize tab screen
		self.tabs = QTabWidget()
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QWidget()

		# # Add tabs
		self.tabs.addTab(self.tab1, "Text Editor")
		self.tabs.addTab(self.tab2, "Results")
		self.tabs.addTab(self.tab3, "MIPS")

		# creating a QPlainTextEdit object
		self.editor = NumberedPlainTextEdit()

		self.showErrors = QLabel()
		self.showErrors.setFont(fixedfont)
		self.showErrors.setText("")
		self.tab2.layout = QVBoxLayout()
		self.tab2.layout.addWidget(self.showErrors)
		self.tab2.setLayout(self.tab2.layout)

		self.showMIPS = QLabel()
		self.showMIPS.setFont(fixedfont)
		self.showMIPS.setText("")
		self.tab3.layout = QVBoxLayout()
		self.tab3.layout.addWidget(self.showMIPS)
		self.tab3.setLayout(self.tab3.layout)

		self.editor.setFont(fixedfont)

		# self.path holds the path of the currently open file.
		# If none, we haven't got a file open yet (or creating new).
		self.path = None

		# adding editor to the layout
		mainlayout.addWidget(self.tabs)
		# layout.addWidget(self.editor)
		self.tab1.layout = QVBoxLayout()
		self.tab1.layout.addWidget(self.editor)
		self.tab1.setLayout(self.tab1.layout)

		# creating a QWidget layout
		container = QWidget()

		# setting layout to the container
		container.setLayout(mainlayout)

		# making container as central widget
		self.setCentralWidget(container)

		# creating a status bar object
		self.status = QStatusBar()

		# setting stats bar to the window
		self.setStatusBar(self.status)

		# creating a file tool bar
		file_toolbar = QToolBar("File")

		# adding file tool bar to the window
		self.addToolBar(file_toolbar)

		# creating actions to add in the file menu
		# creating a open file action
		open_file_action = QAction("Open file", self)

		# setting status tip
		open_file_action.setStatusTip("Open file")

		# adding action to the open file
		open_file_action.triggered.connect(self.file_open)

		# adding this to tool bar
		file_toolbar.addAction(open_file_action)

		# similarly creating a save action
		save_file_action = QAction("Save", self)
		save_file_action.setStatusTip("Save current page")
		save_file_action.triggered.connect(self.file_save)
		file_toolbar.addAction(save_file_action)

		# similarly creating save action
		saveas_file_action = QAction("Save As", self)
		saveas_file_action.setStatusTip("Save current page to specified file")
		saveas_file_action.triggered.connect(self.file_saveas)
		file_toolbar.addAction(saveas_file_action)

		compile_action = QAction("Compile", self)
		compile_action.setStatusTip("Compile current program")
		compile_action.triggered.connect(self.compile)
		file_toolbar.addAction(compile_action)

		# creating another tool bar for editing text
		edit_toolbar = QToolBar("Edit")

		# adding this tool bar to the main window
		self.addToolBar(edit_toolbar)

		# adding actions to the tool bar and menu bar

		# undo action
		undo_action = QAction("Undo", self)
		# adding status tip
		undo_action.setStatusTip("Undo last change")

		# when triggered undo the editor
		undo_action.triggered.connect(self.editor.undo)

		# adding this to tool and menu bar
		edit_toolbar.addAction(undo_action)

		# redo action
		redo_action = QAction("Redo", self)
		redo_action.setStatusTip("Redo last change")

		# when triggered redo the editor
		redo_action.triggered.connect(self.editor.redo)

		# adding this to menu and tool bar
		edit_toolbar.addAction(redo_action)

		# cut action
		cut_action = QAction("Cut", self)
		cut_action.setStatusTip("Cut selected text")

		# when triggered cut the editor text
		cut_action.triggered.connect(self.editor.cut)

		# adding this to menu and tool bar
		edit_toolbar.addAction(cut_action)

		# copy action
		copy_action = QAction("Copy", self)
		copy_action.setStatusTip("Copy selected text")

		# when triggered copy the editor text
		copy_action.triggered.connect(self.editor.copy)

		# adding this to menu and tool bar
		edit_toolbar.addAction(copy_action)

		# paste action
		paste_action = QAction("Paste", self)
		paste_action.setStatusTip("Paste from clipboard")

		# when triggered paste the copied text
		paste_action.triggered.connect(self.editor.paste)

		# adding this to menu and tool bar
		edit_toolbar.addAction(paste_action)

		# select all action
		select_action = QAction("Select all", self)
		select_action.setStatusTip("Select all text")

		# when this triggered select the whole text
		select_action.triggered.connect(self.editor.selectAll)

		# adding this to menu and tool bar
		edit_toolbar.addAction(select_action)


		# wrap action
		wrap_action = QAction("Wrap text to window", self)
		wrap_action.setStatusTip("Check to wrap text to window")

		# making it checkable
		wrap_action.setCheckable(True)

		# making it checked
		wrap_action.setChecked(True)

		# adding action
		wrap_action.triggered.connect(self.edit_toggle_wrap)

		# calling update title methpd
		self.update_title()

		# showing all the components
		self.show()

	# creating dialog critical method
	# to show errors
	def dialog_critical(self, s):

		# creating a QMessageBox object
		dlg = QMessageBox(self)

		# setting text to the dlg
		dlg.setText(s)

		# setting icon to it
		dlg.setIcon(QMessageBox.Critical)

		# showing it
		dlg.show()

	# action called by file open action
	def file_open(self):

		# getting path and bool value
		path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
							"YAPL (*.YAPL)")

		# if path is true
		if path:
			# try opening path
			try:
				with open(path, 'r') as f:
					# read the file
					text = f.read()

			# if some error occured
			except Exception as e:

				# show error using critical method
				self.dialog_critical(str(e))
			# else
			else:
				# update path value
				self.path = path

				# update the text
				self.editor.setPlainText(text)

				# update the title
				self.update_title()

	# action called by file save action
	def file_save(self):

		# if there is no save path
		if self.path is None:

			# call save as method
			return self.file_saveas()

		# else call save to path method
		self._save_to_path(self.path)

	# action called by save as action
	def file_saveas(self):

		# opening path
		path, _ = QFileDialog.getSaveFileName(self, "Save file", "",
							"Text documents (*.txt);All files (*.*)")

		# if dialog is cancelled i.e no path is selected
		if not path:
			# return this method
			# i.e no action performed
			return

		# else call save to path method
		self._save_to_path(path)

	def compile(self):
		print('COMPILANDO...')
		if self.path is None:
			return self.file_saveas()
		self._save_to_path(self.path)
		
		input = self.path

		if self.editor.toPlainText() != '':
			compilado = YAPLPrinter(input)

			tree = compilado.treeStruct

			intermedio = TranslateToTACFunc(tree, compilado.symbolTable)

			print("=======================================================================")

			print(intermedio.__str__())
			print("---------------TAC Code---------------")
			print(intermedio.translate())
			self.showErrors.setText(intermedio.translate())
			print("=======================================================================")


			print("---------------MIPS Code---------------")
			ensamblador = TranslatetoMIPSFunc(intermedio.quadruplesList)
			print(str(ensamblador.data_section + ensamblador.text_section))
			self.showMIPS.setText(str(ensamblador.data_section + ensamblador.text_section))

			self.tabs.setCurrentIndex(2)

			
	# save to path method
	def _save_to_path(self, path):

		# get the text
		text = self.editor.toPlainText()

		# try catch block
		try:

			# opening file to write
			with open(path, 'w') as f:

				# write text in the file
				f.write(text)

		# if error occurs
		except Exception as e:

			# show error using critical
			self.dialog_critical(str(e))

		# else do this
		else:
			# change path
			self.path = path
			# update the title
			self.update_title()

	# update title method
	def update_title(self):
		self.setWindowTitle("%s" %(os.path.basename(self.path)
												if self.path else "Untitled"))

	def edit_toggle_wrap(self):
		self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0 )



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("PyQt5-Note")
    window = MainWindow()
    app.exec_()