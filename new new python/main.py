import pygame
import time
import random
import os  # Importeer de os-module voor het werken met bestandspaden

# Initialiseer Pygame
pygame.font.init()

# Definieer de grootte van het scherm
WIDTH, HEIGHT = 1000, 800

# Maak het venster
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Stel de titel van het venster in
pygame.display.set_caption("Space Dodge")

# Bepaal het volledige pad naar de afbeelding 'bg.jpeg'
image_path = os.path.join(os.path.dirname(__file__), 'bg.jpeg')

# Laad de achtergrondafbeelding en schaal deze naar de grootte van het scherm
BG = pygame.transform.scale(pygame.image.load(image_path), (WIDTH, HEIGHT))

# Breedte en hoogte van de speler
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60

# Snelheid van de speler
PLAYER_VEL = 5

# Breedte en hoogte van een ster
STAR_WIDTH, STAR_HEIGHT = 10, 20

# Snelheid van een ster
STAR_VEL = 3

# Font voor het weergeven van tekst
FONT = pygame.font.SysFont("comicsans", 30)

# Functie om het spel te tekenen
def draw(player, elapsed_time, stars):
    # Tekenen van de achtergrond
    WIN.blit(BG, (0, 0))

    # Tekenen van de tijd
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # Tekenen van de speler
    pygame.draw.rect(WIN, "red", player)

    # Tekenen van de sterren
    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    # Update het scherm
    pygame.display.update()

# Hoofdfunctionaliteit van het spel
def main():
    run = True

    # Initialisatie van variabelen
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    # Hoofdloop van het spel
    while run:
        # Tijd bijhouden en verwerken van gebeurtenissen
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        # Sterren genereren
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        # Gebeurtenissen verwerken
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

               # WASD-toetsen voor beweging
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_w] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_s] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL

        # Beweging en botsing van de sterren
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        # Weergave van 'You Lost!' indien botsing plaatsvond
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        # Tekenen van het spel
        draw(player, elapsed_time, stars)

    # Sluit Pygame af
    pygame.quit()

# Start het spel
if __name__ == "__main__":
    main()