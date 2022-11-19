import sys

import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QApplication, QDialog, \
    QWidget, QLineEdit, QLabel, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Prototype"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        # self.setWindowIcon(QtGui.QIcon(self.iconName))
        #self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(vbox)
        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox("Merge two csv files together.")
        gridLayout = QGridLayout()

        wordsFileLabel = QLabel(self)
        wordsFileLabel.setText("Words File")
        gridLayout.addWidget(wordsFileLabel, 0, 0)

        self.wordsFileLine = QLineEdit(self)
        self.wordsFileLine.setMinimumHeight(40)
        self.wordsFileLine.setPlaceholderText("None selected.")
        gridLayout.addWidget(self.wordsFileLine, 0, 1)

        wordsFileButton = QPushButton("Select", self)
        wordsFileButton.setMinimumHeight(40)
        wordsFileButton.clicked.connect(lambda: self.openFileNameDialog(self.wordsFileLine))
        gridLayout.addWidget(wordsFileButton, 0, 2)

        # Sentences
        sentencesFileLabel = QLabel(self)
        sentencesFileLabel.setText("Sentences File")
        gridLayout.addWidget(sentencesFileLabel, 1, 0)

        self.sentencesFileLine = QLineEdit(self)
        self.sentencesFileLine.setMinimumHeight(40)
        self.sentencesFileLine.setPlaceholderText("None selected.")
        gridLayout.addWidget(self.sentencesFileLine, 1, 1)

        sentencesFileButton = QPushButton("Select", self)
        sentencesFileButton.setMinimumHeight(40)
        sentencesFileButton.clicked.connect(lambda: self.openFileNameDialog(self.sentencesFileLine))
        gridLayout.addWidget(sentencesFileButton, 1, 2)

        # Output file.
        outputFileLabel = QLabel(self)
        outputFileLabel.setText("Output File")
        gridLayout.addWidget(outputFileLabel, 2, 0)

        self.outputFileLine = QLineEdit(self)
        self.outputFileLine.setMinimumHeight(40)
        self.outputFileLine.setPlaceholderText("None selected.")
        gridLayout.addWidget(self.outputFileLine, 2, 1)

        outputFileButton = QPushButton("Select", self)
        outputFileButton.setMinimumHeight(40)
        outputFileButton.clicked.connect(lambda: self.saveFileDialog(self.outputFileLine))
        gridLayout.addWidget(outputFileButton, 2, 2)

        self.statusText = QLabel(self)
        gridLayout.addWidget(self.statusText, 3, 1)

        confirmFileButton = QPushButton("Join", self)
        confirmFileButton.setMinimumHeight(40)
        confirmFileButton.clicked.connect(self.confirmButtonClicked)
        gridLayout.addWidget(confirmFileButton, 3, 2)

        self.groupBox.setLayout(gridLayout)

    def openFileNameDialog(self, outTextWidget):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "CSV File (*.csv);;All Files (*)", options=options)
        outTextWidget.setText(fileName)

    def saveFileDialog(self, outTextWidget):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "CSV File (*.csv);;All Files (*)", options=options)
        outTextWidget.setText(fileName)

    def confirmButtonClicked(self):
        errors = []

        wordsFilePath = self.wordsFileLine.text()
        sentencesFilePath = self.sentencesFileLine.text()
        outputFilePath = self.outputFileLine.text()
        if not wordsFilePath:
            errors.append("Words file is empty.")

        if not sentencesFilePath:
            errors.append("Sentences file is empty.")

        if not outputFilePath:
            errors.append("Output file is empty.")

        if errors:
            self.statusText.setText("<font color = red>" + '\n'.join(errors) + "</font>")
            return

        try:
            words = pd.read_csv(wordsFilePath)
            sentences = pd.read_csv(sentencesFilePath)
            out = words.join(sentences.set_index("ID"), on="SentenceID", validate="m:1")
            out.to_csv(outputFilePath)
            self.statusText.setText("Successfully joined files.")
        except:
            self.statusText.setText("<font color = red>Error when saving file.</font>")

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec())