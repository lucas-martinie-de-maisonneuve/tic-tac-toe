import pygame
import random

pygame.init()

W, H = 600, 800
Fenetre = pygame.display.set_mode((W, H))
Fenetre_menu = pygame.display.set_mode((W, H))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()
scores =[]

def random_color_generator():
    return random.randint(100, 240), 0, random.randint(100, 240)

def titre(title):
    for i, lettre in enumerate(title):
        random_color = random_color_generator()
        texte_titre = pygame.font.SysFont('Calibri', 90, bold=True).render(lettre, True, random_color)
        texte_titre_rect = texte_titre.get_rect(center=(50 + i * 50, 100))
        Fenetre.blit(texte_titre, texte_titre_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(10)

def main_menu():
    Fenetre.fill((22, 22, 22))
    i=1
    j=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        titre("Tic-Tac-Toe")

        random_color = random_color_generator()
        play_button_rect = pygame.Rect(W // 2 - 250, 690 - 50, 500, 50)
        pygame.draw.rect(Fenetre, (51, 0, 102), play_button_rect)

        if play_button_rect.collidepoint(pygame.mouse.get_pos()):
            play_text = pygame.font.SysFont('Calibri', 60, italic=True, bold=True).render("Jouer", True, random_color)
        else:
            play_text = pygame.font.SysFont('Calibri', 60, italic=True, bold=True).render("Jouer", True, (210, 180, 222))
        play_rect = play_text.get_rect(center=(W // 2, 670))
        Fenetre.blit(play_text, play_rect)

        score_button_rect = pygame.Rect(W // 2 - 250, 705, 500, 50)
        pygame.draw.rect(Fenetre, (51, 0, 102), score_button_rect)
        if score_button_rect.collidepoint(pygame.mouse.get_pos()):
            score_text = pygame.font.SysFont('Calibri', 60, italic=True, bold=True).render("Score", True, (random_color))
        else:
            score_text = pygame.font.SysFont('Calibri', 60, italic=True, bold=True).render("Score", True, (210, 180, 222))
        score_rect = score_text.get_rect(center=(W // 2, 735))
        Fenetre.blit(score_text, score_rect)

        credit = pygame.font.SysFont('Calibri', 18).render("Tic-Tac-Toe par Lucas Martinie", True, (189, 189, 189))
        credit_rect = credit.get_rect(center=(W - 150, H - 15))
        Fenetre.blit(credit, credit_rect)

        if play_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            username()
        elif score_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            show_score()
        elif credit_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]: 
            credit_p()
        if j < 4:
            if i == 9:
                j+=1
            if i < 9:
                menu_img = pygame.image.load(f"img/{i}.png")
                turn = pygame.transform.rotate(menu_img, j*90)
                Fenetre_menu.blit(turn, (W // 2 - menu_img.get_width() // 2, 175))
                pygame.time.get_ticks()
                i+=1
            else:
                i=1
        else:
            j=0
        pygame.display.flip()

def username():
    random_color = random_color_generator()
    font = pygame.font.Font(None, 60)
    user1_input = "Croix"
    user2_input = "Cercle"
    input_name = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if input_name == 1:
                        user1_input = user1_input[:-1]
                    elif input_name == 2:
                        user2_input = user2_input[:-1]
                else:
                    if input_name == 1:
                        user1_input += event.unicode
                    elif input_name == 2:
                        user2_input += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input1_rect.collidepoint(event.pos):
                    input_name = 1
                elif input2_rect.collidepoint(event.pos):
                    input_name = 2
        Fenetre.fill((22, 22, 22))

        croix = pygame.image.load("img/croix.png")
        cercle = pygame.image.load("img/cercle.png")
        i= 0
        while i < 5:
            croix_rect = croix.get_rect(center=(-120 + 120 * 2 * i, 80))
            Fenetre.blit(croix, croix_rect.topleft)
            cercle_rect = cercle.get_rect(center=(120 * 2 * i, 80))
            Fenetre.blit(cercle, cercle_rect.topleft)
            i+=1


        text = pygame.font.SysFont(None, 60, italic=True).render("Enter le nom des joueurs", True, (200, 100, 200))
        text_rect = text.get_rect(center=(W // 2, H // 4 + 20))
        Fenetre.blit(text, text_rect)

        text = pygame.font.SysFont(None, 40, italic=True).render("Joueur 1", True, (200, 100, 200))
        text_rect = text.get_rect(center=(W // 2, H // 2 - 80))
        input1_rect = pygame.Rect(W // 2 - 200, H // 2 - 50, 400, 80)
        pygame.draw.rect(Fenetre, (255, 255, 255), input1_rect, 2)
        input1_surface = font.render(user1_input, True, (155, 155, 155))
        input1_surface_rect = input1_surface.get_rect(center=(input1_rect.centerx, input1_rect.centery))
        Fenetre.blit(input1_surface, (input1_surface_rect.x + 5, input1_surface_rect.y))
        Fenetre.blit(text, text_rect)

        text = pygame.font.SysFont(None, 40, italic=True).render("Joueur 2", True, (200, 100, 200))
        text_rect = text.get_rect(center=(W // 2, H // 2 +100))
        input2_rect = pygame.Rect(W // 2 - 200, H // 2+ 130, 400, 80)
        pygame.draw.rect(Fenetre, (255, 255, 255), input2_rect, 2)
        input2_surface = font.render(user2_input, True, (155, 155, 155))
        input2_surface_rect = input2_surface.get_rect(center=(input2_rect.centerx, input2_rect.centery))
        Fenetre.blit(input2_surface, (input2_surface_rect.x + 5, input2_surface_rect.y))
        Fenetre.blit(text, text_rect)

        launch_button_rect = pygame.Rect(W // 2 - 250, 705, 500, 80)
        pygame.draw.rect(Fenetre, (51, 0, 102), launch_button_rect)
        if launch_button_rect.collidepoint(pygame.mouse.get_pos()):
            launch_text = pygame.font.SysFont('Calibri', 60, italic=True, bold=True).render("Lancer la partie", True, random_color)
        else: 
            launch_text = pygame.font.SysFont('Calibri', 60, italic=True, bold=True).render("Lancer la partie", True, (210, 180, 222))
        launch_rect = launch_text.get_rect(center=(W // 2, 745))
        Fenetre.blit(launch_text, launch_rect)

        if launch_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:       
            play(user1_input, user2_input )
        pygame.display.flip()
        
def play(user1_input,user2_input):
    taille_case = 150
    case = [[''] * 3 for _ in range(3)]
    tour = 0
    coups = 0
    rotate = 0
    rotate_i = 0
    fin_partie = False
    add_score = 0

    def draw_board():
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(Fenetre, (95, 15, 191), (75 + i * taille_case, taille_case + j * taille_case, taille_case, taille_case), 3)
                if case[i][j] == 'X':
                    img = pygame.image.load("img/croix.png")
                elif case[i][j] == 'O':
                    img = pygame.image.load("img/cercle.png")
                else:
                    continue

                img_rect = img.get_rect(center=(75 + i * taille_case + taille_case // 2, taille_case + j * taille_case + taille_case // 2))
                Fenetre.blit(img, img_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and fin_partie == False:
                x, y = event.pos
                for i in range(3):
                    for j in range(3):
                        rect = pygame.Rect(75 + i * taille_case, taille_case + j * taille_case, taille_case, taille_case)
                        if rect.collidepoint(x, y) and case[i][j] == '':
                            case[i][j] = 'X' if tour == 0 else 'O'
                            tour = 1 - tour
                            coups += 1

        Fenetre.fill((22, 22, 22))

        draw_board()

        winner = check_winner(case)
        rotate += 5
        rotate_i -= 5



        if winner == 'X_win':
            message_gagne = pygame.font.Font(None, 36).render(f"{user1_input} remporte", True, (0, 153, 0))
            message_gagne2 = pygame.font.Font(None, 36).render("la partie.", True, (0, 153, 0))
            message_gagne_rect = message_gagne.get_rect(center=(W // 2, H - 125))
            message_gagne_rect2 = message_gagne2.get_rect(center=(W // 2, H - 95))
            Fenetre.blit(message_gagne, message_gagne_rect)
            Fenetre.blit(message_gagne2, message_gagne_rect2)
            left_croix = pygame.image.load("img/croix.png")
            right_croix = pygame.image.load("img/croix.png")
            left_croix_r = pygame.transform.rotate(left_croix, rotate_i)
            right_croix_r = pygame.transform.rotate(right_croix, rotate)
            left_croix_rect = left_croix_r.get_rect(center=(50 + left_croix.get_width() / 2, H - 150 + left_croix.get_height() / 2))
            right_croix_rect = right_croix_r.get_rect(center=(450 + right_croix.get_width() / 2, H - 150 + right_croix.get_height() / 2))
            Fenetre.blit(left_croix_r, left_croix_rect.topleft)
            Fenetre.blit(right_croix_r, right_croix_rect.topleft)
            pygame.time.Clock().tick(30)
            fin_partie = True
            winner_score = user1_input
            if add_score == 0:
                score(winner_score)
                add_score = 1

        elif winner == 'O_win':
            message_gagne = pygame.font.Font(None, 36).render(f"{user2_input} remporte", True, (0, 153, 0))
            message_gagne2 = pygame.font.Font(None, 36).render("la partie.", True, (0, 153, 0))
            message_gagne_rect = message_gagne.get_rect(center=(W // 2, H - 125))
            message_gagne_rect2 = message_gagne2.get_rect(center=(W // 2, H - 95))
            Fenetre.blit(message_gagne, message_gagne_rect)
            Fenetre.blit(message_gagne2, message_gagne_rect2)
            left_cercle = pygame.image.load("img/cercle.png")
            right_cercle = pygame.image.load("img/cercle.png")
            left_cercle_r = pygame.transform.rotate(left_cercle, rotate_i)
            right_cercle_r = pygame.transform.rotate(right_cercle, rotate)
            left_cercle_rect = left_cercle_r.get_rect(center=(50 + left_cercle.get_width() / 2, H - 150 + left_cercle.get_height() / 2))
            right_cercle_rect = right_cercle_r.get_rect(center=(450 + right_cercle.get_width() / 2, H - 150 + right_cercle.get_height() / 2))
            Fenetre.blit(left_cercle_r, left_cercle_rect.topleft)
            Fenetre.blit(right_cercle_r, right_cercle_rect.topleft)
            pygame.time.Clock().tick(30)
            fin_partie = True
            winner_score = user2_input
            if add_score == 0:
                score(winner_score)
                add_score = 1

        elif coups == 9 and winner != 'X_win' and winner != 'O_win':
            message_gagne = pygame.font.Font(None, 36).render("Il n'y a aucun gagnant", True, (211, 47, 47))
            message_gagne2 = pygame.font.Font(None, 36).render("à cette partie", True, (211, 47, 47))
            message_gagne_rect = message_gagne.get_rect(center=(W // 2, H - 125))
            message_gagne_rect2 = message_gagne2.get_rect(center=(W // 2, H - 95))
            Fenetre.blit(message_gagne, message_gagne_rect)
            Fenetre.blit(message_gagne2, message_gagne_rect2)
            fin_partie = True

        if fin_partie == False:
            message_gagne = pygame.font.Font(None, 50).render("C'est au tour des :", True, (191, 201, 202))
            message_gagne_rect = message_gagne.get_rect(center=(W//2 - 60, H - 100))
            Fenetre.blit(message_gagne, message_gagne_rect)
            if tour == 0:
                img = pygame.image.load("img/croix.png")
                img_rect = img.get_rect(center=(W // 2 + 150, H - 100))
                Fenetre.blit(img, img_rect)
            elif tour == 1:
                img = pygame.image.load("img/cercle.png")
                img_rect = img.get_rect(center=(W // 2 + 150, H - 100))
                Fenetre.blit(img, img_rect)


        back_text = pygame.font.Font(None, 36).render("Menu", True, (210, 180, 222))
        back_button_rect = pygame.Rect(75, 50, 200, 60)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)

        if back_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (71, 20, 122), back_button_rect)
        else:
            pygame.draw.rect(Fenetre, (51, 0, 102), back_button_rect)
        Fenetre.blit(back_text, back_text_rect)

        replay_text = pygame.font.Font(None, 36).render("Rejouer", True, (210, 180, 222))
        replay_button_rect = pygame.Rect(325, 50, 200, 60)
        replay_text_rect = replay_text.get_rect(center=replay_button_rect.center)

        if replay_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (71, 20, 122), replay_button_rect)
        else:
            pygame.draw.rect(Fenetre, (51, 0, 102), replay_button_rect)
        Fenetre.blit(replay_text, replay_text_rect)


        if back_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            main_menu()

        elif replay_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            taille_case = 150
            case = [[''] * 3 for _ in range(3)]
            tour = 0
            coups = 0
            rotate = 0
            rotate_i = 0
            fin_partie = False
            add_score = 0
            draw_board()
        pygame.display.flip()

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'X' or board[0][i] == board[1][i] == board[2][i] == 'X':
            return 'X_win'
        elif board[i][0] == board[i][1] == board[i][2] == 'O' or board[0][i] == board[1][i] == board[2][i] == 'O':
            return 'O_win'
    
    if board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return 'O_win'
    elif board[0][2] == board[1][1] == board[2][0] == 'X' or board[0][0] == board[1][1] == board[2][2] == 'X':
        return 'X_win'
    else:
        return None

def score(winner_score):
    global scores
    player_exists = False

    if not scores:
        scores = [(winner_score, 1)]
    else:
        for i, (name, score) in enumerate(scores):
            if name == winner_score:
                scores[i] = (name, score + 1)
                player_exists = True
                break

        if not player_exists:
            scores.append((winner_score, 1))
        
def show_score():
    Fenetre.fill((22, 22, 22))
    global scores

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        text = pygame.font.SysFont('Calibri', 60, italic=True).render("Tableau des scores", True, (200, 100, 200))
        text_rect = text.get_rect(center=(W // 2, 100))
        Fenetre.blit(text, text_rect)

        y_position = H // 4
        for name, score in scores:
            score_text = pygame.font.Font(None, 40).render(f"{name}: {score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(W // 2, y_position))
            Fenetre.blit(score_text, score_rect)
            y_position += 30

        back_text = pygame.font.SysFont('Calibri', 36).render("Menu", True, (210, 180, 222))
        back_button_rect = pygame.Rect(W // 2 - 200, H - 40, 400, 35)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)

        if back_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (71, 20, 122), back_button_rect)
        else:
            pygame.draw.rect(Fenetre, (51, 0, 102), back_button_rect)
        Fenetre.blit(back_text, back_text_rect)
        if back_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            main_menu()
        pygame.display.flip()

def credit_p():
    Fenetre.fill((22, 22, 22))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        credit = pygame.font.SysFont('Calibri', 18).render("Tic-Tac-Toe par Lucas Martinie", True, (189, 189, 189))
        credit_rect = credit.get_rect(center=(W - 150, H - 15))
        Fenetre.blit(credit, credit_rect)

        back_text = pygame.font.Font(None, 30).render("Menu", True, (210, 180, 222))
        back_button_rect = pygame.Rect(50, H-20 - 30, 100, 40)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)

        if back_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(Fenetre, (71, 20, 122), back_button_rect)
        else:
            pygame.draw.rect(Fenetre, (51, 0, 102), back_button_rect)
        Fenetre.blit(back_text, back_text_rect)

        if back_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            main_menu()

        pygame.display.flip()

main_menu()