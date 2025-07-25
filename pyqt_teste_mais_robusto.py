import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QMainWindow, QLabel, QVBoxLayout, QWidget,
    QLineEdit, QPushButton
)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QPalette, QColor


class HelloWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(400, 200))
        self.setWindowTitle("Janela Personalizada - PyQt5")

        # Cores de fundo
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#f0f8ff"))  # azul bem claro
        self.setPalette(palette)

        # Widget central
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # ✅ CORREÇÃO: Criar o layout com o centralWidget como pai
        layout = QVBoxLayout(centralWidget)
        centralWidget.setLayout(layout)

        # Título
        title = QLabel("Bem-vindo ao PyQt5!")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)

        # Campo de entrada
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Digite seu nome...")
        layout.addWidget(self.input_name)

        # Label de resposta
        self.result_label = QLabel("")
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.result_label)

        # Botão "Saudar"
        btn_saudacao = QPushButton("Saudar")
        btn_saudacao.clicked.connect(self.saudacao)
        layout.addWidget(btn_saudacao)

        # Botão "Sair"
        btn_sair = QPushButton("Sair")
        btn_sair.clicked.connect(self.close)
        layout.addWidget(btn_sair)

    def saudacao(self):
        nome = self.input_name.text().strip()
        if nome:
            self.result_label.setText(f"Olá, {nome}! Seja bem-vindo 😄")
        else:
            self.result_label.setText("Por favor, digite seu nome.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())
