import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class ChessStats(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chess Stats')

        # Create username label and text input
        username_label = QLabel('Enter Chess.com username:')
        self.username_input = QLineEdit(self)

        # Create submit button
        submit_btn = QPushButton('Submit', self)
        submit_btn.clicked.connect(self.get_stats)

        # Create labels to display stats
        self.rapid_label = QLabel()
        self.blitz_label = QLabel()
        self.classical_label = QLabel()

        # Create layout and add widgets
        vbox = QVBoxLayout()
        vbox.addWidget(username_label)
        vbox.addWidget(self.username_input)
        vbox.addWidget(submit_btn)
        vbox.addWidget(self.rapid_label)
        vbox.addWidget(self.blitz_label)
        vbox.addWidget(self.classical_label)

        self.setLayout(vbox)

    def get_stats(self):
        username = self.username_input.text()

        # Make API request for user's stats
        stats_url = f'https://api.chess.com/pub/player/{username}/stats'
        response = requests.get(stats_url)

        # Check for errors
        if response.status_code != 200:
            self.rapid_label.setText('Error: Could not retrieve stats')
            self.blitz_label.setText('')
            self.classical_label.setText('')
            return

        # Get user's rating in rapid, blitz, and classical
        stats = response.json()
        try:
            rapid_rating = stats['chess_rapid']['last']['rating']
        except KeyError:
            rapid_rating = 'N/A'

        try:
            blitz_rating = stats['chess_blitz']['last']['rating']
        except KeyError:
            blitz_rating = 'N/A'

        try:
            classical_rating = stats['chess_bullet']['last']['rating']
        except KeyError:
            classical_rating = 'N/A'

        # Display ratings
        self.rapid_label.setText(f'Rapid rating: {rapid_rating}')
        self.blitz_label.setText(f'Blitz rating: {blitz_rating}')
        self.classical_label.setText(f'Classical rating: {classical_rating}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chess_stats = ChessStats()
    chess_stats.show()
    sys.exit(app.exec_())
