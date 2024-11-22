import sys
import vlc
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QPushButton, QVBoxLayout

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle('Video Player')

        v_layout1 = QVBoxLayout()
        videoFrame = QFrame()
        videoFrame.setGeometry(0, 0, 800, 600)
        # videoFrame.resize(800, 600)
        # videoFrame.move(0, 0)
        instance = vlc.Instance()
        media_player = instance.media_player_new()
        media_player.set_hwnd(videoFrame.winId())
        media = instance.media_new("rtsp://192.168.0.51:8554/stream")
        # media = instance.media_new("rtsp://admin:Sygy%402024@192.168.0.64:554")
        media_player.set_media(media)
        media_player.play()
        v_layout1.addWidget(videoFrame)

        v_layout2 = QVBoxLayout()
        dataFrame = QFrame()
        dataFrame.resize(200, 400)
        # dataFrame.move(800, 0)
        dataFrame.setStyleSheet("background-color: white;")
        self.btn = QPushButton("Start")
        self.btn.clicked.connect(self.change_text)
        self.btn.setStyleSheet("background-color: gray;")
        v_layout2.addWidget(dataFrame)
        v_layout2.addWidget(self.btn)

        hlayout = QHBoxLayout()
        hlayout.addLayout(v_layout1)
        hlayout.addLayout(v_layout2)
        self.setLayout(hlayout)
        
    def change_text(self):
        if self.btn.text() == "Start":
            self.btn.setText("Stop")
        else:
            self.btn.setText("Start")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())

