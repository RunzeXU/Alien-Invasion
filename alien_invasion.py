import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from  scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, " PLAY ")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    sb = Scoreboard(ai_settings, screen, stats)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb)

        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, screen, stats, ship, aliens, bullets, sb)
            gf.update_bullets(ai_settings, screen, stats, ship, aliens, bullets, sb)
        gf.update_screen(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb)


run_game()
