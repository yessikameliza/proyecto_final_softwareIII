# coding: utf-8

from DB.InsertarDatos import insert_matter
from DB.InsertarDatos import insert_docent
from DB.InsertarDatos import insert_date
from DB.Seleccionar_Datos import search_matter2
from DB.ActualizarDatos import update_matter1
from DB.EliminarDatos import delete_matter1
from DB.Seleccionar_Datos import search_docent2
from DB.ActualizarDatos import update_docent1
from DB.EliminarDatos import delete_date1
from DB.Seleccionar_Datos import obtener_fechas2
from DB.EliminarDatos import delete_docent1
from DB.Seleccionar_Datos import obtener_matter2
from DB.Seleccionar_Datos import buscar_mater_por_semester
from DB.Seleccionar_Datos import buscar_hora_inicio_fin
from DB.ActualizarDatos import update_date1
from DB.Seleccionar_Datos import obtener_fechas_hour2
from DB.ActualizarDatos import update_b_ma1
from DB.Seleccionar_Datos import obtener_fecha_indu2
from DB.Seleccionar_Datos import search_docent_matter

def register_matter(codigo: str, name: str, ubisemester: int, numcredit: str, codrequisite: str, numhourssem: int):
    insert_matter(codigo, name, ubisemester, numcredit, codrequisite, numhourssem)


def register_docent(name: str, state: str, limithours: int, contract: str, phone: str, identification: str,
                    matter: str, city: str):
    insert_docent(name, state, limithours, contract, phone, identification, matter, city)


def register_date(date: str, origin: str, idblock: int, ident: str):
    datee = str(date)
    orige = str(origin)
    idents = str(ident)
    insert_date(datee, orige, idblock, idents)


def search_matter(codigo: str):
    return search_matter2(codigo)


def update_matter(codigo: str, name: str, ubisemester: int, numcredit: str, codrequisite: str, numhourssem: int):
    update_matter1(codigo, name, ubisemester, numcredit, codrequisite, numhourssem)


def delete_matter(codigo: str):
    return delete_matter1(codigo)


def search_docent(ident: str):
    return search_docent2(ident)


def update_docent(name: str, state: str, limithours: int, contract: str, phone: str, identification: str, matter: str,
                  city: str):
    update_docent1(name, state, limithours, contract, phone, identification, matter, city)


def delete_docent(identification: str):
    return delete_docent1(identification)


def delete_date():
    print("entroooo")
    return delete_date1()


def update_datee(date: str, origin: str, idblock: int, idents: str):
    update_date1(date, origin, idblock, idents)


def obtener_fecha(idents: str):
    return obtener_fechas2(idents)


def obtener_fechas_p(idents: str, origin: str):
    return obtener_fechas_hour2(idents, origin)


def obtener_matter():
    return obtener_matter2()

def obtener_f_induct(idents: str):
    return obtener_fecha_indu2(idents)

def gene_hours(semester: int, ciudad: str) -> list:
    hours: list = []
    if semester == 1:
        return gene_hours_primer_s(semester, hours)
    elif semester == 2:
        return gene_hours_segundo_s(semester, hours)
    elif semester == 3:
        return gene_hours_tercer_s(semester, hours)
    elif semester == 4:
        return gene_hours_cuarto_s(semester, hours)
    elif semester == 5:
        return gene_hours_quinto_s(semester, hours)
    elif semester == 6:
        return gene_hours_sexto_s(semester, hours)
    return None

def obtener_datos_profe(semester: int, ciudad: str):
    auxx: list = []
    files: list = buscar_mater_por_semester(semester)
    print("materiaas segun el seemestreprofe", files)
    print("ciudad : ", ciudad)
    aux2: list = []
    for f in files:
        auxx.append(f[1])
        auxx.append(f[2])
        auxx.append(f[5])
        print(f[2], " : nombre materia")
        profe: list = search_docent_matter(f[2], ciudad)
        print(profe, " este profe persis")

        if profe is not None:
            auxx.append(profe[1])
            auxx.append(profe[5])
            aux2.append(auxx)
        auxx = []
    print("tabla completa", aux2)
    return aux2


