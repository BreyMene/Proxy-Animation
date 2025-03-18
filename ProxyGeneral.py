from manim import *

class ProxyPpal(Scene):
    def construct(self):
        self.intro()
    
    def intro(self):
        # Cargar imágenes y ajustar tamaños
        user = ImageMobject("Images/user.png").scale(0.6).to_edge(LEFT)
        proxy = ImageMobject("Images/proxy.png").scale(0.3).move_to(ORIGIN)
        server = ImageMobject("Images/server.png").scale(0.6).to_edge(RIGHT)
        
        # Etiquetas para cada elemento
        user_label = Text("Usuario").scale(0.4).next_to(user, DOWN)
        proxy_label = Text("Proxy").scale(0.4).next_to(proxy, DOWN)
        server_label = Text("Servidor").scale(0.4).next_to(server, DOWN)
        
        # Crear grupo de paquetes de datos 
        requests = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
        requests.arrange(RIGHT, buff=0.15).next_to(user, RIGHT)
        
        # Mostrar los elementos en la escena
        self.play(FadeIn(user, proxy, server, user_label, proxy_label, server_label))
        self.play(FadeIn(requests))
        
        # Mover los paquetes en grupo pero con efecto de carga y pausa de 1 segundos
        self.move_requests(requests, proxy, run_time=1.5)
        self.wait(1)
        self.move_requests(requests, server, run_time=1.5)
        self.wait(1)
        self.move_requests(requests, proxy, run_time=1.5)
        self.wait(1)
        self.move_requests(requests, user, run_time=1.5)
        self.wait(1)
    
    def move_requests(self, requests, target, run_time=1.5):
        # Mover todo el grupo de paquetes juntos más lentamente
        self.play(requests.animate.move_to(target.get_center()), run_time=run_time)
        
        # Simular efecto de encendido y apagado (carga) al llegar al destino
        for dot in requests:
            self.play(dot.animate.set_opacity(0.3), run_time=0.2)
            self.play(dot.animate.set_opacity(1), run_time=0.2)
            self.play(FadeOut(dot), run_time=0.3)