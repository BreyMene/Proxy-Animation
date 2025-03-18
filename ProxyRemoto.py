from manim import *

class ProxyRemoto(Scene):
    def construct(self):
        self.intro()
    
    def intro(self):
        # Título
        title = Text("Proxy Remoto").scale(0.6).to_edge(UP)
        
        # Cargar imágenes y ajustar tamaños
        user = ImageMobject("Images/user.png").scale(0.6).to_edge(LEFT)
        proxy = ImageMobject("Images/proxy.png").scale(0.3).move_to(ORIGIN)
        server_real = ImageMobject("Images/server.png").scale(0.6).to_edge(RIGHT)
        
        # Servidores falsos en diferentes ubicaciones
        fake_server1 = ImageMobject("Images/server.png").scale(0.5).shift(UP * 2 + RIGHT * 3)
        fake_server2 = ImageMobject("Images/server.png").scale(0.5).shift(DOWN * 2 + RIGHT * 3)
        
        # Icono de denegación
        denial_icon = ImageMobject("Images/denied.png").scale(0.5).next_to(fake_server1, UP)
        
        # Etiquetas
        user_label = Text("Usuario").scale(0.4).next_to(user, DOWN)
        proxy_label = Text("Proxy").scale(0.4).next_to(proxy, DOWN)
        server_label = Text("Servidor Remoto").scale(0.4).next_to(server_real, DOWN)
        
        # Paquetes de datos
        requests = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
        requests.arrange(RIGHT, buff=0.15).next_to(user, RIGHT)
        
        # Mostrar elementos
        self.play(FadeIn(title, user, proxy, user_label, proxy_label, fake_server1, fake_server2, server_real, server_label))
        
        # Usuario no sabe cuál servidor usar
        unknown_location = Text("?").scale(1.5).next_to(user, UP)
        self.play(FadeIn(unknown_location))
        self.wait(1)
        self.play(FadeOut(unknown_location))
        
        # Intento fallido del usuario de contactar al servidor incorrecto (arriba)
        self.play(FadeIn(requests))
        self.move_requests(requests, fake_server1)
        self.play(FadeIn(denial_icon))  # Mostrar icono de denegación
        self.wait(1)
        self.play(FadeOut(denial_icon))
        self.wait(1)
        
        # Usuario reenvía la solicitud al proxy
        requests = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
        requests.arrange(RIGHT, buff=0.15).next_to(user, RIGHT)
        self.play(FadeIn(requests))
        self.move_requests(requests, proxy)
        self.wait(1)
        
        # Línea punteada para mostrar conexión secreta con el servidor correcto
        connection = DashedLine(proxy.get_right(), server_real.get_left(), color=BLUE)
        self.play(Create(connection))
        self.wait(1)
        
        # Enviar solicitud desde el proxy al servidor correcto
        self.move_requests(requests, server_real)
        self.wait(1)
        
        # Servidor responde con los círculos verdes de vuelta
        response = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
        response.arrange(RIGHT, buff=0.15).move_to(server_real.get_left() + LEFT * 0.5)
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