def gene_hours_primer_s(semester, horario: list):
    files: list = buscar_mater_por_semester(semester)
    fileshor: list = buscar_hora_inicio_fin()
    auxlist: list = []
    print("entro aquii")
    print(files)
    print(fileshor)
    l = 0
    aux: str = ""
    for file in files:
        if l <= 2:
            update_b_ma1(file[2], 1)
        elif 2 < l <= 4:
            update_b_ma1(file[2], 2)
        elif l > 4:
            update_b_ma1(file[2], 3)
        print(file[2], " esto es aux")
        print(file[6], "esto es el bloque")
        if file[2] == "Metodologia Educacion a Distancia":
            num: int = int(file[7])
            number: int = int(num / 4)
            i = 0
            while i <= number:
                if i + 1 == number:
                    auxlist.append(fileshor[0] + " " + file[2])
                    auxlist.append(file[6])
                    horario.insert(1, auxlist)
                    auxlist = []
                else:
                    auxlist.append(fileshor[0] + " " + file[2] + "\t" + fileshor[1] + " " + file[2])
                    auxlist.append(file[6])
                    horario.insert(0, auxlist)
                    auxlist = []
                    print("este")
                    print(horario)
                i = i + 2
        else:
            # el if es para coger los valores intercalados
            if (l % 2) != 0:
                if l < 5:
                    aux = (files[l + 1])[2]
                else:
                    aux = file[2]
                num: int = int(file[7])
                print("numero", num)
                number: int = int(num / 4)
                print("number", number)
                i = 0
                while i < number:
                    auxlist.append(fileshor[0] + " " + file[2] + "\n" + fileshor[1] + " " + aux)
                    auxlist.append(file[6])
                    horario.append(auxlist)
                    auxlist = []
                    if aux == file[2]:
                        i = i + 2
                    else:
                        i = i + 1
        aux = ""
        l = l + 1
    print("horario final:")
    print(horario)
    return horario


def gene_hours_segundo_s(semester, horario: list):
    files: list = buscar_mater_por_semester(semester)
    fileshor: list = buscar_hora_inicio_fin()
    auxlist: list = []
    print("entro aquii")
    print(files)
    print(fileshor)
    l = 0
    aux: str = ""
    for file in files:
        if l < 2:
            update_b_ma1(file[2], 1)
            print("entroo primera vez")
        elif 2 <= l < 4:
            update_b_ma1(file[2], 2)
        elif l > 4:
            update_b_ma1(file[2], 3)
        print(file[2], " esto es aux")
        print(file[6], "esto es el bloque")
        print(file)
        # el if es para coger los valores intercalados
        if (l % 2) == 0:
            if l < 4:
                aux = (files[l + 1])[2]
            else:
                aux = file[2]
            num: int = int(file[7])
            print("numero", num)
            number: int = int(num / 4)
            print("number", number)
            i = 0
            while i < number:
                auxlist.append(fileshor[0] + " " + file[2] + "\n" + fileshor[1] + " " + aux)
                auxlist.append(file[6])
                horario.append(auxlist)
                auxlist = []
                if aux == file[2]:
                    i = i + 2
                else:
                    i = i + 1
        aux = ""
        l = l + 1
    print("horario final:")
    print(horario)
    return horario


def gene_hours_tercer_s(semester, horario: list):
    files: list = buscar_mater_por_semester(semester)
    fileshor: list = buscar_hora_inicio_fin()
    auxlist: list = []
    print("entro aquii")
    print(files)
    print(fileshor)
    l = 0
    aux: str = ""
    for file in files:
        # el if es para coger los valores intercalados
        if (l % 2) == 0:
            if l < 3:
                aux = (files[l + 1])[2]
            else:
                aux = file[2]
            num: int = int(file[7])
            print("numero", num)
            number: int = int(num / 4)
            print("number", number)
            i = 0
            while i < number:
                if i < number/2:
                    auxlist.append(fileshor[0] + " " + file[2] + "\n" + fileshor[1] + " " + aux)
                    auxlist.append(1)
                    horario.append(auxlist)
                    auxlist = []
                else:
                    aux = (files[l+2])[2]
                    print("este es el segunndo aux", aux)
                    auxlist.append(fileshor[0] + " " + file[2] + "\n" + fileshor[1] + " " + aux)
                    auxlist.append(2)
                    horario.append(auxlist)
                    auxlist = []
                if aux == file[2]:
                    i = i + 2
                else:
                    i = i + 1
        return horario
    print("horario final:")
    print(horario)
    return horario


