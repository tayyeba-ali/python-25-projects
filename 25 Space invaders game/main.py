import math
import random
import pygame
from pygame import mixer
import os

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED = 10
MAX_ENEMIES = 6

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game assets
class Assets:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        images_path = os.path.join(base_path, 'images')
        sounds_path = base_path

        # Images
        self.background = pygame.image.load(os.path.join(images_path, 'background.png'))
        self.player_img = pygame.image.load(os.path.join(images_path, 'player.png'))
        self.enemy_img = pygame.image.load(os.path.join(images_path, 'enemy.png'))
        self.bullet_img = pygame.image.load(os.path.join(images_path, 'bullet.png'))
        self.icon = pygame.image.load(os.path.join(images_path, 'ufo.png'))
        
        # Sounds
        mixer.music.load(os.path.join(sounds_path, "background.wav"))
        self.bullet_sound = mixer.Sound(os.path.join(sounds_path, "laser.wav"))
        self.explosion_sound = mixer.Sound(os.path.join(sounds_path, "explosion.wav"))
        
        # Fonts
        self.score_font = pygame.font.Font('freesansbold.ttf', 32)
        self.game_over_font = pygame.font.Font('freesansbold.ttf', 64)

# Game objects
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.img = assets.player_img
        
    def update(self):
        self.x += self.speed
        # Boundary checking
        self.x = max(0, min(self.x, SCREEN_WIDTH - 64))
        
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def fire_bullet(self):
        return Bullet(self.x, self.y)

class Enemy:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - 64)
        self.y = random.randint(50, 150)
        self.speed_x = ENEMY_SPEED_X
        self.speed_y = ENEMY_SPEED_Y
        self.img = assets.enemy_img
        
    def update(self):
        self.x += self.speed_x
        
        # Change direction when hitting screen edges
        if self.x <= 0 or self.x >= SCREEN_WIDTH - 64:
            self.speed_x *= -1
            self.y += self.speed_y
            
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
    def check_collision(self, bullet):
        distance = math.sqrt(math.pow(self.x - bullet.x, 2) + math.pow(self.y - bullet.y, 2))
        return distance < 27

class EnemyBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7
        self.img = assets.bullet_img
        self.state = "fire"
        
    def update(self):
        self.y += self.speed
        if self.y >= SCREEN_HEIGHT:
            self.state = "ready"
            
    def draw(self):
        screen.blit(self.img, (self.x + 16, self.y + 10))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = BULLET_SPEED
        self.img = assets.bullet_img
        self.state = "fire"
        assets.bullet_sound.play()
        
    def update(self):
        self.y -= self.speed
        if self.y <= 0:
            self.state = "ready"
            
    def draw(self):
        screen.blit(self.img, (self.x + 16, self.y + 10))

