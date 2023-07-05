import pygame, sys
from settings import *
from class_character import Character
# from animation_settings import dic_animations_character
from class_platform import Platform
from animation_settings import *
import random
from class_fire import Enemy_fire
from class_enemy_phamton import Enemy_phantom
from class_time import Cronometro
from windows import Item
from class_bull import Bull

# --------------------------------------------

class Level_1:
    def __init__(self):
        pygame.init()
        #pantalla 
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        self.background =  pygame.transform.scale(pygame.image.load("src/resources/image/menu/background.png"), SIZE_SCREEN)
        #plataforma
        self.platforms = Platform(lista_superficie)
        self.floor = self.platforms.rectangles[0]
        #personaje 
        self.character = Character(self.screen, self.platforms.rectangles)
        self.live = 3
        self.character_restart_game = self.character.rect
        #enemigos level 1
        self.sprite_phantom = pygame.sprite.Group()
        self.sprite_fire = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.character)
        #musica
        # pygame.mixer.music.load("src/resources/sound/sound_dificult_1.mp3")
        # pygame.mixer.music.set_volume(0.5)  # Ajusta el volumen de la música (opcional)
        self.music_level1 = pygame.mixer.Sound("src/resources/sound/sound_dificult_1.mp3")
        self.chanel_level1 = pygame.mixer.Channel(0)
        #Cronometro
        self.time = pygame.time.Clock()
        #evento bull
        #esta jugando 
        self.playing = False
        self.running = False
        self.is_game_over = False
        #fuente
        self.font_time = pygame.font.Font("src/resources/fonts/DS-DIGI.TTF", 80)
        self.font = pygame.font.Font("src/resources/fonts/Dark College.otf", 50)
        #cronometro
        self.cronometro = Cronometro(2, 30)
        self.is_pause = True
        self.menu_pause = Item(menu_items, self.font)
        self.menu_game_over = Item(game_over_items, self.font)
        self.font_game_over = pygame.font.Font("src/resources/fonts/Dark College.otf", 100)
        #pantalla win
        self.menu_win = Item(game_win_items, self.font)
        self.background_win = pygame.transform.scale(pygame.image.load("src/resources/image/menu/screen_main_menu.jpg"), SIZE_SCREEN)
        self.sound_monster = pygame.mixer.Sound("src/resources/sound/sound_enemy (2).mp3")
        self.sound_fire = pygame.mixer.Sound("src/resources/sound/sound_enemy.mp3")
        self.sound_game_over  = pygame.mixer.Sound("src/resources/sound/gameover.mp3")
        self.sprite_bull = pygame.sprite.Group()
        self.GENERAR_EVENTO_PHANTOM = pygame.USEREVENT + 1
        pygame.time.set_timer(self.GENERAR_EVENTO_PHANTOM, 6000)
        #evento fire
        self.GENERAR_EVENTO_FIRE = pygame.USEREVENT + 2
        pygame.time.set_timer(self.GENERAR_EVENTO_FIRE, 6000)
        self.GENERAR_BULL_EVENTO = pygame.USEREVENT + 3
        pygame.time.set_timer(self.GENERAR_BULL_EVENTO, random.randint(5000, 20000))
        self.sound_win = pygame.mixer.Sound("src/resources/sound/sound_win.mp3")
        self.sound_click = pygame.mixer.Sound("src/resources/sound/click.mp3")
        self.inicial_game = True


    # --------------------------------------------------------------------------------------------------
    def play(self):
        self.cronometro.start()
        self.running = True
        self.playing = True
        self.winer = False
        self.play_music()
        while self.running:
            self.time.tick(FPS)
            self.handle_events()
            self.update()
            self.render()



    # ------------------------------------------------------------------------------------------------
    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.sound_click.play()
                    if not self.is_pause:
                        self.is_pause = True
                        self.pause_game()
                    else:
                        self.is_pause = False
                        self.resume_game()

            elif event.type == self.GENERAR_EVENTO_FIRE and not self.is_pause and self.playing:
                self.sound_fire.play()
                for _ in range(random.randint(4, 10)):
                    direction = random.choice(["derecha", "izquierda", "arriba"])
                    velocidad = random.randint(2, 5)
                    fire = Enemy_fire(enemy_fire, direction , velocidad)
                    self.all_sprites.add(fire)
                    self.sprite_fire.add(fire)
                pygame.time.set_timer(self.GENERAR_EVENTO_FIRE, random.randint(5000, 10000))
                
            elif event.type == self.GENERAR_EVENTO_PHANTOM and not self.is_pause  and self.playing:
                self.sound_monster.play()
                self.generate_phantom()
                pygame.time.set_timer(self.GENERAR_EVENTO_PHANTOM, random.randint(2000, 10000))

            elif event.type == self.GENERAR_BULL_EVENTO and not self.is_pause  and self.playing:
                nuevo_bull = Bull(dic_bull, self.floor)
                nuevo_bull.sound.play()
                self.all_sprites.add(nuevo_bull)
                self.sprite_bull.add(nuevo_bull)
                pygame.time.set_timer(self.GENERAR_BULL_EVENTO, random.randint(2000, 10000))

            if self.is_pause:
                self.menu_pause.handle_event(event)
                if self.menu_pause.items[0].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.is_pause = False
                    self.resume_game()
                    self.sound_click.play()
                if self.menu_pause.items[1].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.running = False
            elif self.is_game_over:
                self.menu_game_over.handle_event(event)
                if self.menu_game_over.items[0].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.reset_game()
                    self.sound_click.play()
                if self.menu_game_over.items[1].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.running = False
            elif self.winer:
                self.menu_win.handle_event(event)
                if self.menu_win.items[0].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.reset_game()
                    self.sound_click.play()
                if self.menu_win.items[1].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.running = False
                

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and not keys[pygame.K_a]:   #CAMINA DERECHA
            self.character.left = False
            self.character.state = "camina_derecha"
            self.character.speed_x = SPEED
        
        elif keys[pygame.K_a] and not keys[pygame.K_d]: #CAMINA IZQUIERDA
            self.character.left = True
            self.character.state = "camina_izquierda"
            self.character.speed_x = -SPEED

        elif keys[pygame.K_SPACE]:
            self.character.state = "salta"
        elif keys[pygame.K_q]:
            self.character.state = "ataque"
        else:
            self.character.state = "quieto"
    # ----------------------------------------------------------------------------------------------------------
    def update(self):
        self.kill_enemy()
        self.detectet_collide()
        self.all_sprites.update()
        self.cronometro.update()

        if self.is_pause and self.inicial_game:
            self.pause_game()
            self.inicial_game = False
        elif self.cronometro.is_finished:
            self.sound_win.play()
            self.win()

    # -------------------------------------------------
    def render(self):
        if self.playing:
            self.show_game()
            if self.is_pause:
                self.menu_pause.draw(self.screen)
        elif self.is_game_over:
            self.show_game_over()
        elif self.winer:
            self.show_win()

        pygame.display.flip()

    # --------------------------------------------------------------------------}
    def generate_phantom(self):
        if len(self.sprite_phantom) == 0:
            for _ in range(10):
                rectangle = random.choice(self.platforms.rectangles)
                location = (random.randrange(rectangle.left, rectangle.right), rectangle.top)
                phantom = Enemy_phantom(dic_enemy_phantom, location, rectangle.right, rectangle.left)
                self.all_sprites.add(phantom)
                self.sprite_phantom.add(phantom)
    # -----------------------------------------------------------------------------------
    def detectet_collide(self):
        phantom_collide = pygame.sprite.spritecollide(self.character, self.sprite_phantom, True)
        if len(phantom_collide) != 0:
            self.live -= 1
            if self.live == 0:
                self.character.kill()
                self.game_over()

        fire_collide = pygame.sprite.spritecollide(self.character, self.sprite_fire, True)
        if len(fire_collide) != 0:
            self.live -= 1
            if self.live == 0:
                self.character.kill()
                self.game_over()
        bull_collide = pygame.sprite.spritecollide(self.character, self.sprite_bull, True)
        if len(bull_collide) != 0:
            self.live -= 1
            if self.live == 0:
                self.character.kill()
                self.game_over()
    # ---------------------------------------------------------------------------------------
    def kill_enemy(self):
        self.character.update_attack(self.all_sprites)
    # --------------------------------------------------------------------------
    def play_music(self):
        self.chanel_level1.play(self.music_level1, -1)  

    def pause_music(self):
        self.chanel_level1.pause() 

    def resume_music(self):
        self.chanel_level1.unpause() 
    def stop_music(self):
        self.chanel_level1.stop()  

    # ----------------------------------------------------------------------------------------
    def game_over(self):
        self.stop_music()
        self.cronometro.pause()
        for sprite in self.all_sprites:
            sprite.stop()
        self.playing = False
        self.is_game_over = True
        self.sound_game_over.play()

    def show_game_over(self):
        self.screen.fill((0, 0, 0))
        txt = self.font_game_over.render("GAME OVER", True, RED)
        self.screen.blit(txt, (400, 100))
        self.menu_game_over.draw(self.screen)
    # -----------------------------------------------------------------------------------------
    def reset_game(self):
        self.live = 3
        self.sprite_phantom.empty()
        self.sprite_fire.empty()
        self.all_sprites.empty()
        self.character = Character(self.screen, self.platforms.rectangles)
        self.all_sprites.add(self.character)
        self.cronometro.reset(2, 30)
        self.cronometro.start()
        self.is_game_over = False
        self.play_music()
        self.running = True
        self.is_pause = False
        self.playing = True
        self.winer = False

    # --------------------------------------------------------------------------------------------------------------------
    def pause_game(self):
        self.pause_music()  
        self.cronometro.pause() 
        for sprite in self.all_sprites:
            sprite.stop()
    # ------------------------------------------------------------------------------------------------------------------------
    def resume_game(self):
        self.resume_music()  
        self.cronometro.resume()  
        for sprite in self.all_sprites:
            sprite.resume()

    def show_win(self):
        self.screen.blit(self.background_win, ORIGIN)
        txt = self.font_game_over.render("WIN", True, GREEN)
        self.screen.blit(txt, (550, 100))
        self.menu_win.draw(self.screen)

    def win(self):
        self.stop_music()
        self.cronometro.pause()
        for sprite in self.all_sprites:
            sprite.stop()
        self.playing = False
        self.winer = True
    
    def show_game(self):
        self.screen.blit(self.background, ORIGIN)
        self.all_sprites.draw(self.screen)
        self.cronometro.draw(self.screen, self.font_time, (WIDTH // 2, 0), WHITE)
        txt = self.font.render("vidas: " + str(self.live), True, WHITE)
        self.screen.blit(txt, (1000, 20))


game = Level_1()
game.play()