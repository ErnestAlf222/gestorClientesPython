import config
import copy
import csv
import database as db
import helpers
import unittest

class TestDB(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista=[
            db.Cliente('22A','Ernesto','Sánchez'),
            db.Cliente('23B','Alejandro','Montiel'),
            db.Cliente('24C','Natalie Sofia','Sánchez Montiel'),

        ]
    
    def test_buscar_clientes(self):
        cliente_existente= db.Clientes.buscar('24C')
        cliente_inexistente= db.Clientes.buscar('99Z')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)
    
    def test_crear_cliente(self):
        new_Cliente= db.Clientes.crear('39X','Hector','Costa')
        self.assertEqual(len(db.Clientes.lista),4)
        self.assertEqual(new_Cliente.dni, '39X')
        self.assertEqual(new_Cliente.nombre,'Hector')
        self.assertEqual(new_Cliente.apellido,'Costa')
    
    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('22A'))
        clienteModificado= db.Clientes.modificar('22A','Ernesto Alfonso','Montiel')
        self.assertEqual(cliente_a_modificar.nombre, 'Ernesto')
        self.assertEqual(clienteModificado.nombre, 'Ernesto Alfonso')

    def test_borrar_cliente(self):
        clienteBorrado= db.Clientes.borrar('23B')
        clienteRebuscado=db.Clientes.buscar('23B')
        self.assertEqual(clienteBorrado.dni,'23B')
        self.assertIsNone(clienteRebuscado)

    def test_dniValido(self):
        self.assertTrue(helpers.dniValidate('29A',db.Clientes.lista))
        self.assertFalse(helpers.dniValidate('ERNE25',db.Clientes.lista))
        self.assertFalse(helpers.dniValidate('F35',db.Clientes.lista))
        self.assertFalse(helpers.dniValidate('23B',db.Clientes.lista))
    
    def testEscrituraCSV(self):
        db.Clientes.borrar('23B')
        db.Clientes.borrar('24C')
        db.Clientes.modificar('22A','alfonso','montiel')

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH,newline='\n') as fichero:
            reader= csv.reader(fichero,delimiter=';')
            dni, nombre, apellido = next(reader)
        self.assertEqual(dni, '22A')
        self.assertEqual(nombre, 'alfonso')
        self.assertEqual(apellido, 'montiel')

