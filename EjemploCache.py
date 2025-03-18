class Objeto:
    def request(self, key):
        pass

class ObjetoReal(Objeto):
    def request(self, key):
        print(f"Obteniendo datos reales para {key}")
        return f"Datos para {key}"

class CacheProxy(Objeto):
    def __init__(self):
        self.cache = {}
        self.objeto_real = ObjetoReal()
    
    def request(self, key):
        if key not in self.cache:
            print(f"CacheProxy: No en caché, solicitando a ObjetoReal...")
            self.cache[key] = self.objeto_real.request(key)
        else:
            print(f"CacheProxy: Obteniendo {key} desde la caché")
        return self.cache[key]

# Uso del proxy
proxy = CacheProxy()
proxy.request("Usuario123")  # Primera vez, obtiene desde ObjetoReal
proxy.request("Usuario123")  # Segunda vez, obtiene desde la caché