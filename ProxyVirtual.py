from manim import *

class ProxyVirtual(Scene):
    def construct(self):
        self.intro()
    
    def intro(self):
        # Título
        title = Text("Proxy Virtual").scale(0.6).to_edge(UP)
        
        # Cargar imágenes y ajustar tamaños
        user = ImageMobject("Images/user.png").scale(0.6).to_edge(LEFT)
        proxy = ImageMobject("Images/proxy.png").scale(0.3).move_to(ORIGIN)
        server = ImageMobject("Images/server.png").scale(0.6).to_edge(RIGHT)
        file_icon = ImageMobject("Images/heavy_file.png").scale(0.3).next_to(server, UP)
        
        # Etiquetas para cada elemento
        user_label = Text("Usuario").scale(0.4).next_to(user, DOWN)
        proxy_label = Text("Proxy").scale(0.4).next_to(proxy, DOWN)
        server_label = Text("Servidor").scale(0.4).next_to(server, DOWN)
        file_label = Text("Archivo Pesado").scale(0.4).next_to(file_icon, UP)
        
        # Pensamiento del usuario preguntando por el archivo (sin nube de pensamiento, con imagen del archivo)
        thought_text = Text("¿Necesito").scale(0.4).next_to(user, UP, buff=0.3)
        thought_file = ImageMobject("Images/heavy_file.png").scale(0.2).next_to(thought_text, RIGHT)
        question_mark = Text("?").scale(0.4).next_to(thought_file, RIGHT)
        thought_group = Group(thought_text, thought_file, question_mark) 
        
        # Mostrar los elementos en la escena
        self.play(FadeIn(title, user, proxy, server, user_label, proxy_label, server_label))
        
        self.play(FadeIn(thought_group))
        self.wait(2)
        self.play(FadeOut(thought_group))
        self.wait(1)
        
        # SituaciónNecesita el archivo
        thought_text_2 = Text("Sí, lo necesito").scale(0.4).next_to(user, UP, buff=0.3)
        self.play(FadeIn(thought_text_2))
        self.wait(2)
        self.play(FadeOut(thought_text_2))
        
        # Enviar petición al proxy con los círculos verdes
        requests = VGroup(*[Dot(color=GREEN).scale(1) for _ in range(5)])
        requests.arrange(RIGHT, buff=0.15).next_to(user, RIGHT)
        self.play(FadeIn(requests))
        self.move_requests(requests, proxy, run_time=1.5)
        self.wait(1)
        self.move_requests(requests, server, run_time=1.5)
        self.wait(1)
        
        # Mostrar el archivo en el servidor al recibir la petición
        self.play(FadeIn(file_icon, file_label))
        self.wait(1)
        
        # Eliminar el texto del archivo antes de enviarlo
        self.play(FadeOut(file_label))
        
        # Enviar el archivo desde el servidor al usuario
        self.play(file_icon.animate.move_to(proxy.get_right() + RIGHT * 0.5), run_time=1.5)
        self.play(file_icon.animate.move_to(user.get_right() + RIGHT * 0.5), run_time=1.5)
        self.wait(2)
    
    def move_requests(self, requests, target, run_time=1.5):
        # Mover los paquetes al destino
        self.play(requests.animate.move_to(target.get_center()), run_time=run_time)
        
        # Desaparecer los paquetes progresivamente
        for dot in requests:
            self.play(dot.animate.set_opacity(0.3), run_time=0.2)
            self.play(dot.animate.set_opacity(1), run_time=0.2)
            self.play(FadeOut(dot), run_time=0.3)