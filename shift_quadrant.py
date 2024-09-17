import pandas as pd
import numpy as np
from datetime import date


def new_squadrant(year=date.today().year, month=date.today().month+1, employees=None):
    """
    :type employees: list,
    :type year: number,
    :type month: number

    """

    if employees is None:
        employees = ['employee1, employee2', 'employee3']

    days_month = pd.date_range(start=f'{year}-{month:02d}-01',
                               end=pd.Timestamp(f'{year}-{month:02d}-01') + pd.offsets.MonthEnd(1))

    sq = pd.DataFrame(columns=days_month.day, index=employees)

    sq.index = sq.index.astype(str)

    return sq


def assign_init_shifts(quadrant=None, rotation=None):
    for i, persona in enumerate(quadrant.index.tolist()):
        # Redimensionar la rotación para cubrir todos los días del mes y asignar a cada persona
        turnos_persona = np.resize(rotation, len(quadrant.columns))
        quadrant.loc[persona] = np.roll(turnos_persona, i * 7)  # Desplazar el ciclo para cada persona


def day_min_shifts(quadrant):
    # Ahora, aseguramos que cada día haya una persona en Mañana, Tarde y Noche
    for dia in quadrant.columns:
        # Obtener los turnos asignados para este día
        turnos_dia = quadrant[dia].values

        # Revisar si hay una persona en cada turno esencial (Mañana, Tarde, Noche)
        if 'Ma' not in turnos_dia or 'Ta' not in turnos_dia or 'No' not in turnos_dia:
            # Si falta alguno, reasignamos a alguien que esté "Libre"
            for i, turno in enumerate(turnos_dia):
                if turno == 'Li':
                    # Reasignar la persona al turno que falta
                    if 'Ma' not in turnos_dia:
                        quadrant.iloc[i, quadrant.columns.get_loc(dia)] = 'Ma'
                        turnos_dia[i] = 'Ma'
                    elif 'Ta' not in turnos_dia:
                        quadrant.iloc[i, quadrant.columns.get_loc(dia)] = 'Ta'
                        turnos_dia[i] = 'Ta'
                    elif 'No' not in turnos_dia:
                        quadrant.iloc[i, quadrant.columns.get_loc(dia)] = 'No'
                        turnos_dia[i] = 'No'
                    # Dejar de reasignar cuando se cubran los tres turnos esenciales
                    if 'Ma' in turnos_dia and 'Ta' in turnos_dia and 'No' in turnos_dia:
                        break