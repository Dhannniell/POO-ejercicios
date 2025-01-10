import threading
from abc import ABC, abstractmethod

# Patron Singleton 
class SistemaFacturacion:
    
    _instancia = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        
        if not cls._instancia: 
            cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
            cls._instancia._inicializacionHistorico()
        return cls._instancia
        
    def _inicializacionHistorico(self):
        self.historial = []
        print("Sistema de Facturacion inicializado")
        
    def registrarOperacion(self, operacion):
        self.historial.append(operacion)
        print(f"La operacion fue registrada: {operacion}")
        
# Clase Abstracta = Superclase 
class ProcesoNegocio(ABC):
    
    @abstractmethod
    def ejecutar(self):
        pass 
    
class ProcesarPedido(ProcesoNegocio):
    
    def ejecutar(self):
        print("Procesando el pedido el pedido...")
        return "Pedido procesado"
    
class ProcesarFactura(ProcesoNegocio):
    
    def ejecutar(self):
        print("Procesando el pedido la factura...")
        return "Factura procesada"
    
# Crear la fabrica (Patron de diseño Factory)

class FabricaProcesosNegocio:
    
    @staticmethod
    def crearProceso(tipoProceso):
        
        if tipoProceso == "pedido":
            return ProcesarPedido()
        elif tipoProceso =="factura":
            return ProcesarFactura()
        else:
            raise ValueError(f"El proceso {tipoProceso} no existe")
        
if __name__ == "__main__":
    
    sistema_facturacion = SistemaFacturacion()
    
    proceso1 = FabricaProcesosNegocio.crearProceso("pedido")
    proceso2 = FabricaProcesosNegocio.crearProceso("factura")
    
    resultadoPedido1 = proceso1.ejecutar()
    sistema_facturacion.registrarOperacion(resultadoPedido1)
    
    resultadoPedido2 = proceso2.ejecutar()
    sistema_facturacion.registrarOperacion(resultadoPedido2)
    
    print("\nHistorico de procesos de Negocios \n")
    for operacion in sistema_facturacion.historial:
        print(f"Transaccion: {operacion}")