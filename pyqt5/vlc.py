import sys
import vlc
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class ViedoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(100, 100, 1920, 1080)
        self.setWindowTitle('VLC Player')

        self.videoFrame = QFrame(self)
        self.videoFrame.resize(1920, 1080)
        self.videoFrame.move(0, 0)
        self.videoFrame.setStyleSheet("background-color: black;")

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.player.set_hwnd(self.videoFrame.winId)

        meida = self.instance.media_new('file:///media/nick/data1/Movie/[阳光电影www.ygdy8.com].沃伦.BD.720p.中英双字幕.mkv')
        self.player.set_media(meida)
        self.player.play()

if __name__== '__main__':
    app = QApplication(sys.argv)
    win = ViedoPlayer()
    win.show()
    sys.exit(app.exec_())