def gene_hours_cuarto_s(semester, horario: list):
    files: list = buscar_mater_por_semester(semester)
    fileshor: list = buscar_hora_inicio_fin()
    auxlist: list = []
    print("entro aquii")
    print(files)
    print(fileshor)
    l = 0
    aux: str = ""
    for file in files:
        if l <= 2:
            update_b_ma1(file[2], 1)
            print("entroo primera vez")
        elif 2 < l < 4:
            update_b_ma1(file[2], 2)
        elif l >= 4:
            update_b_ma1(file[2], 3)
        num: int = int(file[7])
        print("numero", num)
        number: int = int(num / 4)
        if num == 12 or num == 16:
            aux = (files[0])[2]
            k = 0
            while k < number:
                print("entro condi", file[2])
                auxlist.append(fileshor[0] + " " + aux + "\n" + fileshor[1] + " " + file[2])
                auxlist.append(file[6])
                horario.append(auxlist)
                auxlist = []
                k = k + 1
        elif num == 8:
            auxlist.append(fileshor[0] + " " + file[2] + "\n" + fileshor[1] + " " + file[2])
            auxlist.append(file[6])
            horario.append(auxlist)
            auxlist = []
        aux = ""
        l = l + 1
    print("horario final:")
    print(horario)
    return horario


def gene_hours_quinto_s(semester, horario: list):
    files: list = buscar_mater_por_semester(semester)
    fileshor: list = buscar_hora_inicio_fin()
    auxlist: list = []
    print("entro aquii")
    print(files)
    print(fileshor)
    l = 0
    aux: str = ""
    for file in files:
        if l < 2:
            update_b_ma1(file[2], 1)
            print("entroo primera vez")
        elif 2 <= l < 4:
            update_b_ma1(file[2], 2)
        elif l >= 4:
            update_b_ma1(file[2], 3)
        print(file[2], " esto es aux")
        print(file[6], "esto es el bloque")
        print(file)
        # el if es para coger los valores intercalados
        if (l % 2) == 0:
            if l < 4:
                aux = (files[l + 1])[2]
            else:
                aux = file[2]
            num: int = int(file[7])
            print("numero", num)
            number: int = int(num / 4)
            print("number", number)
            i = 0
            while i < number:
                auxlist.append(fileshor[0] + " " + file[2] + "\n" + fileshor[1] + " " + aux)
                auxlist.append(file[6])
                horario.append(auxlist)
                auxlist = []
                if aux == file[2]:
                    i = i + 2
                else:
                    i = i + 1
        aux = ""
        l = l + 1
    print("horario final:")
    print(horario)
    return horario

def gene_hours_sexto_s(semester, horario: list):
    files: list = buscar_mater_por_semester(semester)
    fileshor: list = buscar_hora_inicio_fin()
    auxlist: list = []
    print("entro aquii")
    print(files)
    print(fileshor)
    l = 0
    aux: str = ""
    for file in files:
        if l < 2:
            updateBMa(file[2], 1)
            print("entroo primera vez")
        elif 2 <= l < 4:
            update_b_ma1(file[2], 2)
        elif l >= 4:
            update_b_ma1(file[2], 3)
        print(file[2], " esto es aux")
        print(file[6], "esto es el bloque")
        print(file)
        # el if es para coger los valores intercalados
        if (l % 2) == 0:
            if l < 4:
                aux = (files[l + 1])[2]
            else:
                aux = file[2]
            num: int = int(file[7])
            print("numero", num)
            number: int = int(num / 4)
            print("number", number)
            i = 0
            while i < number:
                auxlist.append(fileshor[0] + " " + file[2] + "\n" + fileshor[1] + " " + aux)
                auxlist.append(file[6])
                horario.append(auxlist)
                auxlist = []
                if aux == file[2]:
                    i = i + 2
                else:
                    i = i + 1
        aux = ""
        l = l + 1
    print("horario final:")
    print(horario)
    return horario
