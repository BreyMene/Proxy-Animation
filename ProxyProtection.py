from manim import *

class ProxyProteccion(Scene):
    def construct(self):
        self.intro()
    
    def intro(self):
        # Título
        title = Text("Proxy de Protección").scale(0.6).to_edge(UP)
        
        # Cargar imágenes y ajustar tamaños
        hacker = ImageMobject("Images/hacker.png").scale(0.6).shift(UP * 2 + LEFT * 4)
        user = ImageMobject("Images/user.png").scale(0.6).shift(DOWN * 2 + LEFT * 4)
        proxy = ImageMobject("Images/proxy.png").scale(0.3).move_to(ORIGIN)
        server = ImageMobject("Images/server.png").scale(0.6).to_edge(RIGHT)
        
        # Iconos de acceso
        denied_icon = ImageMobject("Images/access_denied.png").scale(0.3).next_to(proxy, UP)
        granted_icon = ImageMobject("Images/access_granted.png").scale(0.3).next_to(proxy, UP)
        
        # Candado cerrado desde el inicio
        lock_closed = ImageMobject("Images/lock_closed.png").scale(0.2).next_to(proxy, RIGHT)
        lock_open = ImageMobject("Images/lock_open.png").scale(0.2).next_to(proxy, RIGHT)
        
        # Etiquetas
        user_label = Text("Usuario").scale(0.4).next_to(user, DOWN)
        proxy_label = Text("Proxy").scale(0.4).next_to(proxy, DOWN)
        server_label = Text("Servidor").scale(0.4).next_to(server, DOWN)
        
        # Virus que intenta enviar el hacker
        virus = ImageMobject("Images/virus.png").scale(0.2).next_to(hacker, RIGHT)
        
        # Paquetes de datos del usuario autorizado
        requests = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
        requests.arrange(RIGHT, buff=0.15).next_to(user, RIGHT)
        
        # Mostrar elementos
        self.play(FadeIn(title, hacker, user, proxy, server, user_label, proxy_label, server_label, lock_closed))
        
        # Hacker intenta enviar un virus al servidor
        self.play(FadeIn(virus))
        self.play(virus.animate.move_to(proxy.get_left() + LEFT * 0.5), run_time=1.5)
        self.play(FadeIn(denied_icon))  # Mostrar acceso denegado
        self.wait(1)
        self.play(FadeOut(denied_icon, virus))  # Bloquear ataque
        self.wait(1)
        
        # Usuario autorizado envía solicitud
        self.play(FadeIn(requests))
        self.move_requests(requests, proxy)
        
        # Mostrar acceso permitido y abrir el candado
        self.play(FadeOut(lock_closed), FadeIn(granted_icon))
        self.wait(1)
        self.play(FadeOut(granted_icon), FadeIn(lock_open))
        
        # Permitir el paso de la solicitud hasta el servidor
        self.move_requests(requests, server)
        self.wait(1)
        
        # Respuesta del servidor de vuelta al usuario
        response = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
        response.arrange(RIGHT, buff=0.15).move_to(server.get_left() + LEFT * 0.5)
        self.play(FadeIn(response))
        self.move_requests(response, proxy)
        self.wait(1)
        self.move_requests(response, user)
        self.wait(2)
    
    def move_requests(self, requests, target, run_time=1.5):
        self.play(requests.animate.move_to(target.get_center()), run_time=run_time)
        for dot in requests:
            self.play(dot.animate.set_opacity(0.3), run_time=0.2)
            self.play(dot.animate.set_opacity(1), run_time=0.2)
            self.play(FadeOut(dot), run_time=0.3)
