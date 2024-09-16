# ejemplo utilizando PyQt5, donde combinamos los widgets QRadioButton (RadioBox), QComboBox (ComboBox), y QSpinBox (SpinBox). 
# El programa permitirá seleccionar el tipo de comida preferida (rápida, saludable, vegetariana) usando un RadioBox, elige una bebida mediante un ComboBox, 
# y selecciona la cantidad de porciones usando un SpinBox. El objetivo del programa es simular un formulario básico de pedido en un restaurante.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QComboBox, QSpinBox, QPushButton, QMessageBox

class VentanaPedido(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Formulario de Pedido")
        self.setGeometry(100, 100, 300, 300)

        # Crear el layout vertical
        layout = QVBoxLayout()

        # Etiqueta de introducción
        self.etiqueta_intro = QLabel("Seleccione su tipo de comida:")
        layout.addWidget(self.etiqueta_intro)

        # Radio Buttons (Tipo de Comida)
        self.radio_rapida = QRadioButton("Comida Rápida")
        self.radio_saludable = QRadioButton("Comida Saludable")
        self.radio_vegetariana = QRadioButton("Comida Vegetariana")

        # Agregar radio buttons al layout
        layout.addWidget(self.radio_rapida)
        layout.addWidget(self.radio_saludable)
        layout.addWidget(self.radio_vegetariana)

        # ComboBox (Bebida)
        self.etiqueta_bebida = QLabel("Seleccione su bebida:")
        layout.addWidget(self.etiqueta_bebida)

        self.combo_bebidas = QComboBox()
        self.combo_bebidas.addItems(["Agua", "Refresco", "Jugo", "Cerveza", "Café"])
        layout.addWidget(self.combo_bebidas)

        # SpinBox (Número de Porciones)
        self.etiqueta_porciones = QLabel("Seleccione la cantidad de porciones:")
        layout.addWidget(self.etiqueta_porciones)

        self.spin_porciones = QSpinBox()
        self.spin_porciones.setRange(1, 10)  # Rango de 1 a 10 porciones
        layout.addWidget(self.spin_porciones)

        # Botón para enviar el pedido
        self.boton_enviar = QPushButton("Enviar Pedido")
        self.boton_enviar.clicked.connect(self.mostrar_pedido)
        layout.addWidget(self.boton_enviar)

        # Etiqueta de salida (resumen del pedido)
        self.etiqueta_salida = QLabel("")
        layout.addWidget(self.etiqueta_salida)

        # Configurar el layout en la ventana
        self.setLayout(layout)

    def mostrar_pedido(self):
        # Obtener el tipo de comida seleccionada
        tipo_comida = ""
        if self.radio_rapida.isChecked():
            tipo_comida = "Comida Rápida"
        elif self.radio_saludable.isChecked():
            tipo_comida = "Comida Saludable"
        elif self.radio_vegetariana.isChecked():
            tipo_comida = "Comida Vegetariana"

        # Obtener la bebida seleccionada
        bebida = self.combo_bebidas.currentText()

        # Obtener la cantidad de porciones seleccionada
        porciones = self.spin_porciones.value()

        if tipo_comida == "":
            # Mostrar un mensaje de error si no se seleccionó un tipo de comida
            QMessageBox.warning(self, "Error", "Debe seleccionar un tipo de comida.")
        else:
            # Crear el mensaje resumen del pedido
            resumen = f"Pedido realizado:\nTipo de comida: {tipo_comida}\nBebida: {bebida}\nPorciones: {porciones}"
            self.etiqueta_salida.setText(resumen)

app = QApplication(sys.argv)
ventana = VentanaPedido()
ventana.show()
sys.exit(app.exec_())
