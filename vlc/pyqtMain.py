import sys
import vlc
from PyQt5.QtWidgets import QApplication, QMainWindow
import template.vwyl as vwyl

class VWYLMainWidget(QMainWindow, vwyl.Ui_MainWindow):
    def __init__(self):
        super(VWYLMainWidget, self).__init__()
        self.setupUi(self)

        instance = vlc.Instance()
        media_player = instance.media_player_new()
        media_player.set_hwnd(self.video_frame.winId())
        media = instance.media_new("rtsp://192.168.0.51:8554/stream")
        media_player.set_media(media)
        media_player.play()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_widget = VWYLMainWidget()
    main_widget.show()
    sys.exit(app.exec_())
