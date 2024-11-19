import json
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton


class StatisticsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Статистика")
        self.stats_label = QLabel()
        self.setMinimumSize(200, 100)
        layout = QVBoxLayout()
        layout.addWidget(self.stats_label)

        clear_button = QPushButton("Очистить статистику")
        clear_button.clicked.connect(self.clear_statistics)
        layout.addWidget(clear_button)

        self.setLayout(layout)
        self.stats_file = "statistics.json"
        self.load_statistics()

    def load_statistics(self):
        try:
            with open(self.stats_file, "r") as file:
                stats = json.load(file)
            formatted_stats = self.format_statistics(stats)
            self.stats_label.setText(formatted_stats)
        except FileNotFoundError:
            self.stats_label.setText("Статистика отсутствует.")

    def clear_statistics(self):
        with open(self.stats_file, "w") as file:
            json.dump({}, file)
        self.load_statistics()

    def format_statistics(self, stats):
        if not stats:
            return "Статистика отсутствует."
        result = "Статистика побед:\n"
        for player, wins in stats.items():
            result += f"{player}: {wins} побед\n"
        return result

    @staticmethod
    def add_to_statistics(winner):
        stats_file = "statistics.json"
        try:
            with open(stats_file, "r") as file:
                stats = json.load(file)
        except FileNotFoundError:
            stats = {}

        stats[winner] = stats.get(winner, 0) + 1

        with open(stats_file, "w") as file:
            json.dump(stats, file)
