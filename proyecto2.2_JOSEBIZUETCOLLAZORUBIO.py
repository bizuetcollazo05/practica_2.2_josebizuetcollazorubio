#NOMBRE:JOSE BIZUET COLLAZO RUBIO
#CARRERA:INFORMATICA
#MATERIA:DESAROLLO DE APLICASIONES
#EJERCISIO O PRACTICA: PRACTICA_2.2_JOSEBIZUETCOLLAZORUBIO
fecha=input("fecha(formato ´dia, DD/MM´):")#(ESTO SE CONSIDERA COMO UN ESTRIN LITERAL )aqui indico que ingrese DOS DIGITOS PARA EL DIA Y DOS PARA EL MES 
fecha=fecha.lower()#esto combierte las minusculas las letras pero si ya estan en minusculas no afectara en nada
diasemana=fecha[0:fecha.find(",")]#aqui extraremos los dias de la semana,tambien indico que empieze del cero asta el x numero de letras tendra el dia que ingrese para que la  coma se coloque
dianro=int(fecha[fecha.find(" ")+1:fecha.find("/")]) #aqui iniciamos en DD y enlugar de la como busacara la barra asi iniciara uno antes de la barra
mesnro=int(fecha[fecha.find("/")+1:])#aqui representamos el mes #aqui mostraremos uno despues de la bara asi como para el dia empezabamos uno despues del espasio
if dianro>31 or mesnro>12:#aqui colocamos la condicion que marcara la condicion incorrecta
    print("fecha incorrecta")
else:# aqui si la condicion es correcta continuara 
    if diasemana in "lunes, martes, miercoles":#aqui preguntara los de la semana es, aqui se preguntara si se tomaron examenes lunes ,martes o el miercoles 
        respuesta=input("¿setomaron examenes? S/N:")
        if respuesta.lower()=="s":
            aprobados=int(input("cantidad de aprobados:"))
            reprobados=int(input("cantidad de reprobados:"))
            print("porcentaje de aprobados:", (aprobados*100)/(aprobados+reprobados) ,"s" )#aqui calcularemos el porcentaje de aprobados y reprobados 
    elif diasemana =="jueves":# si el dia de la semana se escribe jueves se ara otra cosa que es el siguiente codigo
        asistencia=int(input("porcentaje de asistencia:"))#este es el codigo que se ejecuta cuando introducimos el dia jueves
        if asistencia>50:  #si es mayor nos dira no asisitio la mayoria y si es menor de 50 pues nos dira asistio la mayoria                               #este es el codigo que se ejecuta cuando introducimos el dia jueves
            print("Asistencia la mayoria")
        else: print("No asistio la mayoria")
    elif diasemana =="viernes":#aqui en viernes en esta parte nos dira que se inicio un nuevo siclo al colocar 1/7
        if dianro==1 and (mesnro==1 or mesnro==7):
            print("comienzo de nuevo ciclo")
            alumno=int(input("cantidad de alumnos:"))#nos pedira el numero demmalumnos
            arancel=float(input("arancel:$"))#aqui escribiremos el arancel
            print("ingreso total:$", alumno*arancel)#nos arrojara el total del arancel y se finalizara el programa
    else:
        print("fcha incorrecta ")

print("fin del programa ")