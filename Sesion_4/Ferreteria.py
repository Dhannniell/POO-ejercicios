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
        

        # opcional 
        '''
        with cls._lock:
            if cls._instancia is None:
                cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
                cls._instancia._inicializacionHistorico()
            return cls._instancia 
        '''
        
    def _inicializacionHistorico(self):
        self.historial = []
        print("Sistema de Facturacion inicializado")
        
    def registrarOperacion(self, operacion):
        self.historial.append(operacion)
        print(f"La operacion fue registrada {operacion}")
        
        
# Clase Abstracta = Superclase
class ProcesoNegocio(ABC):
    
    @abstractmethod
    def ejecutar(self):
        pass 
    
class ProcesarPedido(ProcesoNegocio):
    
    def ejecutar(self):
        print("Procesando pedido...")
        return "Pedido procesado"
    
class ProcesarFactura(ProcesoNegocio):
    
    def ejecutar(self):
        print("Procesando factura...")
        return "Factura procesada"
    
# Crear la Fabrica (Patron Factory)
class FabricaProcesosNegocio:
    
    @staticmethod
    def crearProcesos(tipoProceso):
        
        if tipoProceso == "pedido":
            return ProcesarPedido()
        elif tipoProceso == "factura":
            return ProcesarFactura()
        else:
            raise ValueError(f"El proceso {tipoProceso} no existe")
        
if __name__ == "__main__":
    
    sistema_facturacion = SistemaFacturacion()
    
    proceso1 = FabricaProcesosNegocio.crearProcesos("pedido")
    proceso2 = FabricaProcesosNegocio.crearProcesos("factura")
    
    resultadoPedido1 = proceso1.ejecutar()
    sistema_facturacion.registrarOperacion(resultadoPedido1)
    
    resultadoPedido2 = proceso2.ejecutar()
    sistema_facturacion.registrarOperacion(resultadoPedido2)
    
    print("\nHistorico de Procesos de Negocios \n")
    for operacion in sistema_facturacion.historial:
        print(f"Transaccion: {operacion}")