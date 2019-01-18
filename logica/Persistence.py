# coding: utf-8

from DB.InsertarDatos import insertMatter
from DB.InsertarDatos import insertDocent
from DB.InsertarDatos import insertDate
from DB.Seleccionar_Datos import searchMatter
from DB.ActualizarDatos import upDate_Matter
from DB.EliminarDatos import deleteMatter
from DB.Seleccionar_Datos import searchDocent
from DB.ActualizarDatos import updateDocent
from DB.EliminarDatos import deleteDate
from DB.Seleccionar_Datos import obtenerFechas
from DB.EliminarDatos import deleteDocent
from DB.Seleccionar_Datos import obtenerMatter
from DB.Seleccionar_Datos import buscarMaterPorSemester
from DB.Seleccionar_Datos import buscarhorainiciofin
from DB.ActualizarDatos import updateDate
from DB.Seleccionar_Datos import obtenerFechasHour
from DB.ActualizarDatos import updateBMa
from DB.Seleccionar_Datos import obtenerFechaInduc

def register_Matter(codigo: str, name: str, ubi_Semester: int, numCredit: str, codRequisite: str, numHoursSem: int):
    cod = str(codigo)
    nam = str(name)
    ubi_Semeste = int(ubi_Semester)
    numCredi = str(numCredit)
    codRequisit = str(codRequisite)
    numHoursSema = int(numHoursSem)
    insertMatter(cod, nam, ubi_Semeste, numCredi, codRequisit, numHoursSema)


def register_Docent(name: str, state: str, limitHours: int, contract: str, phone: str, identification: str):
    nom: str = name
    stat: str = state
    limitHour: int = limitHours
    contra: str = contract
    phonen: str = phone
    identi: str = identification
    print(stat)
    print(limitHour)
    print(contra)
    print(phonen)
    print(nom)
    print(identi)
    insertDocent(nom, stat, limitHour, contra, phonen, identi)


def register_Date(date: str, origin: str, idBlock: int, ident: str):
    datee = str(date)
    orige = str(origin)
    idents = str(ident)
    insertDate(datee, orige, idBlock, idents)


def searchhMatter(codigo: str):
    return searchMatter(codigo)


def update_Matter(codigo: str, name: str, ubi_Semester: int, numCredit: str, codRequisite: str, numHoursSem: int):
    upDate_Matter(codigo, name, ubi_Semester, numCredit, codRequisite, numHoursSem)


def delete_Matter(codigo: str):
    return deleteMatter(codigo)


def search_Docent(ident: str):
    return searchDocent(ident)


def update_Docent(name: str, state: str, limitHours: int, contract: str, phone: str, identification: str):
    updateDocent(name, state, limitHours, contract, phone, identification)


def delete_Docent(identification: str):
    return deleteDocent(identification)


def delete_Date():
    print("entroooo")
    return deleteDate()


def updateDatee(date: str, origin: str, idBlock: int, idents: str):
    updateDate(date, origin, idBlock, idents)


def obtener_Fecha(idents: str):
    return obtenerFechas(idents)


def obtenerFechasP(idents: str, origin: str):
    return obtenerFechasHour(idents, origin)


def obtener_Matter():
    return obtenerMatter()

def obtenerFInduct(idents: str):
    return obtenerFechaInduc(idents)

def geneHours(semester: int, ciudad: str) -> list:
    hours: list = []
    if semester == 1:
        return geneHoursPrimerS(semester, ciudad, hours)
    elif semester == 2:
        return geneHoursSegundoS(semester, ciudad, hours)
    elif semester == 3:
        return geneHoursTercerS(semester, ciudad, hours)
    elif semester == 4:
        return geneHoursCuartoS(semester, ciudad, hours)
    elif semester == 5:
        return geneHoursQuintoS(semester, ciudad, hours)
    elif semester == 6:
        return geneHoursSextoS(semester, ciudad, hours)
    return None


def geneHoursPrimerS(semester, ciudad, horario: list):
    files: list = buscarMaterPorSemester(semester)
    fileshor: list = buscarhorainiciofin()
    auxlist: list = []
    print("entro aquii")
    print(files)
    print(fileshor)
    l = 0
    aux: str = ""
    for file in files:
        if l <= 2:
            updateBMa(file[2], 1)
        elif 2 < l <= 4:
            updateBMa(file[2], 2)
        elif l > 4:
            updateBMa(file[2], 3)
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


def geneHoursSegundoS(semester, ciudad, horario: list):
    files: list = buscarMaterPorSemester(semester)
    fileshor: list = buscarhorainiciofin()
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
            updateBMa(file[2], 2)
        elif l > 4:
            updateBMa(file[2], 3)
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


def geneHoursTercerS(semester, ciudad, horario: list):
    files: list = buscarMaterPorSemester(semester)
    fileshor: list = buscarhorainiciofin()
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


def geneHoursCuartoS(semester, ciudad, horario: list):
    files: list = buscarMaterPorSemester(semester)
    fileshor: list = buscarhorainiciofin()
    auxlist: list = []
    print("entro aquii")
    print(files)
    print(fileshor)
    l = 0
    aux: str = ""
    for file in files:
        if l <= 2:
            updateBMa(file[2], 1)
            print("entroo primera vez")
        elif 2 < l < 4:
            updateBMa(file[2], 2)
        elif l >= 4:
            updateBMa(file[2], 3)
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


def geneHoursQuintoS(semester, ciudad, horario: list):
    files: list = buscarMaterPorSemester(semester)
    fileshor: list = buscarhorainiciofin()
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
            updateBMa(file[2], 2)
        elif l >= 4:
            updateBMa(file[2], 3)
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

def geneHoursSextoS(semester, ciudad, horario: list):
    files: list = buscarMaterPorSemester(semester)
    fileshor: list = buscarhorainiciofin()
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
            updateBMa(file[2], 2)
        elif l >= 4:
            updateBMa(file[2], 3)
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
