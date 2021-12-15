# Servicio de Kinesiología - Hoja Ingreso UTI
# Sebatian Caivano - Manija Lab - caivanosebastian@gmail.com
# Julio 2021

import os
from datetime import datetime
import db
import read
import write

PATH = os.getcwd() + os.sep
PATH_DB = PATH + 'db' + os.sep + 'UTI.db'
PATH_INPUT = PATH + 'input' + os.sep
PATH_OUTPUT = PATH + 'output' + os.sep
PATH_TEMPLATE = PATH + 'templates' + os.sep
PATH_AUX = PATH + 'aux' + os.sep
TEMPLATE_NAME = 'Template_UTI.xlsx'


def main():
    if __name__ == "__main__":
        now = datetime.now()
        # dd/mm/YY H:M:S
        start = now.strftime("%d/%m/%Y %H:%M:%S")
        print("***** Servicio de Kinesiología - Hoja Ingreso UTI *****")
        print("Inicio de proceso de migración a Base de Datos: - " + start)

        db.CreateDB(PATH_DB)
        lst = []
        files = read.ReadInput(PATH_INPUT, PATH_DB)
        for file in files:
            values = read.ReadXLSX(PATH_INPUT, file)
            lst.append(values)

        file_output = write.WriteXLSX(PATH_TEMPLATE, TEMPLATE_NAME, lst, PATH_OUTPUT, PATH_DB)

        now = datetime.now()
        # dd/mm/YY H:M:S
        finish = now.strftime("%d/%m/%Y %H:%M:%S")
        print("Fin proceso de migración a Base de Datos: - " + finish)
        print("Cantidad de archivos procesados: - " + str(len(files)))
        print("Se ha creado el archivo: " + file_output)

        format = "%d/%m/%Y %H:%M:%S"
        time = str(datetime.strptime(finish, format) - datetime.strptime(start, format))
        print("El proceso duró: " + time)


main()
