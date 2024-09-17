def month_to_string(month_num):
    """

    :type month_num: number:

    """

    months_name = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
                   'Noviembre', 'Diciembre']

    index = month_num-1

    return months_name[index]