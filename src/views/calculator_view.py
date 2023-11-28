from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from viewmodels.calculator_viewmodel import CalculatorViewModel

class CalculatorView(QWidget):
    """A simple calculator application using PyQt5."""
    def __init__(self):
        """Initialize the calculator view with a ViewModel and UI setup."""
        super().__init__()
        self.init_ui()
        self.viewmodel = CalculatorViewModel()
        self.a = ''  # Will hold the first operand
        self.b = ''  # Will hold the second operand
        self.operation = ''  # Will hold the operation
        self.user_is_typing_second_number = False  # Initialize the attribute here

    def init_ui(self):
        """Set up the user interface components and layout for the calculator."""
        self.setWindowTitle('Calculator')
        self.create_grid_layout()
        self.show()

    def create_grid_layout(self):
        """Create a grid layout with buttons and a display widget."""
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.display = QLineEdit('0')
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        grid_layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 3),
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_click)
            grid_layout.addWidget(button, row, col)
            button.setFixedSize(75, 75)

        self.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                background-color: #e0e0e0;
                border: 2px solid navy; 
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
            QLineEdit {
                font-size: 24px;
                padding: 10px;
                border: 2px solid navy; 
            }
        """)

    def on_click(self):
        """Handle button click events to perform calculator operations."""
        button = self.sender()
        button = self.sender()
        if button:
            text = button.text()
            current_display = self.display.text()

            if text.isdigit() or (text == '.' and '.' not in current_display):
                if self.display.text() == '0' or self.user_is_typing_second_number:
                    self.display.setText(text)
                else:
                    self.display.setText(current_display + text)
            elif text in ('+', '-', '*', '/'):
                if not self.user_is_typing_second_number:
                    self.a = self.display.text()  # Hydrate a with the current display
                    self.operation = text  # Set the operation
                    self.user_is_typing_second_number = True  # Now ready to take b
                    self.display.setText('0')  # Reset the display for b's input
            elif text == '=' and self.user_is_typing_second_number:
                self.b = self.display.text()  # Hydrate b with the current display
                result = self.viewmodel.perform_calculation(self.a, self.b, self.operation)
                self.display.setText(result)
                self.a = ''  # Reset a after calculation
                self.b = ''  # Reset b after calculation
                self.operation = ''  # Clear the operation
                self.user_is_typing_second_number = False
            elif text == 'C':
                self.display.setText('0')
                self.a = ''
                self.b = ''
                self.operation = ''
                self.user_is_typing_second_number = False

# Run the application
if __name__ == '__main__':
    app = QApplication([])
    ex = CalculatorView()
    sys.exit(app.exec_())
