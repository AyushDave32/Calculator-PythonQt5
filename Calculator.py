import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 300)

        layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.result_display.setAlignment(Qt.AlignRight)  # Align the text to the right
        layout.addWidget(self.result_display)

        button_grid = [
            ["1", "2", "3", "*"],
            ["4", "5", "6", "-"],
            ["7", "8", "9", "+"],
            ["0", "C", "=", "/"],
        ]

        for row in button_grid:
            button_row = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.on_button_click)
                button.setStyleSheet(
                    """
                    QPushButton {
                        background-color: purple;
                        border: none;
                        color: white;
                        padding: 15px 32px;
                        text-align: center;
                        font-size: 16px;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin: 4px 2px;
                        cursor: pointer;
                        border-radius: 4px;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                    }
                    QPushButton:pressed {
                        background-color: #45a049;
                        border-style: inset;
                    }
                    """
                )
                button_row.addWidget(button)
            layout.addLayout(button_row)

        self.setLayout(layout)

        self.current_text = ""

    def on_button_click(self):
        button = self.sender()
        button_text = button.text()

        if button_text == "=":
            try:
                result = eval(self.current_text)
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")
        elif button_text == "C":
            self.current_text = ""
            self.result_display.clear()
        else:
            self.current_text += button_text
            self.result_display.setText(self.current_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())

