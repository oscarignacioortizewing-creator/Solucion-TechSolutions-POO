# ==========================================
# PASO 2 Y 3: CLASE CLIENTE CON ENCAPSULAMIENTO
# ==========================================
class Cliente:
    def __init__(self, nombre, email, saldo_inicial):
        # Atributos públicos
        self.nombre = nombre
        self.email = email
        # Atributo privado (Encapsulamiento) para proteger el dinero
        self.__saldo = saldo_inicial 

    def actualizar_datos(self, nuevo_email):
        """Permite cambiar el correo del cliente."""
        self.email = nuevo_email
        print(f"✅ Datos de {self.nombre} actualizados.") 

    def consultar_saldo(self):
        """Método público para ver el saldo sin modificarlo directamente."""
        return self.__saldo 

    def depositar(self, monto):
        """Método para sumar dinero con validación."""
        if monto > 0:
            self.__saldo += monto
            return True
        return False

    def retirar(self, monto):
        """Método para restar dinero si hay suficiente saldo."""
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            return True
        return False

# ==========================================
# PASO 4: CLASE BANCO (INTERACCIÓN ENTRE OBJETOS)
# ==========================================
class Banco:
    def __init__(self):
        # Usamos un diccionario para guardar a los clientes por su email
        self.clientes = {} 

    def agregar_cliente(self, cliente):
        """Guarda un objeto de tipo Cliente en el banco."""
        self.clientes[cliente.email] = cliente
        print(f"🏦 Cliente {cliente.nombre} registrado con éxito.") 

    def realizar_transferencia(self, email_origen, email_destino, monto):
        """Lógica para que dos objetos Cliente interactúen entre sí."""
        if email_origen in self.clientes and email_destino in self.clientes:
            emisor = self.clientes[email_origen]
            receptor = self.clientes[email_destino]
            
            # Si el emisor puede retirar, el receptor recibe el depósito
            if emisor.retirar(monto):
                receptor.depositar(monto)
                print(f"💸 Transferencia exitosa: ${monto} de {emisor.nombre} a {receptor.nombre}.")
            else:
                print("❌ Fondos insuficientes para la transferencia.")
        else:
            print("❌ Error: Uno o ambos correos no existen.") 

# ==========================================
# PASO 5: EJEMPLO PRÁCTICO (SIMULACIÓN)
# ==========================================
if __name__ == "__main__":
    # 1. Creamos el sistema bancario
    mi_banco = Banco()

    # 2. Creamos (instanciamos) dos clientes
    ana = Cliente("Ana López", "ana@mail.com", 1000)
    juan = Cliente("Juan Pérez", "juan@mail.com", 500) 

    # 3. Los registramos en el banco
    mi_banco.agregar_cliente(ana)
    mi_banco.agregar_cliente(juan)

    # 4. Realizamos operaciones
    print(f"\nSaldo inicial de Ana: ${ana.consultar_saldo()}")
    mi_banco.realizar_transferencia("ana@mail.com", "juan@mail.com", 300)

    # 5. Mostramos resultados finales
    print(f"Saldo final de Ana: ${ana.consultar_saldo()}")
    print(f"Saldo final de Juan: ${juan.consultar_saldo()}") 
   

 

