import database as db
import helpers

def iniciar():
    while True:
        helpers.limpiarPantalla()

        print('=======================')
        print(' Bienvenido al gestor ' )
        print('=======================')
        print('[1] Listar los clientes')
        print('[2] Buscar cliente     ')
        print('[3] Añadir un  cliente ')
        print('[4] Modificar un cliente')
        print('[5] Borrar un cliente  ')
        print('[6] Cerrar el gestor   ')
        print('=======================')

        opcion= input("> ")
        helpers.limpiarPantalla()

        if opcion == '1':
            print('Listando los clientes...\n')
            for cliente in db.Clientes.lista:
                print(cliente)
            
        elif opcion == '2':
            print('Buscando un cliente...\n')
            dni = helpers.leerTexto(3,3,'DNI (2 int y 1 chars)').upper()
            cliente= db.Clientes.buscar(dni)
            print(cliente) if cliente else print('Cliente no existe!')
            
        elif opcion == '3':
            print('Añadir un cliente...\n')
            dni=None
            while True:
                dni = helpers.leerTexto(3,3,'DNI (2 int y 1 chars)').upper()
                if helpers.dniValidate(dni,db.Clientes.lista):
                    break;
           
            nombre = helpers.leerTexto(2,30,'Nombre (de 2 a 30 chars)').capitalize()
            apellido = helpers.leerTexto(2,30,'Apellido (de 2 a 30 chars)').capitalize()
            db.Clientes.crear(dni,nombre,apellido)
            print('Cliente añadido exitosamente.')

            
        elif opcion == '4':
            print('Modificar un cliente...\n')
            dni = helpers.leerTexto(3,3,'DNI (2 int y 1 chars)').upper()
            cliente= db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leerTexto(2,30,f'Nombre (de 2 a 30 chars) [{cliente.nombre}]').capitalize()
                apellido = helpers.leerTexto(2,30,f'Apellido (de 2 a 30 chars) [{cliente.apellido}]').capitalize()
                db.Clientes.modificar(cliente.dni,nombre,apellido)
            
            else:
                print('Cliente no encontrado.')


            
        elif opcion == '5':
            print('Borrar un cliente...\n')
            dni = helpers.leerTexto(3,3,'DNI (2 int y 1 chars)').upper()
            print('Cliente borrado exitosamente!') if db.Clientes.borrar(
                dni) else print('No se pudo borrar comprueba')
            
        elif opcion == '6':
            print('Cerrando...\n')
            break;

        input('\nPresiona ENTER para continuar')


