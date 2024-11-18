import sys
import vlc
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame
from PyQt5.QtCore import Qt

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Video Player')

        self.videoFrame = QFrame(self)
        self.videoFrame.setGeometry(10, 10, 800, 600)
        self.videoFrame.resize(800, 600)
        self.videoFrame.move(0, 0)
        self.videoFrame.setStyleSheet("background-color: black;")

        self.instance = vlc.Instance()
        self.media_player = self.instance.media_player_new()
        self.media_player.set_hwnd(self.videoFrame.winId())

        # media = self.instance.media_new("rtsp://192.168.0.125:8554/stream")
        media = self.instance.media_new("rtsp://admin:Sygy%402024@192.168.0.64:554")
        self.media_player.set_media(media)
        self.media_player.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())

