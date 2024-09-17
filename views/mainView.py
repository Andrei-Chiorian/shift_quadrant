from tkinter import *
from pandastable import Table, config


class MainView:

    def __init__(self, master=None, df=None):
        self.frame = Frame(master)

        self.frame.pack(fill=BOTH, expand=1, padx=10, pady=10)
        print(dir(self.frame))
        self.table = CustomTable(self.frame, dataframe=df, showtoolbar=True, showstatusbar=True)

        self.table.show()

        self.options = config.load_options()
        self.options = {'floatprecision': 5, 'cellwidth': 40, 'fontsize': 14, }
        config.apply_options(self.options, self.table)
        self.table.show()
        self.table.redraw()


class CustomTable(Table):
    def __init__(self, parent, dataframe=None, **kwargs):
        super().__init__(parent, dataframe=dataframe, **kwargs)

    # Sobrescribimos el método drawCell para colorear celdas según la condición
    def drawCell(self, row, col, text, fgcolor, bgcolor, align, font, width, canvas, **kwargs):
        value = str(self.model.getValueAt(row, col))

        # Condición: si la celda contiene 'Ma', cambiar el color de fondo a amarillo
        if 'Ma' in value:
            bgcolor = 'red'

        # Llamamos al método original con el nuevo color de fondo
        super().drawCell(row, col, text, fgcolor, bgcolor, align, font, width, canvas, **kwargs)

    def set_color_conditions(self):
        # Recorremos todas las celdas del DataFrame para encontrar las que contienen 'Ma'
        df = self.table.model.df
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                value = str(df.iat[row, col])
                if 'Ma' in value:
                    # Asignamos un color específico a la celda
                    self.table.model.draw(row, col, 'yellow')  # Color amarillo para las celdas con 'Ma'
                    self.table.redraw()