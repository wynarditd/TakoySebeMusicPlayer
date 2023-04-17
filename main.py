from PyQt6 import  QtWidgets
import ui
import os
import time
import multiprocessing


import sound


class MainWindow(QtWidgets.QMainWindow, untitled_ui.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("TakoySebeMusicPlayer")

        self.player = sound.MusicPlayer()

        self.play_button.clicked.connect(self.play)
        self.pause_button.clicked.connect(self.player.pause)
        self.stop_button.clicked.connect(self.player.stop)
        self.next_button.clicked.connect(self.next)
        self.last_button.clicked.connect(self.last)
        self.load_button.clicked.connect(self.load)

        self.slider.valueChanged.connect(self.slider_value)

        self.song_table.itemDoubleClicked.connect(self.play)

        self.count_of_songs = 0
        self.dir = ""
        

    def play(self):
        item = self.song_table.currentItem()

        if item:
            file_name = os.path.join(self.dir,item.text())
            self.player.play(file_name)
            self.slider.setValue(0)
        else:
            self.song_table.setCurrentRow(0)
            self.label.setText(f"No song")
        
        self.set_song()



    def next(self):
        self.song_table.setCurrentRow(self.song_table.currentRow()+1)
        if self.song_table.currentRow() == -1:
            self.song_table.setCurrentRow(0)
        self.play()
        


    def last(self):
        self.song_table.setCurrentRow(self.song_table.currentRow()-1)
        if self.song_table.currentRow() == -1:
            self.song_table.setCurrentRow(self.count_of_songs - 1)
        self.play()




    def load(self):
        self.song_table.clear()

        dir = QtWidgets.QFileDialog.getExistingDirectory(self,"Select Directory")
        self.setWindowTitle("TakoySebeMusicPlayer | "+dir)
        count = 0
        if dir:
            for i in os.listdir(dir):
                if i.endswith(".mp3") or i.endswith(".wav") or i.endswith(".ogg"):
                    count += 1
                    self.song_table.addItem(os.path.join(i))
            self.count_of_songs = count
            self.dir = dir
            self.song_table.setCurrentRow(0)

    def set_song(self):
        self.song_name.setText(self.song_table.currentItem().text())
        len = self.player.sound_length()
        self.slider.setMaximum(len)
        self.label.setText(f"{time.strftime('%H:%M:%S', time.gmtime(len))}")



    def slider_value(self,value):
        self.player.startWith(value)





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
