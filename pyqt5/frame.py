import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout

class ViedoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        print('type of self:', self.width(), self.height())
        self.initUI()
    def initUI(self):
        self.setGeometry(100, 100, 2320, 1080)
        self.setWindowTitle('VLC Player')

        videoFrame = QFrame(self)
        videoFrame.resize(1920, 1080)
        videoFrame.move(0, 0)
        videoFrame.setStyleSheet("background-color: green;")

        dataFrame = QFrame(self)
        dataFrame.resize(400, 1080)
        dataFrame.move(1920, 0)
        dataFrame.setStyleSheet("background-color: black;")

    def resizeEvent(self, event):
        super().resizeEvent(event)

        new_size = event.size()
        print("size of windows: ", new_size.width(), new_size.height())

if __name__== '__main__':
    app = QApplication(sys.argv)
    win = ViedoPlayer()
    win.show()
    sys.exit(app.exec_())