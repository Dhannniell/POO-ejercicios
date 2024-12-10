# Interface


from abc import ABC, abstractmethod

class ProcesoPago(ABC):
    
    @abstractmethod
    def procesoPago(self, cantidad: float) -> None:
        pass
    
    @abstractmethod
    def reembolsoPago(self, transaccionId: str) -> None:
        pass
    
class Paypal(ProcesoPago):
    
    def procesoPago(self, cantidad: float) -> None:
        print(f"Procesando pago de ${cantidad} por Paypal")
        
    def reembolsoPago(self, transaccionId: str) -> None:
        print(f"Reembolsando Id transaccion numero: {transaccionId} por Paypal")
        
class Stripe(ProcesoPago):
    
    def procesoPago(self, cantidad: float) -> None:
        print(f"Procesando pago de ${cantidad} por Stripe")
        
    def reembolsoPago(self, transaccionId: str) -> None:
        print(f"Reembolsando Id transaccion numero: {transaccionId} por Stripe")
        
        
if __name__ == "__main__":
    procesoPaypal = Paypal()
    procesoStripe = Stripe()
    
    procesoPaypal.procesoPago(500.0)
    procesoPaypal.reembolsoPago("FDCS125789X987")
    print("---------------------------------------------------------------------------")
    procesoStripe.procesoPago(988.0)
    procesoStripe.reembolsoPago("EFR102SDFG129X987")