# Game state
class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.player = Player(370, 480)
        self.enemies = [Enemy() for _ in range(MAX_ENEMIES)]
        self.bullets = []
        self.enemy_bullets = []
        self.player_lives = 3
        self.level = 1
        self.game_started = False
        
    def reset(self):
        self.score = 0
        self.game_over = False
        self.player = Player(370, 480)
        self.enemies = [Enemy() for _ in range(MAX_ENEMIES)]
        self.bullets = []
        self.enemy_bullets = []
        self.player_lives = 3
        self.level = 1
        self.game_started = True
        
    def update(self):
        if not self.game_started:
            return
        
        if self.game_over:
            return
            
        self.player.update()
        
        # Update enemies
        for enemy in self.enemies:
            enemy.update()
            
            # Enemy shooting logic
            if random.randint(0, 1000) < 10:  # Adjust shooting frequency here
                if len(self.enemy_bullets) < 5:  # Limit number of enemy bullets
                    self.enemy_bullets.append(EnemyBullet(enemy.x, enemy.y))
            
            # Check for game over condition based on enemy position
            if enemy.y > 440:
                self.player_lives = 0
                self.game_over = True
                
            # Check collision with bullets
            for bullet in self.bullets[:]:
                if bullet.state == "fire" and enemy.check_collision(bullet):
                    assets.explosion_sound.play()
                    bullet.state = "ready"
                    self.score += 1
                    enemy.x = random.randint(0, SCREEN_WIDTH - 64)
                    enemy.y = random.randint(50, 150)
                    
        # Update bullets
        for bullet in self.bullets[:]:
            if bullet.state == "fire":
                bullet.update()
            else:
                self.bullets.remove(bullet)
        
        # Update enemy bullets
        for e_bullet in self.enemy_bullets[:]:
            if e_bullet.state == "fire":
                e_bullet.update()
                # Check collision with player
                distance = math.sqrt(math.pow(self.player.x - e_bullet.x, 2) + math.pow(self.player.y - e_bullet.y, 2))
                if distance < 27:
                    assets.explosion_sound.play()
                    self.player_lives -= 1
                    e_bullet.state = "ready"
                    if self.player_lives <= 0:
                        self.game_over = True
            else:
                self.enemy_bullets.remove(e_bullet)
        
        # Level up logic
        if self.score >= self.level * 10:
            self.level += 1
            # Increase enemy speed
            for enemy in self.enemies:
                enemy.speed_x += 1 if enemy.speed_x > 0 else -1
            # Optionally add more enemies up to a max
            if len(self.enemies) < 10:
                self.enemies.append(Enemy())
                
    def draw(self):
        if not self.game_started:
            self.draw_start_screen()
            return
        
        # Draw background
        screen.blit(assets.background, (0, 0))
        
        # Draw player
        self.player.draw()
        
        # Draw enemies
        for enemy in self.enemies:
            enemy.draw()
            
        # Draw bullets
        for bullet in self.bullets:
            if bullet.state == "fire":
                bullet.draw()
        
        # Draw enemy bullets
        for e_bullet in self.enemy_bullets:
            if e_bullet.state == "fire":
                e_bullet.draw()
                
        # Draw score
        score_text = assets.score_font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        # Draw lives
        lives_text = assets.score_font.render(f"Lives: {self.player_lives}", True, (255, 255, 255))
        screen.blit(lives_text, (10, 50))
        
        # Draw game over
        if self.game_over:
            self.draw_game_over_screen()

# Initialize assets
assets = Assets()
pygame.display.set_caption("Space Invader")
pygame.display.set_icon(assets.icon)
mixer.music.play(-1)  # Play background music on loop

# Main game loop
def main():
    game = Game()
    running = True
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if not game.game_started:
                    game.game_started = True
                else:
                    if event.key == pygame.K_LEFT:
                        game.player.speed = -PLAYER_SPEED
                    if event.key == pygame.K_RIGHT:
                        game.player.speed = PLAYER_SPEED
                    if event.key == pygame.K_SPACE:
                        game.bullets.append(game.player.fire_bullet())
                    if event.key == pygame.K_r and game.game_over:
                        game.reset()
                        
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    game.player.speed = 0
        
        # Update game state
        game.update()
        
        # Draw everything
        game.draw()
        
        # Update display
        pygame.display.update()

    pygame.quit()

    # Additional draw methods for start and game over screens
def draw_text_centered(text, font, color, surface, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(SCREEN_WIDTH // 2, y))
    surface.blit(text_obj, text_rect)

def draw_start_screen(self):
    screen.fill((0, 0, 0))
    draw_text_centered("SPACE INVADERS", assets.game_over_font, (255, 255, 255), screen, SCREEN_HEIGHT // 3)
    draw_text_centered("Press any key to start", assets.score_font, (255, 255, 255), screen, SCREEN_HEIGHT // 2)
    pygame.display.update()

def draw_game_over_screen(self):
    screen.fill((0, 0, 0))
    draw_text_centered("GAME OVER", assets.game_over_font, (255, 255, 255), screen, SCREEN_HEIGHT // 3)
    draw_text_centered(f"Final Score: {self.score}", assets.score_font, (255, 255, 255), screen, SCREEN_HEIGHT // 2)
    draw_text_centered("Press R to Restart", assets.score_font, (255, 255, 255), screen, SCREEN_HEIGHT // 1.5)
    pygame.display.update()

# Bind the new draw methods to Game class
setattr(Game, "draw_start_screen", draw_start_screen)
setattr(Game, "draw_game_over_screen", draw_game_over_screen)

if __name__ == "__main__":
    main()
