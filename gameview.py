from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsTextItem, QMessageBox, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QFont
from game_model import GameModel
from statisticsview import StatisticsDialog


class GameView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.model = GameModel()
        self.cell_size = 30

        # Шрифт для отображения X и O
        self.font = QFont("Arial", 16)
        self.font.setBold(True)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setMinimumSize(600, 600)  # Минимальный размер окна
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def set_board_size(self, size):
        self.model.set_board_size(size)
        self.update_view()

    def update_view(self):
        """
        Перерисовка игрового поля и отображение текущего состояния клеток с учетом нового размера.
        """
        self.scene.clear()
        size = self.model.board_size

        # Рисуем сетку и символы
        for x in range(size):
            for y in range(size):
                # Рисуем клетку
                rect = self.scene.addRect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                    QPen(Qt.black),
                )

                # Если клетка занята, рисуем соответствующий символ
                if self.model.board[y][x] != "":
                    text_item = QGraphicsTextItem(self.model.board[y][x])
                    text_item.setFont(self.font)
                    text_item.setDefaultTextColor(Qt.blue)

                    # Вычисляем центр клетки
                    cell_center_x = x * self.cell_size + self.cell_size / 2
                    cell_center_y = y * self.cell_size + self.cell_size / 2

                    # Вычисляем размеры текста для центрирования
                    text_rect = text_item.boundingRect()
                    text_item.setPos(
                        cell_center_x - text_rect.width() / 2,
                        cell_center_y - text_rect.height() / 2,
                    )
                    self.scene.addItem(text_item)

    def mousePressEvent(self, event):
        """
        Обрабатывает нажатие мыши и делает ход, если клик приходится на игровое поле.
        """
        if event.button() == Qt.LeftButton:
            pos = event.pos()
            x = int(pos.x() / self.cell_size)
            y = int(pos.y() / self.cell_size)

            if self.model.make_move(x, y):
                self.update_view()
                if self.model.check_winner():
                    winner = "O" if self.model.current_player == "X" else "X"
                    QMessageBox.information(self, "Победа!", f"Победил {winner}!")
                    StatisticsDialog.add_to_statistics(winner)
                    self.model.reset_board()
                    self.update_view()

    def resizeEvent(self, event):
        """
        Обеспечивает изменение размеров окна только в квадратной форме.
        """
        # Заставляем окно быть квадратным
        new_size = min(self.width(), self.height())
        self.resize(new_size, new_size)  # Применяем квадратные размеры

        # Пересчитываем размеры клеток
        view_width = self.viewport().width()
        view_height = self.viewport().height()
        size = self.model.board_size
        self.cell_size = min(view_width / size, view_height / size)

        # Перерисовываем поле
        self.update_view()

        # Важно вызвать родительский метод для обработки событий
        super().resizeEvent(event)

    def showEvent(self, event):
        """
        Обрабатывает событие показа окна (окно становится активным).
        Здесь мы пересчитываем размер клеток и обновляем поле.
        """
        # Пересчитываем размеры клеток
        view_width = self.viewport().width()
        view_height = self.viewport().height()
        size = self.model.board_size
        self.cell_size = min(view_width / size, view_height / size)

        # Перерисовываем поле
        self.update_view()

        super().showEvent(event)