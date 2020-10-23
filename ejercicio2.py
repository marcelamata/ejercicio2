class Total:
    def __init__(self):
        self.total = 0.00

    def cantidadIngresos(self, ingreso):
        self.total += ingreso
        print(
            f"La cantida ingresada es de ${ingreso:.2f} y el saldo es de ${self.total:.2f}"
        )

    def cantidadEgreso(self, egreso):
        self.total -= egreso
        print(f"El egreso es de ${egreso:.2f} y el saldo total es de ${self.total:.2f}")


class Ingresos:
    def __init__(self):
        self.ingresos = 0.00

    def sumarIngresos(self, cantidadSumanda):
        self.ingresos += cantidadSumanda
        return cantidadSumanda


class Egresos:
    def __init__(self):
        self.egreso = 0.00

    def sumarEgresos(self, cantidadRestada):
        self.egreso += cantidadRestada
        return cantidadRestada


finanzaPersonal = Total()
ingresos = Ingresos()
egresos = Egresos()

while True:
    Menu = """seleccione el numero que quiera
    0- salir de la aplicacion
    1- ingresar una cantidad
    2- retirar una cantidad
    3- reporte de ingresos
    4- reporte de egresos
    5- reporte de ambos
    6- saldo total
    """
    print(Menu)
    option = int(input("Ingrese el numeor que quiera "))
    if option == 0:
        break
    elif option == 1:
        ingreso = round(float(input("Ingrese la cantidad que va a ingresar ")), 2)
        finanzaPersonal.cantidadIngresos(ingresos.sumarIngresos(ingreso))
    elif option == 2:
        egreso = round(float(input("Ingrese la cantidad que desea retirar ")), 2)
        finanzaPersonal.cantidadEgreso(egresos.sumarEgresos(egreso))
    elif option == 3:
        totalIngresos = ingresos.ingresos
        print(f"Sus ingresos totales son de ${totalIngresos}")
    elif option == 4:
        totalEgreso = egresos.egreso
        print(f"Sus egresos totales son de ${totalEgreso}")
    elif option == 5:
        totalIngresos = ingresos.ingresos
        totalEgreso = egresos.egreso
        print(
            f"El reporte total es de ingresos ${totalIngresos} y egresos ${totalEgreso}"
        )
    elif option == 6:
        total = finanzaPersonal.total
        print(f"Su saldo es de ${total}")