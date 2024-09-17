import numpy as np
from shift_quadrant import new_squadrant, assign_init_shifts, day_min_shifts
from views.mainView import MainView
from tkinter import *

if __name__ == '__main__':

    month = 10
    year = 2024

    shift = {
        'Ma': 'Ma',
        'Ta': 'Ta',
        'No': 'No',
        'Li': 'Li'
    }

    employees = ['Andrei', 'Irina', 'Lucas', 'Abraham', 'Bitter']

    rotation = np.array(['Ta', 'Ta', 'Ta', 'Ta', 'Ta', 'Ta', 'Li', 'Li', 'Li',
                         'Ma', 'Ma', 'Ma', 'Ma', 'Ma', 'Ma', 'Li', 'Li', 'Li',
                         'No', 'No', 'No', 'No', 'No', 'No', 'Li', 'Li', 'Li', 'Li'])

    s_quadrant = new_squadrant(year, month, employees)

    assign_init_shifts(s_quadrant, rotation)



    # Aseguramos que después de una noche haya al menos un día libre
    for i, persona in enumerate(employees):
        for dia in range(len(s_quadrant.columns) - 1):
            # Si el turno actual es "Noche", el siguiente debe ser "Libre"
            if s_quadrant.iloc[i, dia] == 'No' and s_quadrant.iloc[i, dia + 1] != 'Li':
                s_quadrant.iloc[i, dia + 1] = 'Li'

    # Aseguramos que cada persona tenga al menos 3 días consecutivos libres
    for i, persona in enumerate(employees):
        dias_libres = 0
        tiene_3_dias_libres = False

        for dia in range(len(s_quadrant.columns)):
            if s_quadrant.iloc[i, dia] == 'Li':
                dias_libres += 1
            else:
                dias_libres = 0

            # Si encontramos 3 días consecutivos libres, cumplimos la regla
            if dias_libres >= 4:
                tiene_3_dias_libres = True
                break

        # Si la persona no tiene al menos 3 días libres consecutivos, los asignamos
        if not tiene_3_dias_libres:
            # Forzamos 3 días libres consecutivos al final del mes
            for dia_libre in range(len(s_quadrant.columns) - 3, len(s_quadrant.columns)):
                s_quadrant.iloc[i, dia_libre] = 'Li'

    # Aseguramos que cada empleado tenga al menos 10 días libres al mes
    for i, persona in enumerate(employees):
        dias_libres = np.sum(s_quadrant.loc[persona] == 'Li')

        if dias_libres < 10:
            # Añadir días libres hasta alcanzar al menos 7 días
            dias_faltantes = 10 - dias_libres
            for dia in range(len(s_quadrant.columns)):
                if s_quadrant.iloc[i, dia] != 'Li' and dias_faltantes > 0:
                    s_quadrant.iloc[i, dia] = 'Li'
                    dias_faltantes -= 1

    day_min_shifts(s_quadrant)
    s_quadrant.to_csv('sq_nuevo')
    root = Tk()
    root.geometry('1300x400')
    root.title('Cuadrantes')
    app = MainView(master=root, df=s_quadrant)
    root.mainloop()


    # print(s_quadrant.to_markdown())
