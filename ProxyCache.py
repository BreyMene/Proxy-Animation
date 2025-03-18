from manim import *

class ProxyCache(Scene):
    def construct(self):
        self.intro()
    
    def intro(self):
        # Título en la parte superior
        title = Text("Proxy de Caché").scale(0.6).to_edge(UP)
        
        # Cargar imágenes y ajustar tamaños
        user = ImageMobject("Images/user.png").scale(0.6).to_edge(LEFT)
        proxy = ImageMobject("Images/proxy.png").scale(0.3).move_to(ORIGIN)
        database = ImageMobject("Images/database.png").scale(0.6).to_edge(RIGHT)
        cache_storage = ImageMobject("Images/cache.png").scale(0.3).next_to(proxy, DOWN * 2)
        
        # Línea punteada entre el proxy y la caché (inicialmente oculta)
        cache_line = DashedLine(proxy.get_bottom(), cache_storage.get_top(), color=WHITE)
        
        # Etiquetas
        user_label = Text("Usuario").scale(0.4).next_to(user, DOWN)
        proxy_label = Text("Proxy").scale(0.4).next_to(proxy, UP)
        db_label = Text("Base de Datos").scale(0.4).next_to(database, DOWN)
        cache_label = Text("Caché").scale(0.4).next_to(cache_storage, DOWN)
        
        # Paquetes de datos (petición)
        requests = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
        requests.arrange(RIGHT, buff=0.15).next_to(user, RIGHT)
        
        # Respuesta desde la base de datos
        response = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
        response.arrange(RIGHT, buff=0.15).move_to(database.get_left() + LEFT * 0.5)
        
        # Mostrar elementos iniciales
        self.play(FadeIn(title, user, proxy, database, user_label, proxy_label, db_label))
        
        # Primera solicitud (sin caché)
        self.play(FadeIn(requests))
        self.move_requests(requests, proxy)
        self.wait(1)
        
        # Proxy no tiene caché, envía a la base de datos
        self.move_requests(requests, database)
        self.wait(1)
        
        # La base de datos responde
        self.play(FadeIn(response))
        self.move_requests(response, proxy)
        self.wait(1)
        
        # Aparecen la caché y la línea punteada cuando el proxy recibe datos
        self.play(FadeIn(cache_storage), FadeIn(cache_label), FadeIn(cache_line))
        
        # Proxy almacena en caché y envía respuesta al usuario
        cache_response = response.copy()
        self.play(cache_response.animate.move_to(cache_storage.get_center()), run_time=1)
        self.play(FadeOut(cache_response))  # Eliminar copia en caché después de almacenarla
        self.move_requests(response, user)
        self.wait(2)
        
        # Segunda solicitud (con caché)
        new_requests = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
        new_requests.arrange(RIGHT, buff=0.15).next_to(user, RIGHT)
        self.play(FadeIn(new_requests))
        self.move_requests(new_requests, proxy)
        self.wait(1)
        
        # Proxy obtiene los datos desde la caché antes de enviarlos al usuario
        cached_response = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
        cached_response.arrange(RIGHT, buff=0.15).move_to(cache_storage.get_center())
        self.play(FadeIn(cached_response))
        self.move_requests(cached_response, proxy)
        self.wait(1)
        self.move_requests(cached_response, user)
        self.wait(2)
    
    def move_requests(self, requests, target, run_time=1.5):
        self.play(requests.animate.move_to(target.get_center()), run_time=run_time)
        for dot in requests:
            self.play(dot.animate.set_opacity(0.3), run_time=0.2)
            self.play(dot.animate.set_opacity(1), run_time=0.2)
            self.play(FadeOut(dot), run_time=0.3)
