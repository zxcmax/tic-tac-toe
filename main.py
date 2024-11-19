import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QDialog
from gameview import GameView
from settings import SettingsDialog
from statisticsview import StatisticsDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("5 в ряд")

        self.game_view = GameView()
        self.settings_dialog = SettingsDialog()
        self.statistics_dialog = StatisticsDialog()

        # Главное меню
        main_layout = QVBoxLayout()
        play_button = QPushButton("Играть")
        settings_button = QPushButton("Настройки")
        stats_button = QPushButton("Статистика")

        play_button.clicked.connect(self.start_game)
        settings_button.clicked.connect(self.open_settings)
        stats_button.clicked.connect(self.show_statistics)

        main_layout.addWidget(play_button)
        main_layout.addWidget(settings_button)
        main_layout.addWidget(stats_button)

        central_widget = QDialog()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def start_game(self):
        size = self.settings_dialog.get_board_size()
        self.game_view.set_board_size(size)
        self.game_view.show()


    def open_settings(self):
        self.settings_dialog.exec_()

    def show_statistics(self):
        self.statistics_dialog.load_statistics()
        self.statistics_dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Применяем стиль ко всему приложению
    app.setStyleSheet("""
            * { background-color: rgba(176, 196, 222, 255); }
            QPushButton { 
                background-color: rgba(255, 153, 102, 200); 
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 14px;
                width: 3em;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: rgba(255, 102, 0, 200);
            }
            QPushButton:pressed {
                background-color: rgba(255, 0, 0, 200);
            }
            QPushButton:disabled {
                background-color: rgba(204, 153, 102, 200);
            }
            QTextEdit {
                background-color: rgba(102, 204, 102, 200);
                border-style: outset;
                border-width: 0px;
                border-radius: 10px;
                border-color: black;
                width: 3em;
                padding: 6px;
            }
            QLabel {
                font: 12px;
                color: black;
            }
            QComboBox {
                background-color: rgba(255, 255, 255, 255);
                border-style: solid;
                border-width: 2px;
                border-radius: 8px;
                border-color: rgba(102, 102, 102, 255);
                padding: 6px;
                font: bold 12px;
                color: black;
            }
            
            QComboBox::drop-down {
                border-left: 1px solid rgba(102, 102, 102, 255);
                width: 20px;
                background-color: transparent;
            }
            
            QComboBox QAbstractItemView {
                border: 1px solid rgba(102, 102, 102, 255);
                background-color: rgba(240, 240, 240, 255);
                selection-background-color: rgba(255, 153, 102, 200);
                selection-color: black;
            }
            
            QComboBox:hover {
                border-color: rgba(255, 102, 0, 200);
            }
        """)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
