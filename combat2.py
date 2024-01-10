import pygame, time, math, random, requests, io
from pygame.locals import *
from urllib.request import urlopen
from fenetre import Fenetre

pygame.init()

black = (0, 0, 0)
gold = (218, 165, 32)
grey = (200, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)

# Url de l'API pokéapi
base_url = 'https://pokeapi.co/api/v2'