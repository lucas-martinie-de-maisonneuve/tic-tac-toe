import pygame
import random

pygame.init()

W, H = 600, 800
Fenetre = pygame.display.set_mode((W, H))
pygame.display.set_caption("Tic-Tac-Toe")

def random_color_generator():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def main_menu():
    Fenetre.fill((224, 224, 224))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        title = "Tic-Tac-Toe"
        for i, char in enumerate(title):
            random_color = random_color_generator()
            text_tic = pygame.font.Font(None, 120).render(char, True, random_color)
            text_tic_rect = text_tic.get_rect(center=(50 + i * 50, 100))
            Fenetre.blit(text_tic, text_tic_rect)
        pygame.time.delay(200)
        
        menu_img = pygame.image.load("img/menu.png")
        Fenetre.blit(menu_img, (W // 2 - menu_img.get_width() // 2, 175))

        play_text = pygame.font.SysFont(None, 90, italic=True).render("Jouer", True, (92, 107, 192))
        play_rect = play_text.get_rect(center=(W // 2, 675))
        play_button_rect = pygame.Rect(W // 2 - 250, 675 - 50, 500, 100)

        if play_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (159, 168, 218), play_button_rect)
        else:
            pygame.draw.rect(Fenetre, (176, 196, 222), play_button_rect)

        Fenetre.blit(play_text, play_rect)

        credit = pygame.font.Font(None, 20).render("Programme par Lucas Martinie", True, (0, 0, 0))
        credit_rect = credit.get_rect(center=(W - 140, H - 20))
        Fenetre.blit(credit, credit_rect)

        if play_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            grille()


        pygame.display.flip()

def grille():
    c = 150
    matrix = [['' for _ in range(3)] for _ in range(3)]

    def draw_board():
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(Fenetre, (169, 50, 38), (75 + i * c, c + j * c, c, c), 3)
                if matrix[i][j] == 'X':
                    pygame.draw.line(Fenetre, (0, 0, 0), (90 + i * c, 165 + j * c), (210 + i * c, 285 + j * c), 3)
                    pygame.draw.line(Fenetre, (0, 0, 0), (210 + i * c, 165 + j * c), (90 + i * c, 285 + j * c), 3)
                elif matrix[i][j] == 'O':
                    pygame.draw.circle(Fenetre, (0, 0, 0), (150 + i * c, 225 + j * c), 50, 3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Fenetre.fill((224, 224, 224))

        draw_board()

        back_text = pygame.font.Font(None, 36).render("Retour au Menu", True, (0, 0, 0))
        back_button_rect = pygame.Rect(W // 2 - 125, H - 50, 250, 40)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)

        if back_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (0, 169, 247), back_button_rect)
        else:
            pygame.draw.rect(Fenetre, (0, 169, 247), back_button_rect, 2)

        if back_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return "back"
        Fenetre.blit(back_text, back_text_rect)

        pygame.display.flip()

main_menu()
