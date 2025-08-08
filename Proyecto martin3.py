class SistemaDeTransporte:
    def __init__(self):
        # Estaciones
        # e we pon las estaciones que hacen falta 
        self.estaciones = [
            "San Isidro", "Belenes", "Tabachines", "Periférico Norte", 
            "Independencia Norte", "Zoquipan", "Plaza Patria", "División del Norte", 
            "Vallarta", "Colón", "Mezquitán", "Facultad de Medicina", 
            "Seminario", "Américas", "Juárez", "San Juan de Dios", 
            "Washington", "Agua Azul", "Parque Metropolitano", "Estampida", 
            "Monumento", "CUCEI", "Unidad Deportiva", "El Dean", 
            "Abastos", "Fray Angélico", "Periférico Sur", "Adolf Horn"
        ]
        
        # ID de las líneas
        # Agregar las líneas faltantes
        self.ID_estaciones = {
            0: {"linea": "Línea 1", "color": "Amarillo"},
            1: {"linea": "Línea 1", "color": "Amarillo"},
            2: {"linea": "Línea 2", "color": "Naranja"},
            3: {"linea": "Línea 3", "color": "Azul"},
            4: {"linea": "Línea 1", "color": "Amarillo"},
            5: {"linea": "Línea 2", "color": "Naranja"},
            6: {"linea": "Línea 1", "color": "Amarillo"},
            7: {"linea": "Línea 2", "color": "Naranja"},
            8: {"linea": "Línea 1", "color": "Amarillo"},
            9: {"linea": "Línea 3", "color": "Azul"},
            10: {"linea": "Línea 1", "color": "Amarillo"},
            11: {"linea": "Línea 2", "color": "Naranja"},
            12: {"linea": "Línea 1", "color": "Amarillo"},
            13: {"linea": "Línea 3", "color": "Azul"},
            14: {"linea": "Centro", "color": "Verde"},
            15: {"linea": "Centro", "color": "Verde"},
            16: {"linea": "Línea 1", "color": "Amarillo"},
            17: {"linea": "Línea 3", "color": "Azul"},
            18: {"linea": "Línea 3", "color": "Azul"},
            19: {"linea": "Línea 2", "color": "Naranja"},
            20: {"linea": "Línea 1", "color": "Amarillo"},
            21: {"linea": "Línea 3", "color": "Azul"},
            22: {"linea": "Línea 2", "color": "Naranja"},
            23: {"linea": "Línea 2", "color": "Naranja"},
            24: {"linea": "Línea 2", "color": "Naranja"},
            25: {"linea": "Línea 1", "color": "Amarillo"},
            26: {"linea": "Línea 1", "color": "Amarillo"},
            27: {"linea": "Línea 1", "color": "Amarillo"},
        }
        
        self.n = len(self.estaciones)
        self.INF = float('inf')
        
        # Matriz
        self.matM = [
            [0, 1, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [1, 0, 2, 2, self.INF, self.INF, 7, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, 2, 0, 3, 2, self.INF, self.INF, 5, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [2, 2, 3, 0, 2, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 4, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, 2, 2, 0, 3, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, 3, 0, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, 7, self.INF, self.INF, self.INF, self.INF, 0, 4, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF],
            [self.INF, self.INF, 5, self.INF, self.INF, self.INF, 4, 0, 3, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, 3, 0, 2, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF],
            [self.INF, self.INF, self.INF, 3, self.INF, 3, self.INF, self.INF, 2, 0, self.INF, self.INF, self.INF, 4, 3, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, 0, 4, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 4],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, 4, 0, 2, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, 2, 0, 1, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 4, self.INF, self.INF, 1, 0, 2, self.INF, self.INF, 4, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, 2, 0, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, 3, self.INF, self.INF, self.INF, 0, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, 3, 0, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 4, self.INF, self.INF, 3, 0, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, 0, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, 0, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, 0, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, 4, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 0, 3, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, 0, 2, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, 0, 3, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, 0, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 0, 2, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, 0, 3],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 4, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, 0]
        ]
        
        self.matriz_siguiente = None
        self.iniciar = False
        
    # Inicia el nodo    
    def inicializar_matriz_siguiente(self):
        self.matriz_siguiente = [[-1 for _ in range(self.n)] for _ in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    self.matriz_siguiente[i][j] = i
                elif self.matM[i][j] != self.INF:
                    self.matriz_siguiente[i][j] = j
    
    # Floyd
    def floyd_warshall(self):
        if not self.iniciar:
            self.inicializar_matriz_siguiente()
        
        # Algoritmo Floyd
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if (self.matM[i][k] != self.INF and 
                        self.matM[k][j] != self.INF and
                        self.matM[i][k] + self.matM[k][j] < self.matM[i][j]):
                        
                        self.matM[i][j] = self.matM[i][k] + self.matM[k][j]
                        self.matriz_siguiente[i][j] = self.matriz_siguiente[i][k]
        
        self.iniciar = True
    
    # reconstruye el camino mas corto 
    def reconstruir_camino(self, inicio, fin):
        if not self.iniciar:
            self.floyd_warshall()
        
        if self.matriz_siguiente[inicio][fin] == -1:
            return []  # por si no hay camino
        
        camino = [inicio]
        actual = inicio
        
        while actual != fin:
            actual = self.matriz_siguiente[actual][fin]
            if actual == -1:
                return []  # Esto no esta funcioinando 
            camino.append(actual)
        
        return camino
    
    #Encontrar estacion por nombre
    #se puede usar minusculas???????
    def encontrar_estacion_nombre(self, nombre):
        nombre_minusculas = nombre.lower().strip()
        for i, estacion in enumerate(self.estaciones):
            if estacion.lower() == nombre_minusculas:
                return i
        return -1
    
    #aqui es donde se calcula la ruta 
    def calcular_ruta(self, nombre_inicio, nombre_destino):
        id_inicio = self.encontrar_estacion_nombre(nombre_inicio)
        id_destino = self.encontrar_estacion_nombre(nombre_destino)
        
        if id_inicio == -1:
            return {"error": f"Estación '{nombre_inicio}' no encontrada"}
        if id_destino == -1:
            return {"error": f"Estación '{nombre_destino}' no encontrada"}
        if id_inicio == id_destino:
            return {"error": "Las estaciones de origen y destino son las mismas"}
        
        camino = self.reconstruir_camino(id_inicio, id_destino)
        
        if not camino:
            return {"error": "No se encontró una ruta entre las estaciones"}
        
        #info de la ruta 
        pasos_ruta = []
        distancia_total = 0
        transferencias = 0
        linea_actual = ""
        
        for i, id_estacion in enumerate(camino):
            nombre_estacion = self.estaciones[id_estacion]
            info_estacion = self.ID_estaciones.get(id_estacion, {"linea": "Desconocida", "color": "Gris"})
            
            paso = {
                "estacion": nombre_estacion,
                "linea": info_estacion["linea"],
                "color": info_estacion["color"],
                "accion": "inicio" if i == 0 else ("destino" if i == len(camino) - 1 else "continuar")
            }
            
            if i > 0:
                #calcula las distancias entre las estaciones
                estacion_anterior = camino[i-1]
                distancia_paso = self.matM[estacion_anterior][id_estacion] - (self.matM[estacion_anterior][estacion_anterior] if i > 1 else 0)
                distancia_total += distancia_paso
                
                #por si te cambias 
                if info_estacion["linea"] != linea_actual and linea_actual != "":
                    transferencias += 1
                    paso["accion"] = "transferencia"
                
                linea_actual = info_estacion["linea"]
            else:
                linea_actual = info_estacion["linea"]
            
            pasos_ruta.append(paso)
        
        # Calcular distancia total correcta
        #nos hizo falta poner "pasos_ruta" no la va a mostrar
        distancia_total = self.matM[id_inicio][id_destino]
        
        return {
            "exito": True,
            "ruta": pasos_ruta,
            "distancia_total": distancia_total,
            "transferencias": transferencias,
            "total_estaciones": len(camino)
        }
    
    #te enseña las rutas disponibles
    def mostrar_ruta(self, info_ruta):
        if "error" in info_ruta:
            print(f"Error: {info_ruta['error']}")
            return
        
        print("\n" + "-"*50)
        print("RUTA RECOMENDADA")
        print("-"*50)
        
        for i, paso in enumerate(info_ruta["ruta"]):
            print(f"{i+1}. {paso['estacion']}")
            print(f"   Linea: {paso['linea']} ({paso['color']})")
            print(f"   Accion: {paso['accion'].upper()}")
            
            if i < len(info_ruta["ruta"]) - 1:
                print(" -> ")
                print("")

        print("\n" + "-"*50)
        print("RESUMEN DEL VIAJE")
        print("-"*50)
        print(f"Usted paso por: {info_ruta['total_estaciones']} estaciones.")
        print(f"Transferencias: {info_ruta['transferencias']}")
        print("-"*50)
    
    #te enseña las estaciones
    def mostrar_todas_estaciones(self):
        print("\n" + "-"*40)
        print("ESTACIONES DISPONIBLES")
        print("-"*40)
        
        for i, estacion in enumerate(self.estaciones):
            info_linea = self.ID_estaciones.get(i, {"linea": "Desconocida", "color": "Gris"})
            print(f"{i+1:2d}. {estacion} - {info_linea['linea']} ({info_linea['color']})")
        
        print("-"*40)

    #Floyd al 4
    def modo_interactivo(self):
        print("Sistema de Rutas de Transporte Público")
        print("Algoritmo Floyd-Warshall")
        print("="*40)
        
        #esta bien este menu?
        while True:
            print("\nOPCIONES:")
            print("1. Buscar ruta")
            print("2. Ver todas las estaciones")
            print("3. Salir")
            
            eleccion = input("\nSelecciona una opcion: ").strip()
            
            if eleccion == "1":
                estacion_origen = input("\nIngresa la estacion de ORIGEN: ").strip()
                estacion_destino = input("Ingresa la estacion de DESTINO: ").strip()
                
                if not estacion_origen or not estacion_destino:
                    print("Por favor ingresa ambas estaciones.")
                    continue
                
                print("\nCalculando...")
                info_ruta = self.calcular_ruta(estacion_origen, estacion_destino)
                self.mostrar_ruta(info_ruta)
                
            elif eleccion == "2":
                self.mostrar_todas_estaciones()
                
            elif eleccion == "3":
                print("Nos vemos")
                break
                
            else:
                print("Opcion no valida.")

#NO LE MUEVAS
def main():
    sistema_transporte = SistemaDeTransporte()
    sistema_transporte.modo_interactivo() 

if __name__ == "__main__":
    main()