import time
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


class TrafficLight:
    colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0)]
    times_color = [7, 2, 5]
    def running(self):
        while True:
            for color, t in zip(TrafficLight.colors, TrafficLight.times_color):
                screen.fill(color)
                pygame.display.update()
                time.sleep(t)


light = TrafficLight()
light.running()