from manim import *

class ProxyControlFlujo(Scene):
    def construct(self):
        self.intro()
    
    def intro(self):
        # Título
        title = Text("Proxy de Control de Flujo").scale(0.6).to_edge(UP)
        
        # Cargar imágenes y ajustar tamaños
        user1 = ImageMobject("Images/user.png").scale(0.3).to_edge(LEFT).shift(UP * 2)
        user2 = ImageMobject("Images/user.png").scale(0.3).to_edge(LEFT)
        user3 = ImageMobject("Images/user.png").scale(0.3).to_edge(LEFT).shift(DOWN * 2)
        proxy = ImageMobject("Images/proxy.png").scale(0.3).move_to(ORIGIN)
        server = ImageMobject("Images/server.png").scale(0.6).to_edge(RIGHT)
        
        # Etiquetas
        user1_label = Text("Usuario 1").scale(0.4).next_to(user1, DOWN)
        user2_label = Text("Usuario 2").scale(0.4).next_to(user2, DOWN)
        user3_label = Text("Usuario 3").scale(0.4).next_to(user3, DOWN)
        proxy_label = Text("Proxy").scale(0.4).next_to(proxy, DOWN)
        server_label = Text("Servidor").scale(0.4).next_to(server, DOWN)
        
        # Paquetes de datos (solicitudes de los usuarios en grupo)
        requests1 = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)]).arrange(RIGHT, buff=0.15).next_to(user1, RIGHT)
        requests2 = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)]).arrange(RIGHT, buff=0.15).next_to(user2, RIGHT)
        requests3 = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)]).arrange(RIGHT, buff=0.15).next_to(user3, RIGHT)
        
        # Mostrar elementos iniciales
        self.play(FadeIn(title, user1, user2, user3, proxy, server, user1_label, user2_label, user3_label, proxy_label, server_label))
        self.play(FadeIn(requests1, requests2, requests3))
        
        # Mover solicitudes en grupo al proxy con delay entre usuarios
        request_groups = [requests1, requests2, requests3]
        proxy_positions = [proxy.get_center() + UP * 0.5, proxy.get_center(), proxy.get_center() + DOWN * 0.5]
        
        animations = []
        for i, (requests, pos) in enumerate(zip(request_groups, proxy_positions)):
            animations.append(requests.animate.move_to(pos).set_run_time(1).set_delay(i * 0.5))
        self.play(*animations)
        
        for requests in request_groups:
            self.blink_requests(requests)
        
        # Procesar solicitudes en orden desde el proxy hasta el servidor y de regreso
        for requests, user, proxy_pos in zip(request_groups, [user1, user2, user3], proxy_positions):
            self.play(requests.animate.move_to(server.get_left() + LEFT * 0.5), run_time=1)
            self.blink_requests(requests)
            self.play(FadeOut(requests), run_time=0.5)  # Eliminar solicitud en el servidor
            
            # Generar respuesta desde el servidor
            response = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
            response.arrange(RIGHT, buff=0.15).move_to(server.get_left() + LEFT * 0.5)
            self.play(FadeIn(response))
            
            self.play(response.animate.move_to(proxy_pos), run_time=1)  # Volver a la misma posición en el proxy
            self.blink_requests(response)
            self.play(response.animate.move_to(user.get_right() + RIGHT * 0.5), run_time=1)
            self.blink_requests(response)
            self.play(FadeOut(response), run_time=0.5)
        
        self.wait(2)
    
    def blink_requests(self, requests):
        for dot in requests:
            self.play(dot.animate.set_opacity(0.3), run_time=0.2)
            self.play(dot.animate.set_opacity(1), run_time=0.2)