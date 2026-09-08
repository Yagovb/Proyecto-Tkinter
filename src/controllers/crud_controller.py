# src/controllers/crud_controller.py

class ControladorMemoriaCRUD:
    def __init__(self, clave_primaria):
        self.clave_primaria = clave_primaria
        self.datos = []

    def crear(self, registro: dict):
        # Validación: Campos vacíos
        for clave, valor in registro.items():
            if not valor:
                raise ValueError(f"El campo '{clave}' no puede estar vacío.")

        # Validación: Duplicados por clave primaria
        valor_clave = registro.get(self.clave_primaria)
        if any(item[self.clave_primaria] == valor_clave for item in self.datos):
            raise ValueError(f"Ya existe un registro con {self.clave_primaria} = {valor_clave}.")

        self.datos.append(registro)
        return True

    def actualizar(self, valor_clave, registro_actualizado: dict):
        # Validación: Campos vacíos
        for clave, valor in registro_actualizado.items():
            if not valor:
                raise ValueError(f"El campo '{clave}' no puede estar vacío.")

        for i, item in enumerate(self.datos):
            if item[self.clave_primaria] == valor_clave:
                self.datos[i] = registro_actualizado
                return True
        raise ValueError("No se encontró el registro para actualizar.")

    def eliminar(self, valor_clave):
        for i, item in enumerate(self.datos):
            if item[self.clave_primaria] == valor_clave:
                del self.datos[i]
                return True
        raise ValueError("No se encontró el registro para eliminar.")

    def obtener_todos(self):
        return self.datos