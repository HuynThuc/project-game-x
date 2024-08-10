import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class TextDisplayApp (QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        # Set the window properties (title and initial size)
        self.setWindowTitle("Text Display Application")
        self.setGeometry (100, 100, 400, 200) # (x, y, width, height)
        
        
        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        
        # Create widgets (QLineEdit, QPushButton, and QLabel)
        self.name_edit = QLineEdit()
        self.sdt_edit = QLineEdit()
        self.display_button = QPushButton("Click here to display Text")
        self.remove_button = QPushButton("Xóa")
        self.name_label = QLabel("")
        self.sdt_label = QLabel("")
        
        # Create a vertical layout
        layout = QVBoxLayout()
        
        # Add widgets to the layout
        layout.addWidget(self.name_edit)
        layout.addWidget(self.sdt_edit)
        layout.addWidget(self.display_button)
        layout.addWidget(self.remove_button)
        
        layout.addWidget(self.name_label)
        layout.addWidget(self.sdt_label)
        
        central_widget.setLayout(layout)
        
        self.display_button.clicked.connect(self.display_text)
        
        # Set the layout for the central widget central_widget.setLayout(layout)
        # Connect the button click event to the display_text function self.display_button.clicked.connect(self.display_text)
    def display_text(self):
            #Get the text from the QLineEdit and display it in the QLabel entered_text = self.text_edit.text() self.result_label.setText(f"Input Text: {entered_text}")
            name_text = self.name_edit.text() 
            sdt_text = self.sdt_edit.text() 
            
            self.name_label.setText(f"Tên: {name_text}")
            self.sdt_label.setText(f"Số điện thoại: {sdt_text}")
def main():
                # Create a PyQt application
        app = QApplication(sys.argv)
                
                
        window = TextDisplayApp()
        
        window.show()
        
        sys.exit(app.exec_())
        
if __name__ == "__main__":
    main()
        
        
