from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QComboBox


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Настройки")

        # Выпадающий список для выбора размера
        self.size_selector = QComboBox(self)
        self.size_selector.addItems(["10", "20"])  # Доступные размеры поля

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Размер поля (10 или 20):"))
        layout.addWidget(self.size_selector)

        save_button = QPushButton("Сохранить")
        save_button.clicked.connect(self.accept)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def get_board_size(self):
        # Возвращаем выбранный размер как число
        return int(self.size_selector.currentText())