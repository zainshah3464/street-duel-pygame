import pygame
import random
import requests
from io import BytesIO

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Fighting Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Load background images from URLs
image_urls = [
    "https://images.fastcompany.com/image/upload/f_webp,q_auto,c_fit/wp-cms/uploads/2024/01/p-1-91008617-what-killed-the-fight-scene-and-is-it-finally-coming-back.jpg",
    "https://thespinningpen.com/wp-content/uploads/2016/05/fight-scene.jpg?w=640"
]

def load_image_from_url(url):
    response = requests.get(url)
    img = pygame.image.load(BytesIO(response.content))
    return pygame.transform.scale(img, (WIDTH, HEIGHT))

bg_images = [load_image_from_url(url) for url in image_urls]
current_bg = random.choice(bg_images)

# Load player sprites
import requests
from io import BytesIO

# Load image from URL
def load_online_image(url):
    response = requests.get(url)
    img = pygame.image.load(BytesIO(response.content))
    return pygame.transform.scale(img, (80, 120))

# Correct way to load online images
player1_sprite = load_online_image("https://c4.wallpaperflare.com/wallpaper/750/589/116/anime-anime-girls-street-fighter-street-fighter-ii-the-world-warrior-chun-li-hd-wallpaper-preview.jpg")

player1_sprite = pygame.transform.scale(player1_sprite, (80, 120))
import requests
from io import BytesIO

# Load image from URL
def load_online_image(url):
    response = requests.get(url)
    img = pygame.image.load(BytesIO(response.content))
    return pygame.transform.scale(img, (80, 120))

# Correct way to load online images
player2_sprite = load_online_image("https://getwallpapers.com/wallpaper/full/1/4/c/1464573-beautiful-street-fighter-wallpaper-1920x1080-for-iphone-5s.jpg")
player2_sprite = pygame.transform.scale(player2_sprite, (80, 120))

# Player settings
player_size = 60
player1_x, player1_y = 100, HEIGHT - 150
player2_x, player2_y = 600, HEIGHT - 150
player_speed = 5
player1_health = 100
player2_health = 100

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(30)  # 30 FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    
    # Player 1 Controls (WASD + F to punch + G for special attack)
    if keys[pygame.K_a] and player1_x > 0:
        player1_x -= player_speed
    if keys[pygame.K_d] and player1_x < WIDTH - 80:
        player1_x += player_speed
    if keys[pygame.K_f]:  # Punch
        if abs(player1_x - player2_x) < 50:
            player2_health -= 5
    if keys[pygame.K_g]:  # Special Attack
        if abs(player1_x - player2_x) < 100:
            player2_health -= 15
            print("Player 1 Special Attack!")
    
    # Player 2 Controls (Arrow Keys + L to punch + K for special attack)
    if keys[pygame.K_LEFT] and player2_x > 0:
        player2_x -= player_speed
    if keys[pygame.K_RIGHT] and player2_x < WIDTH - 80:
        player2_x += player_speed
    if keys[pygame.K_l]:  # Punch
        if abs(player1_x - player2_x) < 50:
            player1_health -= 5
    if keys[pygame.K_k]:  # Special Attack
        if abs(player1_x - player2_x) < 100:
            player1_health -= 15
            print("Player 2 Special Attack!")
    
    # Drawing elements
    screen.blit(current_bg, (0, 0))  # Draw background
    screen.blit(player1_sprite, (player1_x, player1_y))  # Draw Player 1
    screen.blit(player2_sprite, (player2_x, player2_y))  # Draw Player 2
    
    # Health Bars
    pygame.draw.rect(screen, BLUE, (50, 20, player1_health * 2, 20))
    pygame.draw.rect(screen, RED, (WIDTH - 50 - player2_health * 2, 20, player2_health * 2, 20))
    
    # Check for Game Over
    if player1_health <= 0:
        print("Player 2 Wins!")
        running = False
    if player2_health <= 0:
        print("Player 1 Wins!")
        running = False
    
    pygame.display.update()
    
pygame.quit()
