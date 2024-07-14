import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox, QWidget
from HandTracking import start


class MainApp(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Security Agreement")
        self.setGeometry(150, 150, 400, 200)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.label = QLabel("Please read and accept the following security agreement:")
        self.layout.addWidget(self.label)

        self.contractText = QLabel(
"By using this software, you can navigate and perform various operations on the X platform using hand gestures."
"However, any responsibility for errors or unintended actions that occur during the use of the software lies entirely with the user."
"The user must carefully read all instructions before using the software and exercise necessary caution during use."
"The software developers cannot be held liable for any data loss, account access issues, or other adverse circumstances that may arise from using the software."
                                   )
        self.contractText.setWordWrap(True)
        self.layout.addWidget(self.contractText)

        self.checkbox = QCheckBox("I accept the security agreement.")
        self.layout.addWidget(self.checkbox)

        self.acceptButton = QPushButton("Accept It and Move On")
        self.acceptButton.setEnabled(False)
        self.layout.addWidget(self.acceptButton)

        self.checkbox.stateChanged.connect(self.toggleAcceptButton)

        self.acceptButton.clicked.connect(self.startProgram)

    def toggleAcceptButton(self):
        if self.checkbox.isChecked():
            self.acceptButton.setEnabled(True)
        else:
            self.acceptButton.setEnabled(False)

    def startProgram(self):
        if self.checkbox.isChecked():
            QMessageBox.information(self, "Approved", "Starting the program...")
            start()
        else:
            QMessageBox.warning(self, "Warning", "You must accept the security agreement.")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()